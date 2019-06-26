import time, random
#player_info[0] is the player name the default name is 'default'
#player_info[1] is the player level
#player_info[2] is the player level progress

#Get addition questions from the basic_addition_questions.txt file
def read_basic_addition_questions():
    basic_addition_questions_txt = open("basic_addition_questions.txt","r")
    basic_addition_questions = basic_addition_questions_txt.readlines()
    for index in range(0,len(basic_addition_questions)):
        basic_addition_questions[index] = basic_addition_questions[index].replace("\n","")
    basic_addition_questions_txt.close()
    return basic_addition_questions

#Get addition questions answers from the basic_addition_questions.txt file
def read_basic_addition_questions_answers():
    basic_addition_questions_answers_txt = open("basic_addition_questions_answers.txt","r")
    basic_addition_questions_answers = basic_addition_questions_answers_txt.readlines()
    for index in range(0,len(basic_addition_questions_answers)):
        basic_addition_questions_answers[index] = basic_addition_questions_answers[index].replace("\n","")
    basic_addition_questions_answers_txt.close()

#Get player info from the player_level.txt file
def read_player_info():
    player_info_txt = open("player_info.txt","r")
    player_info = player_info_txt.readlines()
    for index in range(0,len(player_info)):
        player_info[index] = player_info[index].replace("\n","")
    player_info_txt.close()
    return player_info

#Addition questions 
def basic_addition_practice(basic_addition_questions, player_level_progress_int):#, correct_statements, incorrect_statements, player_level_progress_int):
    quiz_questions = 0
    correct_answers = 0
    incorrect_answers = 0
    
    while quiz_questions <= 9:
        addition_random_question_number = random.randint(0,len(basic_addition_questions) - 1)
        player_answer = input("What is " + basic_addition_questions[addition_random_question_number] + "? ")
        if (player_answer == basic_addition_questions_answers[addition_random_question_number]):
            used_correct_statement = random.choice(correct_statements)
            correct_answers += 1
            print("Correct. " + used_correct_statement + "\n")
        else:
            used_incorrect_statement = random.choice(incorrect_statements)
            incorrect_answers += 1
            print("Incorrect. " + used_incorrect_statement + "\n")
        quiz_questions += 1
    
    if (correct_answers >= 8):
        print("Well done, excellent work! You got " + str(correct_answers) + " questions correct.")
    elif (correct_answers >= 4 and correct_answers <= 7):
        print("Good job. You got " + str(correct_answers) + " questions correct.")
    elif (correct_answers >= 0 and correct_answers <= 3):
        print("You got " + str(correct_answers) + " questions correct. Keep trying to improve your score.")
    player_level_progress_int += int(correct_answers)
    player_level_progress_str = str(player_level_progress_int)
    print(player_level_progress_str)
    #print(correct_answers)
    #print(incorrect_answers)

#Print player statistics. E.g level
def print_player_stats(player_level_str, player_level_progress_int, player_level_int, player_name):
    player_level_progress_str = str(player_level_progress_int)
    player_level_str = str(player_level_int)
    print("|  Level: " + player_level_str, end="  |  ")
    print("Level progress: " + player_level_progress_str + "/" + str(10 + (player_level_int * 2)), end="  |  ")
    print("User: " + player_name + "  |")

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

#Put the changed information/player_info back onto the txt file so it can be read again later.
def info_back_to_txt_file(player_info):
    write_to_player_info_txt = open("player_info.txt","w")
    player_info = remove_list_features_for_player_info(player_info)
    write_to_player_info_txt.write(player_info)
    write_to_player_info_txt.close()

#Asking the player to choose a catagory and then 
def choose_catagory():
    print("To choose a catagory use the numbers 1,2,3 or 4.\n 1. Addition\n 2. Subraction\n 3. Multiplication\n 4. Division\n")
    chosen_catagory = input("What would you like to practice? ")
    try:
        chosen_catagory = int(chosen_catagory)
        if (chosen_catagory == 1):
            print("You chose addition.\n")
            basic_addition_practice(basic_addition_questions, player_level_progress_int)#, correct_statements, incorrect_statements, player_level_progress_int)
        elif (chosen_catagory == 2):
            print("Subtraction")
        elif (chosen_catagory == 3):
            print("Multiplication")
        elif (chosen_catagory == 4):
            print("Division")
        else:
            print("Please enter a number from 1 to 4\n")
            choose_catagory()
    except:
        print("Please enter a number from 1 to 4\n")
        choose_catagory()

player_info = read_player_info()
player_name = player_info[0]
player_level_str = player_info[1]
player_level_progress_str = player_info[2]
player_level_int = int(player_level_str)
player_level_progress_int = int(player_level_progress_str)
#player_level_progress_int += 1
player_level_progress_str = str(player_level_progress_int)
correct_statements = ['Well done!','Keep up the good work!','Good job!','Keep it up!']
incorrect_statements = ['Unlucky, keep trying.','Don\'t give up.','Almost, try again.','Keep trying.','Not quite.']

if (player_name == "default"):
    player_name = input("Hello new user, what is your name? ")
    player_info[0] = player_name
    player_info = str(player_info)
    info_back_to_txt_file(player_info)
    print("Welcome " + player_name + ", to Basic Maths Study Tool!")
    print("This program is to help you learn basic addition, subtraction, multiplication and division.\n")
    choose_catagory()
else:
    print_player_stats(player_level_str, player_level_progress_int, player_level_int, player_name)
    print("Welcome back " + player_name +".\n")
    choose_catagory()

#print(basic_addition_questions[0])
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
player_level_progress_str = basic_addition_practice()
player_info[1] = player_level_str
player_info[2] = player_level_progress_str
print(str(correct_answers))
print(player_level_progress_str)
print(player_info[2])
player_info = str(player_info)
info_back_to_txt_file(player_info)