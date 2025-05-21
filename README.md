# Cloud Tools API

Une API FastAPI déployée sur Google Cloud Run qui interagit avec Google Cloud Storage et Vertex AI.

## Fonctionnalités

- `GET /hello` : Message de bienvenue
- `GET /status` : Date et heure du serveur
- `GET /data` : Lecture des données depuis Google Cloud Storage
- `POST /data` : Ajout de données dans Google Cloud Storage
- `GET /joke` : Génération de blagues via Vertex AI

## Prérequis

- Python 3.11+
- Docker
- Compte Google Cloud Platform
- Clé de service GCP avec les permissions nécessaires

## Configuration

1. Créez un fichier `.env` à la racine du projet avec les variables suivantes :
```env
BUCKET_NAME=votre-bucket-name
FILE_PATH=data/data.json
PROJECT_ID=votre-project-id
LOCATION=europe-west1
```

2. Assurez-vous d'avoir les credentials GCP configurés localement :
```bash
export GOOGLE_APPLICATION_CREDENTIALS="chemin/vers/votre/cle-service.json"
```

## Installation et exécution en local

1. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix/macOS
# ou
.\venv\Scripts\activate  # Sur Windows
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancez l'application :
```bash
uvicorn main:app --reload
```

## Utilisation avec Docker

1. Construisez l'image :
```bash
docker build -t cloud-tools-api .
```

2. Exécutez le conteneur :
```bash
docker run -p 8080:8080 \
  -e BUCKET_NAME=votre-bucket-name \
  -e FILE_PATH=data/data.json \
  -e PROJECT_ID=votre-project-id \
  -e LOCATION=europe-west1 \
  -v /chemin/vers/credentials.json:/app/credentials.json \
  -e GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json \
  cloud-tools-api
```

## Déploiement sur Google Cloud Run

1. Construisez et poussez l'image vers Google Container Registry :
```bash
gcloud builds submit --tag gcr.io/votre-project-id/cloud-tools-api
```

2. Déployez sur Cloud Run :
```bash
gcloud run deploy cloud-tools-api \
  --image gcr.io/votre-project-id/cloud-tools-api \
  --platform managed \
  --region europe-west1 \
  --allow-unauthenticated
```

## Documentation API

Une fois l'application lancée, accédez à la documentation Swagger UI :
- En local : http://localhost:8080/docs
- Sur Cloud Run : https://votre-url/docs

## Sécurité

- Assurez-vous de ne jamais commiter vos credentials GCP
- Utilisez des variables d'environnement pour les informations sensibles
- Configurez les permissions IAM appropriées sur GCP

## Contribution

1. Fork le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Créez une Pull Request 