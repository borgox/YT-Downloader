from pytube import YouTube
from src.colors import Colors, ForegroundColors
import os
import re

class Downloader:
    def __init__(self):
        pass

    @staticmethod
    def by_url(url, quality='highest'):
        downloaded = False
        video = YouTube(url, on_progress_callback=print_progress, on_complete_callback=print_complete)
        try:
            video.check_availability()
            stream = video.streams.get_highest_resolution() if quality == 'highest' else video.streams.get_by_resolution(quality)
            if stream is not None:
                global filename
                filename = sanitize_filename(video.title)
                stream.download("downloaded/", filename=filename, max_retries=5, skip_existing=True)
                downloaded = True
        except Exception as e:
            print(f"{ForegroundColors.CYAN}An error occurred:{ForegroundColors.RED}{Colors.BOLD}", str(e), Colors.RESET)
        return "Downloaded." if downloaded else "Not Downloaded."

def print_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"{ForegroundColors.YELLOW}Downloading: {ForegroundColors.MAGENTA}{percentage:.2f}%{Colors.RESET}")

def print_complete(stream, file_handle):
    downloaded_path = os.path.join(os.path.expanduser("~"), "downloaded", filename)
    print(f"{ForegroundColors.GREEN}Download Complete: {ForegroundColors.YELLOW}{downloaded_path}{Colors.RESET}")
def sanitize_filename(filename):
    # Remove invalid characters
    invalid_chars = r'[<>:"/\\|?*]'
    filename = re.sub(invalid_chars, '_', filename)
    return filename.replace(" ", "_") + ".mp4"