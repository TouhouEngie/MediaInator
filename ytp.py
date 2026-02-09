import dependencies

while True:
    try:
        import yt_dlp as youtube
        break
    except ImportError:
        dependencies.install_youtube()

# you must also have ffmpeg and deno installed!

parameters = {
    'format': 'mp3/bestaudio/best', # Download best quality
    'outtmpl': './songs/%(title)s.%(ext)s', # Output template
    'noplaylist': True, # Don't download a playlist
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': "mp3",
    }]
}

def sign_in(pathway):
    parameters.update({'cookies': f'{pathway}/cookies.txt'})

def download_mp3(url):
    try:
        with youtube.YoutubeDL(parameters) as download:
            info = download.extract_info(url, download=True)
            print("Download successful!")
            
            # video metadata
            title = info.get('title', 'N/A') + ".mp3"
            duration = info.get('duration', 'N/A')
            
            return title

    except Exception as err:
        print(f"An error occurred: {err}")
