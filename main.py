from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import storage
from google.cloud import aiplatform
from datetime import datetime
import json
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

app = FastAPI(title="DataTools API")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration Google Cloud
try:
    storage_client = storage.Client()
    bucket_name = os.getenv("BUCKET_NAME")
    file_path = os.getenv("FILE_PATH")
    project_id = os.getenv("PROJECT_ID")
    location = os.getenv("LOCATION")
    
    print(f"Configuration GCP:")
    print(f"Project ID: {project_id}")
    print(f"Bucket: {bucket_name}")
    print(f"File path: {file_path}")
    print(f"Location: {location}")
except Exception as e:
    print(f"Erreur lors de l'initialisation de GCP: {str(e)}")

# Initialisation de Vertex AI
aiplatform.init(project=project_id, location=location)

@app.get("/hello")
async def hello():
    return {"message": "Bienvenue sur l'API DataTools!"}

@app.get("/status")
async def status():
    return {
        "status": "OK",
        "message": "La connexion est établie",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/data")
async def read_data():
    try:
        print(f"Tentative de lecture depuis {bucket_name}/{file_path}")
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_path)
        content = blob.download_as_text()
        return json.loads(content)
    except Exception as e:
        error_msg = f"Erreur lors de la lecture des données: {str(e)}"
        print(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)

@app.post("/data")
async def write_data(data: dict):
    try:
        print(f"Tentative d'écriture dans {bucket_name}/{file_path}")
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_path)
        
        # Lire le contenu existant
        try:
            content = json.loads(blob.download_as_text())
        except:
            content = {"data": []}
        
        # Ajouter la nouvelle entrée avec un timestamp
        new_entry = {
            "timestamp": datetime.now().isoformat(),
            **data
        }
        content["data"].append(new_entry)
        
        # Sauvegarder le fichier mis à jour
        blob.upload_from_string(
            json.dumps(content, indent=2),
            content_type='application/json'
        )
        
        return {
            "message": "Données ajoutées avec succès",
            "new_entry": new_entry
        }
    except Exception as e:
        error_msg = f"Erreur lors de l'écriture des données: {str(e)}"
        print(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)

@app.get("/joke")
async def generate_joke():
    try:
        model = aiplatform.GenerativeModel("gemini-pro")
        response = model.generate_content(
            "Génère une blague drôle en français. La blague doit être courte et professionnelle."
        )
        return {"joke": response.text}
    except Exception as e:
        # Fallback local si Vertex AI n'est pas disponible
        jokes = [
            "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau !",
            "Qu'est-ce qu'un canard qui fait du vélo ? Un canard qui pédale !",
            "Pourquoi les poissons sont-ils si mauvais en tennis ? Parce qu'ils ont toujours la raquette mouillée !"
        ]
        import random
        return {"joke": random.choice(jokes)} 