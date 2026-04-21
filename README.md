# 🎬 YouTube Downloader Flask

Simple Flask web server for downloading YouTube videos using yt-dlp, exposed publicly via ngrok.

## ⚙️ How it works
Web page (index.html) with URL + quality selection  
POST request to /download  
Download handled via yt-dlp  
File sent directly to the client  
Automatic deletion after 5 minutes  
External access via ngrok  

## 📦 Installation

### 1. Clone the repo
git clone https://github.com/your-repo/yt-downloader-flask.git  
cd yt-downloader-flask  

### 2. Create virtual environment
python -m venv venv  

### 3. Activate environment

Windows:  
venv\Scripts\activate  

Linux / Mac:  
source venv/bin/activate  

### 4. Install dependencies
pip install -r requirements.txt  

## 🔑 Configuration

### ngrok
Create an account: https://ngrok.com  
Get your auth token  
Replace in code:  
ngrok.set_auth_token("YOUR_TOKEN_HERE")  

### YouTube cookies (recommended)
Export cookies using a browser extension  
Place cookies.txt at the project root  

## 🚀 Run

python app.py  

Public URL generated:  
https://xxxx.ngrok.io  

## 📁 Project structure

/project  
│── app.py  
│── requirements.txt  
│── cookies.txt  
│── /downloads  
│── /templates  
│   └── index.html  
│── /static  
│   └── script.js  
