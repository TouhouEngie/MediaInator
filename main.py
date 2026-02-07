# TODO: Find a way to circumvent the bloody YT "bot protection"

import ytp
import dependencies

def troubleshooter():
    print("\n=====Troubleshooting Menu=====")
    print("1. YouTube requires sign-in")
    print("2. Set up JS runtime")
    print("3. Set up FFmpeg")
    print("4. Main menu\n")

    while True:
        try:
            user_input = int(input("Enter an option: "))
        except ValueError:
            print("Invalid option. ")
        if (user_input == 1):
            print("Sorry not yet implemented.")
        elif (user_input == 2):
            dependencies.install_deno()
        elif (user_input == 3):
            dependencies.install_something("ffmpeg")
        elif (user_input == 4):
            main_menu()
            return 0
        else:
            print("Invalid option.")

def main_menu():
    print("\n===== MediaInator =====")
    print("Select an option: ")
    print("1. Search for a song to download")
    print("2. Enter a video URL of the song to download")
    print("3. Troubleshoot")
    print("4. Exit program\n")

main_menu()
while True:
    try:
        user_input = int(input("Enter an option: "))
    except ValueError:
        print("Invalid option")
    if (user_input == 1):
        # thing
        print("Sorry not yet implemented.")
    elif (user_input == 2):
        print("Enter the video ID of the song: ")
        user_url = input()
        print(ytp.download_mp3("https://youtube.com/watch?v=" + user_url))
    elif (user_input == 3):
        troubleshooter()
    elif (user_input == 4):
        break
    else:
        continue



