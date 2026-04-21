from flask import Flask , render_template , request , send_file
import yt_dlp
import os
import time
import threading
from pyngrok import ngrok
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download' , methods = ["POST"])
def download():
    url = request.form["url"]
    quality = request.form["quality"]
    print(url)
    print(quality)
    
    ydl_opts = {
    "outtmpl": "downloads/%(title)s.%(ext)s",

    # Format safe
    "format": f"best[height<={quality}]/best",

    # Headers solides
    "http_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    },

    # Cookies
    "cookiefile": "cookies.txt",

    # Anti-blocage yt-dlp
    "extractor_args": {
        "youtube": {
            "player_client": ["android", "tv"]
        }
    },

    # Réseau / retry
    "retries": 10,
    "fragment_retries": 10,
    "sleep_interval": 1,
    "max_sleep_interval": 3,

    # stabilité
    "quiet": False,
    "no_warnings": False,}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    threading.Thread(
        target=lambda: (time.sleep(300), os.path.exists(filename) and os.remove(filename)),
        daemon=True
    ).start()
    return send_file(filename, as_attachment=True)


ngrok.set_auth_token("TOKEN NGROK")
ngrok.kill()
public_url = ngrok.connect(5000)
print("URL ngrok :", public_url)

app.run(port=5000 , debug=False, use_reloader=False)
