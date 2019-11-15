# Write a function 'music_func' that takes 3 parameters --
#  music type, music group, vocalist -- 
# and prints them all out as shown in the example below.
#  In case no input is provided by the user, the function should assume these default values for the parameters: 
# "Classic Rock", "The Beatles", "Freddie Mercury".
# The main program is given. 

# Input music, group, singer: Alternative Rock,Pearl Jam,Chris Cornell
# The best type of music is Alternative Rock
# The best music group is Pearl Jam
# The best lead vocalist is Chris Cornell
# The best type of music is Classic Rock
# The best music group is The Beatles
# The best lead vocalist is Freddie Mercury

def music_func(music_type = "Classic rock", music_group = "The Beatles", vocalist = "Freddie Mercury"):
    print("The best type of music is", music_type)
    print("The best music group is", music_group)
    print("The best lead vocalist is", vocalist)
#definition for music_func goes here

def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()