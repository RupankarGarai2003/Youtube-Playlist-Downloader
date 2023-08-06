from pytube import Playlist

def download_playlist(playlist_url, download_folder):
    playlist = Playlist(playlist_url)
    for video in playlist.videos:
        print(f"Downloading: {video.title}")
        video.streams.get_highest_resolution().download(output_path=download_folder)

if __name__ == "__main__":
    playlist_url = "https://youtube.com/playlist?list=PLdOKnrf8EcP17p05q13WXbHO5Z_JfXNpw"  # Replace this with the URL of the playlist you want to download
    download_folder = r"D:\VIDEOS\Study\Computer\SQl"  # Use raw string for the folder path

    download_playlist(playlist_url, download_folder)
