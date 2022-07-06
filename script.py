######
# song mover
'''
1. Get songs in file, turn into a string
2. Possible convert the string to match song name
3. Once each song can match, move song in a specific folder
'''
import os
import shutil
from string import ascii_letters


def spec_char_replacer(list_replace,list_append):

    for song in list_replace:
        for letter in range(len(song)):
            if song[letter] not in ascii_letters and song[letter] not in '0123456789':
                song = song.replace(song[letter],"_")
        list_append.append(song)
        


# getting the song names in file
song_list = [] # song names of daily tunes v2 playlist
song_list_two = [] # song names of daily tunes v2 playlist


with open('C:\\Users\\ASUS\\song_list\\daily_tunes_song_list.txt', 'r') as f:
    contents = f.readlines()
    print(contents)

spec_char_replacer(contents,song_list)


daily_tunes_dir = os.listdir('C:\\Users\\ASUS\\daily_tunes')

new_song = ''

for song in daily_tunes_dir:

    newsong = song.replace(".mp3","")
    song_list_two.append(newsong)



'''
replace all special characters in song with (_) 
this will hopefully match each song. 
'''


#for song in song_list:
#    print(song)
#    if song in song_list_two:
#        print("True! Song is in song_list_two")
#    else:
#        print('False! Not in song_list_two')

def space_remover(name_list):
    for word in name_list:
        if word == '':
            name_list.pop(name_list.index(word))
#
import re

original_song_names = []
song_one = []
song_two = []

for song_name in song_list:
    print(song_name)
    song_one = re.split(r"_+", song_name) # words of the song_name in a list
    space_remover(song_one)
    bool = False
    while True:
        for song in song_list_two:
            song_two = re.split(r"_+", song) # words of the song in a list
            space_remover(song_two)
            
            if song_one == song_two:
                bool = True
                break
        if not bool:
            print('False')
        elif bool:
            print('True')
        break
               

