# program to be random quiz on music

import random

users = [["Admin", "Password"], ["Josh", "Letmein"], ["Will", "TeachMe"]]
musiclist = []
scoreboard = []
limit = 0

# FUNCTION DEFINITION

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

# The Actual Quiz
def quiz():
    global musiclist
    global limit
    play = "y"
    while play.lower() != "n":
        quiz_no = random.randint(0, limit - 1)
        letters = gen_question(quiz_no)
        letter_no = len(letters)
        question = "\nWhat song by " + musiclist[quiz_no][1] + " starts with the letter"
        if letter_no > 1:
            question = question + "s " 
            c = 0
            while c < letter_no:
                if c < (letter_no - 1):
                    question = question + str(letters[c]) + ", "
                elif c == letter_no - 1:
                    question = question +  "and " + str(letters[c]) + "?"
                c = c + 1
        else:
            question  = question +  " " + str(letters[0]) + "?"
        print(question)
        print ("HINT: (Answer is '"+ musiclist[quiz_no][0] + ")")
        answer = input("Answer : ")
        play = input("Do you want to go again? (Y/N) : ")
    exit()

# Breaks the Answer down into Letters
def gen_question(quiz_no):
    global musiclist
    question = []
    word_split = musiclist[quiz_no][0].split(" ")
    word_limit = len(word_split)
    c = 0
    while c < word_limit:
         first_letter = list(word_split[c])
         question.append(first_letter[0])
         c = c + 1
    return question

    # START OF PROGRAM

loadmusic()
current_user = input("\nWhat is your name? ('Quit' to Exit): ")
while current_user.lower() != "quit":
    pword = input("Password? : ")
    for login in users:
        if current_user.lower() == login[0].lower() and pword == login[1]:
            quiz()
    else:
        print("\nInvalid User and/or Password\n")
        current_user = input("What is your name? ('Quit' to Exit): ")
exit()     