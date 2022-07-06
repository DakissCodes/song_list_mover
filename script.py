
'''
A script I used to locate missing files in iTunes by matching the names then copying them through shutil module.
'''

import re
import os
import shutil
from string import ascii_letters

# function that replaces spaces and special characters with underscore (_) 
 
def spec_char_replacer(list_replace,list_append):

    for song in list_replace:
        for letter in range(len(song)):
            if song[letter] not in ascii_letters and song[letter] not in '0123456789':
                song = song.replace(song[letter],"_")
        list_append.append(song)
        
# removes blank element in the song name lists (due to spaces)        
        
def space_remover(name_list):
    for word in name_list:
        if word == '':
            name_list.pop(name_list.index(word))
            
song_list = [] # song names of songs I want to locate
song_list_two = [] # song names of the playlist where the songs are


with open('C:\\Users\\ASUS\\song_list\\daily_tunes_song_list.txt', 'r') as f:
    contents = f.readlines()
    print(contents)

spec_char_replacer(contents,song_list) # append the song names to the list


daily_tunes_dir = os.listdir('C:\\Users\\ASUS\\daily_tunes') # lists the song names in the playlist

new_song = ''

for song in daily_tunes_dir:

    newsong = song.replace(".mp3","") # remove ..mp3 extension in name
    song_list_two.append(newsong) 



song_one = [] # song to be located in playlist
song_two = [] # song to match 

true_count = 0 # match count
false_count = 0 # numbers of songs that didn't match 

folder_dir = 'C:\\Users\\ASUS\\daily_tunes\\' 

for song_name in song_list:
    
    song_one = re.split(r"_+", song_name) # name of the song to be located
    print(song_name + '\n')
    space_remover(song_one)
    bool = False
    
    while True:
        
        for song in song_list_two: # loops through songs in the playlist to see if it matches
            song_two = re.split(r"_+", song) 
            space_remover(song_two)
            
            if song_one == song_two: 
                bool = True
                
                print('source: ' + folder_dir + song + '.mp3')
                print('destination: ' + folder_dir + 'daily_tunes_copy')
            
                dest = shutil.copy(folder_dir + song + '.mp3', folder_dir + 'daily_tunes_copy') # copies the file to a folder
                print("file copied successfully!")

        if not bool:
            
            print('DID NOT MATCH _______________________________________________________________________________') # allows you to see songs that cannot be located / did not match name
            false_count += 1
            
        elif bool:
            true_count += 1
            
        break
               
print(str(true_count) + '<-- matched songs')
print(str(false_count) + '<-- unmatched songs')

