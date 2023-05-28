from src.download import Downloader
import pytube
import os
from src.colors import Colors, ForegroundColors, BackgroundColors
os.system("cls " if os.name == "nt" else "clear")
def main():
    print(f""" {ForegroundColors.RED}{Colors.BOLD}

 __     _________   _____                      _                 _           
 \ \   / /__   __| |  __ \                    | |               | |          
  \ \_/ /   | |    | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \   /    | |    | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    | |     | |    | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
    |_|     |_|    |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                             
                                     {Colors.RESET}  {ForegroundColors.RED} [{ForegroundColors.CYAN}https://github.com/borgox/YT-Downloader{ForegroundColors.RED}]                                                        

    """, Colors.RESET)
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