# TODO: Find a way to circumvent the bloody YT "bot protection"
# this bot protection only flags static IPs - figure out PO tokens later

import ytp
import dependencies
import playlist

def troubleshooter():
    print("\n===== Troubleshooting =====")
    print("1. YouTube requires sign-in")
    print("2. Set up JS runtime")
    print("3. Set up FFmpeg")
    print("4. Reinstall yt-dlp")
    print("\n===== Storage =====")
    print("5. Set up HTTP fileserver...")
    print("6. Main menu\n")

    while True:
        try:
            user_input = int(input("Enter an option: "))
        except ValueError:
            print("Invalid option. ")
        if (user_input == 1):
            print("Assuming that cookies.txt is in song directory")
            playlist.sign_in()
        elif (user_input == 2):
            dependencies.install_deno()
        elif (user_input == 3):
            dependencies.install_something("ffmpeg")
        elif (user_input == 4):
            dependencies.install_youtube()
        elif (user_input == 5):
            print("Sorry not yet implemented.")
        elif (user_input == 6):
            main_menu()
            return 0
        else:
            print("Invalid option.")

def main_menu():
    print("\n===== MediaInator =====")
    print("Select an option: ")
    print("1. Browse music library")
    print("2. Search for a song to download")
    print("3. Enter a video URL of the song to download")
    print("4. Settings")
    print("5. Pause audio")
    print("6. Exit program\n")

main_menu()
while True:
    try:
        user_input = int(input("Enter an option: "))
    except ValueError:
        print("Invalid option")
    if (user_input == 1):
        playlist.start()
        main_menu()
    if (user_input == 2):
        # thing
        print("Sorry not yet implemented.")
    elif (user_input == 3):
        print("Enter the video ID of the song: ")
        user_url = input()
        print(ytp.download_mp3("https://youtube.com/watch?v=" + user_url))
    elif (user_input == 4):
        troubleshooter()
    elif (user_input == 5):
        playlist.pause()
    elif (user_input == 6):
        break
    else:
        continue



