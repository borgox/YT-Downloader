from src.download import Downloader
import pytube
import os
from src.colors import Colors, ForegroundColors, BackgroundColors
os.system("cls " if os.name == "nt" else "clear")
def main():
    url = input(f"{ForegroundColors.GREEN}Insert an {Colors.BOLD}{Colors.UNDERLINE}URL{Colors.RESET}{ForegroundColors.GREEN} for the {ForegroundColors.RED}youtube{ForegroundColors.GREEN} video: {Colors.RESET}")
    try:
        x = pytube.YouTube(url)
        x.check_availability()
    except:
        pass
    downloader = Downloader()
    result = downloader.by_url(url, quality='highest')
    if result == "Downloaded.":
        input(f"{ForegroundColors.BLUE}Press {Colors.BOLD}ENTER{Colors.RESET}{ForegroundColors.BLUE} to exit.")
        exit(code="200")
    else:
        
        input(f"{ForegroundColors.BLUE}Press {Colors.BOLD}ENTER{Colors.RESET}{ForegroundColors.BLUE} to exit.")
        exit(code="400")
if __name__ == "__main__":
    main()