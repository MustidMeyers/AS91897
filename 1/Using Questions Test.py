from random import *

#Get addition questions from the addition_questions.txt file
#addition_questions_txt = open("addition_questions.txt","r")
#addition_questions = addition_questions_txt.readlines()
#for index in range(0,len(addition_questions)):
    #addition_questions[index] = addition_questions[index].replace("\n","")
#addition_questions_txt.close()

#Get player info from the player_level.txt file
player_info_txt = open("player_info.txt","r")
player_info = player_info_txt.readlines()
for index in range(0,len(player_info)):
    player_info[index] = player_info[index].replace("\n","")
player_level_progress_str = player_info[1]
player_level_str = player_info[0]
player_info_txt.close()

#print(addition_questions[0])
#print(player_level_str)
#print(player_level_progress_str)

player_level_int = int(player_level_str)
player_level_progress_int = int(player_level_progress_str)
player_level_progress_int += 1
player_level_progress_str = str(player_level_progress_int)

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
def print_player_stats(player_level_str, player_level_progress_int, player_level_int):
    player_level_progress_str = str(player_level_progress_int)
    player_level_str = str(player_level_int)
    print("Level: " + player_level_str)
    print("Level progress: " + player_level_progress_str + "/" + str(10 + player_level_int))

def info_back_to_txt_file(player_info):
    write_to_player_info_txt = open("player_info.txt","w")
    player_info = remove_list_features_for_player_info(player_info)
    write_to_player_info_txt.write(player_info)
    write_to_player_info_txt.close()
    print_player_stats(player_level_str, player_level_progress_int, player_level_int)

if player_level_progress_int >= (player_level_int + 10):
    player_level_int += 1
    player_level_progress_int = 0
    player_level_progress_str = str(player_level_progress_int)
    player_info[1] = player_level_progress_str
    player_level_str = str(player_level_int)
    player_info[0] = player_level_str

player_info[0] = player_level_str
player_info[1] = player_level_progress_str
player_info = str(player_info)
info_back_to_txt_file(player_info)