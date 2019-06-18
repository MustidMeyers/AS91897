import time, random

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
    print("|  Level: " + str(player_level), end="  |  ")
    print("Level progress: " + str(player_level_progress) + "/" + str(10 + (int(player_level) * 2)), end="  |  ")
    print(player_type + "  |  ", end="")
    print("User: " + player_name + "  |  ")

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

#Quiz funtion
def quiz(b_add_q, b_add_a):
    quiz_questions = 0
    correct_answers = 0
    while quiz_questions <= 9:
        rand_q_number = random.randint(0,len(b_add_q) - 1)
        player_answer = input("What is " + b_add_q[rand_q_number] + "? ")
        if (player_answer == b_add_a[rand_q_number]):
            #used_correct_statement = random.choice(correct_statements)
            correct_answers += 1
            #print("Correct. " + used_correct_statement + "\n")
            print("Correct")
        else:
            #used_incorrect_statement = random.choice(incorrect_statements)
            #incorrect_answers += 1
            #print("Incorrect. " + used_incorrect_statement + "\n")
            print("Incorrect")        
        quiz_questions += 1
    return correct_answers

#Welcome function
def welcome_user(player_name, player_info, player_level, player_level_progress, player_type):
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
    return player_name, player_info

#Get the player to choose one of the maths catagories
def choose_catagory(b_add_q, b_add_a, player_level_progress):
    print("To choose a catagory use the numbers 1,2,3 or 4.\n 1. Addition\n 2. Subraction\n 3. Multiplication\n 4. Division\n")
    chosen_catagory = input("What would you like to practice? ")
    try:
        chosen_catagory = int(chosen_catagory)
    except:
        print("Please enter a number from 1 to 4\n")
        choose_catagory(b_add_q, b_add_a)
    if (chosen_catagory == 1):
        print("You chose addition.\n")
        correct_answers = quiz(b_add_q, b_add_a)
        player_level_progress = show_quiz_stats(correct_answers, player_level_progress)
        #basic_addition_practice(basic_addition_questions, player_level_progress_int)#, correct_statements, incorrect_statements, player_level_progress_int)
    elif (chosen_catagory == 2):
        print("Subtraction")
    elif (chosen_catagory == 3):
        print("Multiplication")
    elif (chosen_catagory == 4):
        print("Division")
    else:
        print("Please enter a number from 1 to 4\n")
        choose_catagory(b_add_q, b_add_a)
    return player_level_progress

#Menu function
def menu(b_add_q, b_add_a, player_level_progress):
    print("Menu:\n 1. Practice maths\n 2. View achievements\n")
    player_choice = input("What would you like to do? ")
    try:
        player_choice = int(player_choice)
    except:
        print("Please enter a number")
        menu()
    if player_choice == 1:
        print("You chose practice maths.\n")
        player_level_progress = choose_catagory(b_add_q, b_add_a, player_level_progress)
    elif player_choice == 2:
        print("Achievements")
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
def main():
    b_add_q = read_b_add_q()
    b_add_a = read_b_add_a()
    player_info, player_name, player_level, player_level_progress, player_type = read_player_info()
    player_name, player_info = welcome_user(player_name, player_info, player_level, player_level_progress, player_type)
    player_level_progress = menu(b_add_q, b_add_a, player_level_progress)
    player_level, player_level_progress = check_levelup(player_level, player_level_progress)
    player_info = return_values_player_info(player_level, player_level_progress, player_info)
    info_to_file(player_info)

main()