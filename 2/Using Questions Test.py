from random import *
import time
#player_info[0] is the player name the default name is 'default'
#player_info[1] is the player level
#player_info[2] is the player level progress

#Get addition questions from the addition_questions.txt file
addition_questions_txt = open("addition_questions.txt","r")
addition_questions = addition_questions_txt.readlines()
for index in range(0,len(addition_questions)):
    addition_questions[index] = addition_questions[index].replace("\n","")
addition_questions_txt.close()

#Get player info from the player_level.txt file
def read_player_info():
    player_info_txt = open("player_info.txt","r")
    player_info = player_info_txt.readlines()
    for index in range(0,len(player_info)):
        player_info[index] = player_info[index].replace("\n","")
    player_info_txt.close()
    return player_info

#Removes all the list features from the player info string and puts it back into a format that is displayed the same as the text document it grabs from
def remove_list_features_for_player_info(playerInfo):
    for i in range(0,len(playerInfo)):
        playerInfo = playerInfo.replace("[","")
    for i in range(0,len(playerInfo)):
        playerInfo = playerInfo.replace("]","")
    for i in range(0,len(playerInfo)):
        playerInfo = playerInfo.replace(",","\n")
    for i in range(0,len(playerInfo)):
        playerInfo = playerInfo.replace("'","")
    for i in range(0,len(playerInfo)):
        playerInfo = playerInfo.replace(" ","")
    return playerInfo

#Print player statistics. E.g level
def print_player_stats(player_level_str, player_level_progress_int, player_level_int, player_name):
    player_level_progress_str = str(player_level_progress_int)
    player_level_str = str(player_level_int)
    print("|  Level: " + player_level_str, end="  |  ")
    print("Level progress: " + player_level_progress_str + "/" + str(10 + (player_level_int * 2)), end="  |  ")
    print("User: " + player_name + "  |")

#Put the changed information/player_info back onto the txt file so it can be read again later.
def info_back_to_txt_file(player_info):
    write_to_player_info_txt = open("player_info.txt","w")
    player_info = remove_list_features_for_player_info(player_info)
    write_to_player_info_txt.write(player_info)
    write_to_player_info_txt.close()
    
def choose_catagory():
    print("To choose a catagory use the numbers 1,2,3 or 4.\n 1. Addition\n 2. Subraction\n 3. Multiplication\n 4. Division\n")
    chosen_catagory = input("What would you like to practice? ")
    try:
        chosen_catagory = int(chosen_catagory)
        if (chosen_catagory == 1):
            print("addition")
        elif (chosen_catagory == 2):
            print("Subtraction")
        elif (chosen_catagory == 3):
            print("Multiplication")
        elif (chosen_catagory == 4):
            print("Division")
        else:
            print("Please enter a number from 1 to 4\n")
            time.sleep(2)
            choose_catagory()
    except:
        print("Please enter a number from 1 to 4\n")
        time.sleep(2)
        choose_catagory()

player_info = read_player_info()
player_name = player_info[0]
player_level_str = player_info[1]
player_level_progress_str = player_info[2]
player_level_int = int(player_level_str)
player_level_progress_int = int(player_level_progress_str)
#player_level_progress_int += 1
player_level_progress_str = str(player_level_progress_int)

if (player_name == "default"):
    player_name = input("Hello new user, what is your name? ")
    player_info[0] = player_name
    player_info = str(player_info)
    info_back_to_txt_file(player_info)
    print("Welcome " + player_name + ", to Basic Maths Study Tool!")
    print("This program is to help you learn basic addition, subtraction, multiplication and division.")
    choose_catagory()
else:
    print_player_stats(player_level_str, player_level_progress_int, player_level_int, player_name)
    print("Welcome back " + player_name +".")
    choose_catagory()

#print(addition_questions[0])
#print(player_level_str)
#print(player_level_progress_str)

if player_level_progress_int >= (player_level_int + 10):
    player_level_int += 1
    player_level_progress_int = 0
    player_level_progress_str = str(player_level_progress_int)
    player_info[2] = player_level_progress_str
    player_level_str = str(player_level_int)
    player_info[1] = player_level_str

player_info = read_player_info()
player_info[1] = player_level_str
player_info[2] = player_level_progress_str
player_info = str(player_info)
info_back_to_txt_file(player_info)