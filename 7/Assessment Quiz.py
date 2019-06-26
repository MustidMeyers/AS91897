import time, random

#Get division questions from the b_subtraction_questions.txt file
def read_b_div_q():
    b_div_q_txt = open("b_division_questions.txt","r")
    b_div_q = b_div_q_txt.readlines()
    for index in range(0,len(b_div_q)):
        b_div_q[index] = b_div_q[index].replace("\n","")
    b_div_q_txt.close()
    return b_div_q

#Get division answers from the b_subtraction_answers.txt file
def read_b_div_a(): # read_basic_subtraction_answers
    b_div_a_txt = open("b_division_answers.txt","r")
    b_div_a = b_div_a_txt.readlines()
    for index in range(0,len(b_div_a)):
        b_div_a[index] = b_div_a[index].replace("\n","")
    b_div_a_txt.close()
    return b_div_a

#Get multiplication questions from the b_subtraction_questions.txt file
def read_b_mul_q():
    b_mul_q_txt = open("b_multiplication_questions.txt","r")
    b_mul_q = b_mul_q_txt.readlines()
    for index in range(0,len(b_mul_q)):
        b_mul_q[index] = b_mul_q[index].replace("\n","")
    b_mul_q_txt.close()
    return b_mul_q

#Get multiplication answers from the b_subtraction_answers.txt file
def read_b_mul_a(): # read_basic_subtraction_answers
    b_mul_a_txt = open("b_multiplication_answers.txt","r")
    b_mul_a = b_mul_a_txt.readlines()
    for index in range(0,len(b_mul_a)):
        b_mul_a[index] = b_mul_a[index].replace("\n","")
    b_mul_a_txt.close()
    return b_mul_a

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

def get_txt_data_a_s(): #Get text data for addition and subtraction
    b_add_q = read_b_add_q()
    b_add_a = read_b_add_a()
    b_sub_q = read_b_sub_q()
    b_sub_a = read_b_sub_a()
    return b_add_q, b_add_a, b_sub_q, b_sub_a

def get_txt_data_m_d(): #Get text data for multiplication and division
    b_mul_q = read_b_mul_q()
    b_mul_a = read_b_mul_a()
    b_div_q = read_b_div_q()
    b_div_a = read_b_div_a()
    return b_mul_q, b_mul_a, b_div_q, b_div_a

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
    return player_info, player_name, player_level, player_level_progress

def print_player_stats(player_level, player_level_progress, player_name):
    player_stats = ("|  Level: " + str(player_level) + "  |  " + "Level progress: " + str(player_level_progress) + "/" + str(10 + (int(player_level) * 2)) + "  |  " + "User: " + player_name + "  |\n")
    print("_" * (len(player_stats) - 1))
    print(player_stats)

#Removes all the list features from the player info string and puts it back into a format that is displayed the same as the text document it grabs from
def remove_list_features(player_info):
    player_info = str(player_info)
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
        print("\nWell done, excellent work! You got " + str(correct_answers) + " questions correct.\n")
    elif (correct_answers >= 4 and correct_answers <= 7):
        print("\nGood job. You got " + str(correct_answers) + " questions correct.\n")
    elif (correct_answers >= 0 and correct_answers <= 3):
        print("\nYou got " + str(correct_answers) + " questions correct. Keep trying to improve your score.\n")
    player_level_progress = int(player_level_progress)
    player_level_progress += int(correct_answers)
    player_level_progress = str(player_level_progress)
    return player_level_progress

#Division quiz funtion
def div_quiz():
    b_mul_q, b_mul_a, b_div_q, b_div_a = get_txt_data_m_d()
    quiz_questions = 0
    correct_answers = 0
    while quiz_questions <= 9:
        rand_q_number = random.randint(0,len(b_div_q) - 1)
        player_answer = input("What is " + b_div_q[rand_q_number] + "? ")
        if (player_answer == b_div_a[rand_q_number]):
            correct_answers += 1
            print("Correct")
        else:
            print("Incorrect")        
        quiz_questions += 1
    return correct_answers

#Multiplication quiz funtion
def mul_quiz():
    b_mul_q, b_mul_a, b_div_q, b_div_a = get_txt_data_m_d()
    quiz_questions = 0
    correct_answers = 0
    while quiz_questions <= 9:
        rand_q_number = random.randint(0,len(b_mul_q) - 1)
        player_answer = input("What is " + b_mul_q[rand_q_number] + "? ")
        if (player_answer == b_mul_a[rand_q_number]):
            correct_answers += 1
            print("Correct")
        else:
            print("Incorrect")        
        quiz_questions += 1
    return correct_answers

#Addition quiz funtion
def add_quiz():
    b_add_q, b_add_a, b_sub_q, b_sub_a = get_txt_data_a_s()
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
    b_add_q, b_add_a, b_sub_q, b_sub_a = get_txt_data_a_s()
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

def achievements_function(player_level):
    player_level = int(player_level)
    if player_level >= 1:
        achievements[0] = 'Newbie: Reach level 1'
    if player_level >= 5:
        achievements[1] = 'Beginner: Reach level 5'
    if player_level >= 10:
        achievements[2] = 'Efficient: Reach level 10'
    if player_level >= 15:
        achievements[3] = 'Advanced: Reach level 15'
    if player_level >= 20:
        achievements[4] = 'Expert: Reach level 20'
    if player_level >= 25:
        achievements[5] = 'Master: Reach level 25'    
    print(" " + achievements[0])
    print(" " + achievements[1])
    print(" " + achievements[2])
    print(" " + achievements[3])
    print(" " + achievements[4])
    print(" " + achievements[5])
    print("")
    input("Press 'enter' to continue... ")
    player_level = str(player_level)
    return achievements

#Welcome function
def welcome_user(player_name, player_info, player_level, player_level_progress):
    if (player_name == "default"):
        player_name = input("Hello new user, what is your name? ")
        player_info[0] = player_name
        player_info = str(player_info)
        info_to_file(player_info)
        print("Welcome " + player_name + ", to Basic Maths Study Tool!")
        print("This program is to help you learn basic addition, subtraction, multiplication and division.\n")
    else:
        print("Welcome back " + player_name +".\n")
    #choose_catagory()
    return player_name, player_info

def replay_current_quiz(chosen_catagory, player_level_progress):
    try_again = input("Would you like to take the quiz again? (y / n) ")
    if try_again == "y":
        if (chosen_catagory == 1):
            print("")
            correct_answers = add_quiz()
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress)
            player_level_progress = replay_current_quiz(chosen_catagory, player_level_progress)
        elif (chosen_catagory == 2):
            print("")
            correct_answers = sub_quiz()
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress) 
            player_level_progress = replay_current_quiz(chosen_catagory, player_level_progress)
        elif (chosen_catagory == 3):
            print("")
            correct_answers = mul_quiz()
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress)
            player_level_progress = replay_current_quiz(chosen_catagory, player_level_progress)
        elif (chosen_catagory == 4):
            print("")
            correct_answers = div_quiz()
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress)
            player_level_progress = replay_current_quiz(chosen_catagory, player_level_progress)
    elif try_again == "n":
        print("\nOkay taking you back to the menu.")
        return player_level_progress
    else:
        print("Please enter 'y' or 'n'.\n")
        player_level_progress = replay_current_quiz(chosen_catagory, player_level_progress)
    return player_level_progress

#Get the player to choose one of the maths catagories
def choose_catagory(player_level_progress):
    print("To choose a catagory use the numbers 1,2,3 or 4.\n 1. Addition\n 2. Subraction\n 3. Multiplication\n 4. Division\n")
    chosen_catagory = input("What would you like to practice? ")    
    while type(chosen_catagory) != int:
        try:
            chosen_catagory = int(chosen_catagory)
        except:
            print("\nPlease enter a number.\n")
            print("To choose a catagory use the numbers 1,2,3 or 4.\n 1. Addition\n 2. Subraction\n 3. Multiplication\n 4. Division\n")
            chosen_catagory = input("What would you like to practice? ")            
    else:
        if (chosen_catagory == 1):
            print("\nYou chose addition.\n")
            correct_answers = add_quiz()
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress)
        elif (chosen_catagory == 2):
            print("\nYou chose subtraction\n")
            correct_answers = sub_quiz()
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress)            
        elif (chosen_catagory == 3):
            print("\nYou chose multiplication\n")
            correct_answers = mul_quiz()
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress)
        elif (chosen_catagory == 4):
            print("\nYou chose division, remember this symbol '/' means divide.\n")
            correct_answers = div_quiz()
            player_level_progress = show_quiz_stats(correct_answers, player_level_progress)
        else:
            print("\nPlease enter a number from 1 to 4.\n")
            choose_catagory(player_level_progress)
    player_level_progress = replay_current_quiz(chosen_catagory, player_level_progress)
    return player_level_progress

#Menu function
def menu(player_level_progress, player_level):
    print("Menu: (Please enter a number: 1, 2 or 3)\n 1. Practice maths\n 2. View achievements\n 3. Quit program\n")
    player_choice = input("What would you like to do? ")
    while type(player_choice) != int:
        try:
            player_choice = int(player_choice)        
        except:
            print("\nPlease enter a number.\n")
            print("Menu: (Please enter a number: 1, 2 or 3)\n 1. Practice maths\n 2. View achievements\n 3. Quit program\n")
            player_choice = input("What would you like to do? ")            
    else:
        if player_choice == 1:
            print("\nYou chose practice maths.\n")
            player_level_progress = choose_catagory(player_level_progress)
        elif player_choice == 2:
            print("\nAchievements:")
            achievements = achievements_function(player_level)
        elif player_choice == 3:
            print("\nQuitting")
            exit()
        else:
            print("\nPlease enter a number between 1 and 3.\n")
            menu(player_level_progress, player_level)        
    return player_level_progress

def check_levelup(player_level, player_level_progress, achievements):
    player_level = int(player_level)
    player_level_progress = int(player_level_progress)    
    if player_level_progress >= ((int(player_level) * 2) + 10):
        player_level_progress = (player_level_progress - ((int(player_level) * 2) + 10))
        player_level += 1
    player_level_progress = str(player_level_progress)
    player_level = str(player_level)    
    return player_level, player_level_progress, achievements

def return_values_player_info(player_level, player_level_progress, player_info):
    player_info[1] = player_level
    player_info[2] = player_level_progress
    player_info = str(player_info)
    return player_info

#Main function
def main(achievements):
    player_info, player_name, player_level, player_level_progress = read_player_info()
    print_player_stats(player_level, player_level_progress, player_name)
    player_level_progress = menu(player_level_progress, player_level)
    player_level, player_level_progress, achievements = check_levelup(player_level, player_level_progress, achievements)
    player_info = return_values_player_info(player_level, player_level_progress, player_info)
    info_to_file(player_info)
    main(achievements)

def __inti__ ():
    player_info, player_name, player_level, player_level_progress = read_player_info()
    player_name, player_info = welcome_user(player_name, player_info, player_level, player_level_progress)
    #player_info = return_values_player_info(player_level, player_level_progress, player_info)
    info_to_file(player_info)    
    return player_info, player_name, player_level, player_level_progress

player_info, player_name, player_level, player_level_progress = __inti__()
achievements = ['????', '????', '????', '????', '????', '????']
main(achievements)