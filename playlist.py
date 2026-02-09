import os
import vlc
import ytp
# TODO: switch away from VLC somehow

pathway = "./songs"
current_song = ""
final_list = []

class song:
    def __init__(self, song, name):
        self.song = song
        self.name = name

def start():
    set_up_objects()
    print("Select a song: ")
    for i in range(rin(final_list)):
        print(f"({i+1}) {final_list[i]["name"]}")
    while True:
        try:
            global current_song
            user_input = int(input("Select your song... "))
            current_song = vlc.MediaPlayer(final_list[user_input - 1]["song_path"])
            current_song.play()
            return
        except ValueError:
            print("Invalid option")
        except IndexError:
            print("Invalid option")

def get_path(string):
    global pathway
    pathway = string

def set_up_objects():
    global final_list
    song_list = os.listdir(pathway)
    song_list.remove("names.csv")
    for i in range(rin(song_list)):
        dict_item = {
            "song_path": f"{pathway}/{song_list[i]}",
            "name": song_list[i][0:rin(song_list[i]) - 4]
        }
        final_list.append(dict_item)
    
    file = open(f"{pathway}/names.csv", "r")
    file_list = []
    for line in file:
        file_list.append(line.strip().split(","))
    file.close()
    
    # yes, this is definitely shitty, but will have to do
    for i in range(rin(final_list)):
        for j in range(rin(file_list)):
            if (final_list[i]["song_path"] == file_list[j][1]):
                final_list[i]["name"] = file_list[j][0]

def sign_in():
    ytp.sign_in(pathway)

def pause():
    global current_song
    current_song.stop()

# lol
def rin(thing):
    return len(thing)