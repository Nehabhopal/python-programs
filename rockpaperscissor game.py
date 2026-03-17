"""import gtts
import playsound
text = input("enter something here:")
sound = gtts.gTTS(text, lang="en")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")"""

import random

print("-----------welcome to RPS--------")

user_score = 0
comp_score = 0
ties = 0

name = input("enter your name:")
print(""" 
Winning Rules:
1.Paper vs Rock --> Paper
2.Rock vs scissors --> Rock
3.Scissors vs paper ---> scissors""")
print()
while True:
    print(""" Choices are:
        1.Rock
        2.Paper
        3.Scissors""")
    choice = int(input("enter a choice from 1-3:"))
    print()
    while choice > 3 or choice < 1:
        choice = int(input("enter a vaild input"))

    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "scissors"

    print("The user's choice is",user_choice)
    print("Now it is Computer's turn")

    computer = random.randint(1,3)

    if computer==1:
        comp_choice = "Rock"
    elif computer==2:
        comp_choice = "Paper"
    else:
        comp_choice = "scissors"

    print("The computer choice is",comp_choice)

    if((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("paper wins")
        result = "paper"
    elif((user_choice == "scissors" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "scissors")):
        print("Rock wins")
        result = "Rock"
    elif(user_choice==comp_choice):
        print("it's a tie")
        result = "Tie"
    else:
        print("scissors wins")
        result = "scissors"

    if result == "Tie":
        ties += 1
    elif result == user_choice:
        print("user wins")
        user_score += 1
    else:
        print("computer wins")
        comp_score += 1

    print("scores are")
    print(name,"score is",user_score)
    print("computer's score is",comp_score)
    print("ties are",ties)

    repeat = ("do you want to play again:",repeat)
    if repeat == "No":
        break

print("Game over!")
print("Thanks for playing!!!")