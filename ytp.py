import yt_dlp as youtube
import ffmpeg

parameters = {
    'format': 'mp3/bestaudio/best', # Download best quality
    'outtmpl': './%(title)s.%(ext)s', # Output template
    'noplaylist': True, # Don't download a playlist
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': "mp3",
    }]
}

def download_mp3(url):
    try:
        with youtube.YoutubeDL(parameters) as download:
            info = download.extract_info(url, download=True)
            print("Download successful!")
            
            # video metadata
            title = info.get('title', 'N/A')
            duration = info.get('duration', 'N/A')
            print(f"Downloaded: {title}")
            print(f"Duration: {duration} seconds")

    except Exception as err:
        print(f"An error occurred: {err}")
