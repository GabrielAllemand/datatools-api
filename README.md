# 🚀 Mini API Python - GCP Cloud Run

## 🎯 Objectif

Ce projet a été réalisé en équipe dans le cadre d'un mini-projet pédagogique.  
L'objectif était de développer une API en Python (FastAPI), conteneurisée avec Docker, déployée sur Google Cloud Run, et capable :

- de lire et écrire un fichier dans un bucket Google Cloud Storage (GCS)
- de générer des blagues aléatoires via l’API Vertex AI
- de démontrer l'utilisation de Git, Docker, GCP, et des bonnes pratiques de développement

---

## 📌 Endpoints de l’API

| Méthode | Endpoint    | Description |
|---------|-------------|-------------|
| GET     | `/hello`    | Message de bienvenue |
| GET     | `/status`   | Date et heure du serveur |
| GET     | `/data`     | Récupère un fichier JSON ou CSV depuis GCS |
| POST    | `/data`     | Ajoute une entrée dans le fichier GCS |
| GET     | `/joke`     | Renvoie une blague générée par Vertex AI |

---

## 🛠️ Technologies utilisées

- Python (FastAPI)
- Docker
- Google Cloud Storage (GCS)
- Vertex AI (LLM API)
- Cloud Run (déploiement serverless)
- Google Cloud IAM (compte de service)
- Git & GitHub

---

## ⚙️ Lancer le projet en local

1. Cloner le projet :

```bash
git clone https://github.com/<ton-utilisateur>/<ton-repo>.git
cd <ton-repo>
```
```
