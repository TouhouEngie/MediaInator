# TODO: Find a way to circumvent the bloody YT "bot protection"

import ytp

print("\n===== MediaInator =====")
print("Select an option: ")
print("1. Search for a song to download")
print("2. Enter a video URL of the song to download")
print("3. Exit program\n")

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
        ytp.download_mp3("https://youtube.com/watch?v=" + user_url)
    elif (user_input == 3):
        break
    else:
        continue
