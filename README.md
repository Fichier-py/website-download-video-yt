# 🎬 YouTube Downloader Flask

Serveur web simple en Flask permettant de télécharger des vidéos YouTube avec yt-dlp, exposé publiquement via ngrok.

## ⚙️ Fonctionnement
Page web (index.html) avec URL + qualité  
Requête POST vers /download  
Téléchargement via yt-dlp  
Envoi du fichier directement au client  
Suppression automatique après 5 minutes  
Accès externe grâce à ngrok  

## 📦 Installation

### 1. Cloner le repo
git clone https://github.com/ton-repo/yt-downloader-flask.git  
cd yt-downloader-flask  

### 2. Créer un environnement virtuel
python -m venv venv  

### 3. Activer l’environnement

Windows :  
venv\Scripts\activate  

Linux / Mac :  
source venv/bin/activate  

### 4. Installer les dépendances
pip install -r requirements.txt  

## 🔑 Configuration

### ngrok
Crée un compte : https://ngrok.com  
Récupère ton token  
Remplace dans le code :  
ngrok.set_auth_token("TON_TOKEN_ICI")  

### Cookies YouTube (recommandé)
Exporte tes cookies (extension navigateur)  
Place le fichier cookies.txt à la racine  

## 🚀 Lancement

python app.py  

URL publique générée :  
https://xxxx.ngrok.io  

## 📁 Structure du projet

/project  
│── app.py  
│── requirements.txt  
│── cookies.txt  
│── /downloads  
│── /templates  
│   └── index.html  
