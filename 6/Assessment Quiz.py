import time, random

#Get subtraction questions from the b_subtraction_questions.txt file
def read_b_sub_q():
    b_sub_q_txt = open("b_subtraction_questions.txt","r")
    b_sub_q = b_sub_q_txt.readlines()
    for index in range(0,len(b_sub_q)):
        b_sub_q[index] = b_sub_q[index].replace("\n","")
    b_sub_q_txt.close()
    return b_sub_q

#Get subtraction answers from the b_subtraction_answers.txt file
def read_b_sub_a(): # read_basic_subtraction_answers
    b_sub_a_txt = open("b_subtraction_answers.txt","r")
    b_sub_a = b_sub_a_txt.readlines()
    for index in range(0,len(b_sub_a)):
        b_sub_a[index] = b_sub_a[index].replace("\n","")
    b_sub_a_txt.close()
    return b_sub_a

#Get addition questions from the addition_questions.txt file
def read_b_add_q():
    b_add_q_txt = open("b_addition_questions.txt","r")
    b_add_q = b_add_q_txt.readlines()
    for index in range(0,len(b_add_q)):
        b_add_q[index] = b_add_q[index].replace("\n","")
    b_add_q_txt.close()
    return b_add_q

#Get addition answers from the addition_answers.txt file
def read_b_add_a(): # read_basic_addition_answers
    b_add_a_txt = open("b_addition_answers.txt","r")
    b_add_a = b_add_a_txt.readlines()
    for index in range(0,len(b_add_a)):
        b_add_a[index] = b_add_a[index].replace("\n","")
    b_add_a_txt.close()
    return b_add_a

def get_txt_data():
    b_add_q = read_b_add_q()
    b_add_a = read_b_add_a()
    b_sub_q = read_b_sub_q()
    b_sub_a = read_b_sub_a()
    return b_add_q, b_add_a, b_sub_q, b_sub_a

#Get player info from the player_level.txt file
def read_player_info():
    player_info_txt = open("player_info.txt","r")
    player_info = player_info_txt.readlines()
    for index in range(0,len(player_info)):
        player_info[index] = player_info[index].replace("\n","")
    player_info_txt.close()
    player_name = player_info[0]
    player_level = player_info[1]
    player_level_progress = player_info[2]
    player_type = player_info[3]
    return player_info, player_name, player_level, player_level_progress, player_type

def print_player_stats(player_level, player_level_progress, player_name, player_type):
    player_stats = ("|  Level: " + str(player_level) + "  |  " + "Level progress: " + str(player_level_progress) + "/" + str(10 + (int(player_level) * 2)) + "  |  " + player_type + "  |  " + "User: " + player_name + "  |\n")
    #print("|  Level: " + str(player_level), end="  |  ")
    #print("Level progress: " + str(player_level_progress) + "/" + str(10 + (int(player_level) * 2)), end="  |  ")
    #print(player_type + "  |  ", end="")
    #print("User: " + player_name + "  |  ")
    print("_" * (len(player_stats) - 1))
    print(player_stats)

#Removes all the list features from the player info string and puts it back into a format that is displayed the same as the text document it grabs from
def remove_list_features(player_info):
    for i in range(0,len(player_info)):
        player_info = player_info.replace("[","")
    for i in range(0,len(player_info)):
        player_info = player_info.replace("]","")
    for i in range(0,len(player_info)):
        player_info = player_info.replace(",","\n")
    for i in range(0,len(player_info)):
        player_info = player_info.replace("'","")
    for i in range(0,len(player_info)):
        player_info = player_info.replace(" ","")
    return player_info

#Put the changed information/player_info back onto the txt file so it can be read again later.
def info_to_file(player_info):
    player_info = remove_list_features(player_info)
    write_player_info = open("player_info.txt","w")
    write_player_info.write(player_info)
    write_player_info.close()

def show_quiz_stats(correct_answers, player_level_progress):
    if (correct_answers >= 8):
        print("Well done, excellent work! You got " + str(correct_answers) + " questions correct.")
    elif (correct_answers >= 4 and correct_answers <= 7):
        print("Good job. You got " + str(correct_answers) + " questions correct.")
    elif (correct_answers >= 0 and correct_answers <= 3):
        print("You got " + str(correct_answers) + " questions correct. Keep trying to improve your score.")
    player_level_progress = int(player_level_progress)
    player_level_progress += int(correct_answers)
    player_level_progress = str(player_level_progress)
    print(player_level_progress)
    return player_level_progress

#Addition quiz funtion
def add_quiz():
    b_add_q, b_add_a, b_sub_q, b_sub_a = get_txt_data()
    quiz_questions = 0
    correct_answers = 0
    while quiz_questions <= 9:
        rand_q_number = random.randint(0,len(b_add_q) - 1)
        player_answer = input("What is " + b_add_q[rand_q_number] + "? ")
        if (player_answer == b_add_a[rand_q_number]):
            correct_answers += 1
            print("Correct")
        else:
            print("Incorrect")        
        quiz_questions += 1
    return correct_answers

#Subtraction quiz funtion
def sub_quiz():
    b_add_q, b_add_a, b_sub_q, b_sub_a = get_txt_data()
    quiz_questions = 0
    correct_answers = 0
    while quiz_questions <= 9:
        rand_q_number = random.randint(0,len(b_sub_q) - 1)
        player_answer = input("What is " + b_sub_q[rand_q_number] + "? ")
        if (player_answer == b_sub_a[rand_q_number]):
            correct_answers += 1
            print("Correct")
        else:
            print("Incorrect")        
        quiz_questions += 1
    return correct_answers

#Welcome function
def welcome_user(player_name, player_info, player_level, player_level_progress, player_type, first_time_on):
    if (first_time_on == 1):
        first_time_on = 0
        if (player_name == "default"):
            player_name = input("Hello new user, what is your name? ")
            player_info[0] = player_name
            player_info = str(player_info)
            info_to_file(player_info)
            print("Welcome " + player_name + ", to Basic Maths Study Tool!")
            print("This program is to help you learn basic addition, subtraction, multiplication and division.\n")
        else:
            print_player_stats(player_level, player_level_progress, player_name, player_type)
            print("Welcome back " + player_name +".\n")
        #choose_catagory()
    else:
        print_player_stats(player_level, player_level_progress, player_name, player_type)
    return player_name, player_info, first_time_on

#Get the player to choose one of the maths catagories
def choose_catagory(player_level_progress):
    print("To choose a catagory use the numbers 1,2,3 or 4.\n 1. Addition\n 2. Subraction\n 3. Multiplication\n 4. Division\n")
    chosen_catagory = input("What would you like to practice? ")
    try:
        chosen_catagory = int(chosen_catagory)
    except:
        print("Please enter a number from 1 to 4\n")
        choose_catagory(player_level_progress)
    else:
        if (chosen_catagory == 1):
            print("You chose addition.\n")
            correct_answers = add_quiz()
            print(correct_answers)
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress)
        elif (chosen_catagory == 2):
            print("Subtraction\n")
            correct_answers = sub_quiz()
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress)            
        elif (chosen_catagory == 3):
            print("Multiplication")
        elif (chosen_catagory == 4):
            print("Division")
        else:
            print("Please enter a number from 1 to 4\n")
            choose_catagory(player_level_progress)
    return player_level_progress

#Menu function
def menu(player_level_progress):
    print("Menu: (Please enter a number: 1, 2 or 3)\n 1. Practice maths\n 2. View achievements\n 3. Quit program\n")
    player_choice = input("What would you like to do? ")
    try:
        player_choice = int(player_choice)        
    except:
        print("Please enter a number.\n")
        menu(player_level_progress)
    else:
        if player_choice == 1:
            print("You chose practice maths.\n")
            player_level_progress = choose_catagory(player_level_progress)
        elif player_choice == 2:
            print("Achievements")
        elif player_choice == 3:
            print("Quitting")
        else:
            print("Please enter a number.\n")
            menu(player_level_progress)        
    return player_level_progress

def check_levelup(player_level, player_level_progress):
    player_level = int(player_level)
    player_level_progress = int(player_level_progress)    
    if player_level_progress >= ((int(player_level) * 2) + 10):
        player_level_progress = (player_level_progress - ((int(player_level) * 2) + 10))
        player_level += 1
    player_level_progress = str(player_level_progress)
    player_level = str(player_level)    
    return player_level, player_level_progress

def return_values_player_info(player_level, player_level_progress, player_info):
    player_info[1] = player_level
    player_info[2] = player_level_progress
    player_info = str(player_info)
    return player_info

#Main function
def main(first_time_on):
    b_add_q, b_add_a, b_sub_q, b_sub_a = get_txt_data()
    player_info, player_name, player_level, player_level_progress, player_type = read_player_info()
    player_name, player_info, first_time_on = welcome_user(player_name, player_info, player_level, player_level_progress, player_type, first_time_on)
    player_level_progress = menu(player_level_progress)
    player_level, player_level_progress = check_levelup(player_level, player_level_progress)
    player_info = return_values_player_info(player_level, player_level_progress, player_info)
    info_to_file(player_info)
    #main(first_time_on)

first_time_on = 1
main(first_time_on)