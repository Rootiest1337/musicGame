# program to be random quiz on music

import random
import os

users = [["Admin", "Password"], ["Josh", "Letmein"], ["Will", "TeachMe"]]
musiclist = []
scoreboard = []
limit = 0
points = 0
lives = 2
current_user = ""

# FUNCTION DEFINITIONS

# Pulls the details of the music from musicDB.txt
def loadmusic():
    global musiclist
    global limit
    f = open("musicDB.txt", "r")
    music = f.read()
    first_split = music.split("/")
    limit = len(first_split)
    c = 0
    while c < limit:
        second_split = first_split[c].split(",")
        musiclist.append([str(second_split[0]), str(second_split[1])])
        c = c + 1

# Pulls the details of the scoreboard from pointsDB.txt
def loadscoreboard():
    global scoreboard
    f = open ("pointsDB.txt", "r")
    string = f.read()
    if string:
        splitted = string.split("/")
        count = len(splitted)
        c = 0
        while c < count:
            splitted2 = splitted[c].split(",")
            scoreboard.append([str(splitted2[0]), int(splitted2[1])])
            c = c + 1
 
# Generates the Scoreboard || I'm not sure how this sorting method exactly works, but it does what I needed it to. Found it off w3.
def gen_scoreboard():
    global scoreboard
    print("\nHIGH SCORES!\n")
    if scoreboard:
        scores = sorted(scoreboard, key=lambda x: x[1], reverse=True)
        max_scores = 5
        if max_scores > len(scores):
            max_scores = len(scores)
        c = 0
        while c < max_scores:
            print(str(c +1) + ". " + scores[c][0] + " - " + str(scores[c][1]))
            c += 1
        input("\n\nPress RETURN to continue")
        return
    else: print("No High Scores yet! Get in there and makes some!")
    wait = input("\n\nPress RETURN to continue")
     
# The Actual Quiz
def quiz():
    global musiclist
    global limit
    global points
    global lives
    play = "y"
    answer = " "
    while play.lower() != "n":
        quiz_no = random.randint(0, limit - 1)
        question = gen_question(quiz_no)
        lives = 2
        score = 0
        answer = ""
        while answer != "pass":   
            print(question)
            print ("HINT: (Answer is '"+ musiclist[quiz_no][0] + "')")
            print("\nYou Currently have " + str(lives) + " attempts at this question! Your current score is " + str(points) + "!")
            answer = input("Answer : ").lower()
            score = check_answer(answer, quiz_no)
            points = score + points
            if score > 0:
                break
            if lives == 0:
                game_over()
                break
        play = input("\nDo you want to play again? (Y/N) : ")
    game_over()
        

# Creates Question
def gen_question(quiz_no):
    global musiclist
    letters = []
    word_split = musiclist[quiz_no][0].split(" ")
    word_limit = len(word_split)
    c = 0
    while c < word_limit:
         first_letter = list(word_split[c])
         letters.append(first_letter[0])
         c = c + 1
    letter_no = len(letters)
    question = "\nWhat song by " + musiclist[quiz_no][1] + " starts with the letter"
    if letter_no > 1:
        question = question + "s " 
        c = 0
        while c < letter_no:
            if c < (letter_no - 2):
                question = question + str(letters[c]) + ", "
            elif c < (letter_no - 1):
                question = question + str(letters[c]) + " "
            elif c == letter_no - 1:
                    question = question +  "and " + str(letters[c]) + "?"
            c = c + 1
    else:
        question  = question +  " " + str(letters[0]) + "?"
    return question

# Check the Answer of the question
def check_answer(answer, quiz_no):
    global musiclist
    global lives
    points = 0
    correct_answer = musiclist[quiz_no][0].lower()
    if answer == correct_answer:
        if lives == 2:
            points = 3
        elif lives == 1:
            points = 1
        print("\nCORRECT! Well done, you scored " + str(points) + " more points!")
        return(points)
    else:
        lives = lives - 1
        print("\nINCORRECT! Try again!")
        return(points)



# Game over process
def game_over():
    global points
    global lives
    global current_user
    if lives == 0:
        print("\nOh No! You ran out of lives! Sorry but that is game over!")
    print("\nYou managed to score a total of " + str(points) + " points!")
    if points == 0:
        print("Get Gud Noob!")
    elif points < 4:
        print("Hey, not bad going!")
    elif points < 10:
        print("Good going!")
    elif points >= 10:
        print("Wow! You did really well!")
    print("\n How did you do? This is our current High Scores")
    gen_scoreboard()
    if points > 0:
        scoreboard.append([current_user, points])
    
# Menu
def menu():
    global current_user
    opt = 0
    while int(opt) != 3:
        print("\nHi there " + current_user + "! Do you want to...\n")
        print("1. Play the BEST game ever")
        print("2. See the Scoreboard")
        print("3. Quit")
        opt = input("\nPick an Option from the menu: ")
        if int(opt) == 1:
            quiz() 
        elif int(opt) == 2:
            gen_scoreboard()
    end_game()

# Ends the game and saves the scoreboard to file
def end_game():
    global scoreboard
    c = 0
    c_max = len(scoreboard)
    string = ""
    while c < c_max:
        string = string + str(scoreboard[c][0]) + "," + str(scoreboard[c][1])
        if c < c_max -1:
            string = string + "/"
        c = c + 1
    print("\n\nFile Save Format = " + string)
    f = open("pointsDB.txt", "w")
    f.write(string)
    f.close()
    exit()


# START OF PROGRAM

loadmusic()
loadscoreboard()
current_user = input("\nWhat is your name? ('Quit' to Exit): ")
while current_user.lower() != "quit":
    pword = input("Password? : ")
    for login in users:
        if current_user.lower() == login[0].lower() and pword == login[1]:
            current_user = login[0]
            menu()
    else:
        print("\nInvalid User and/or Password\n")
        current_user = input("What is your name? ('Quit' to Exit): ")
exit()       