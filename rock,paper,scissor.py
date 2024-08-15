'''
1 for ROCK
-1 for PAPER
0 for SCISSOR
'''

# INTRODUCTION AND WELCOME OF THE USER
print("WELCOME TO ROCK, PAPER, SCISSOR GAME.")
username = input("ENTER YOUR NAME TO BEGIN: ")
print(f"HELLO {username}, welcome to the game.")

# RULES AND INSTRUCTIONS
print(f"Hey {username}, do you know the rules of the game? Y for Yes and N for No.")
yes_or_no = input("PLEASE ENTER YOUR INPUT (do you know the rules of the game?): ").upper()
yesornoinput = {"Y": 2, "N": 3}

if yes_or_no == "N":
    print("https://wrpsa.com/the-official-rules-of-rock-paper-scissors/")
elif yes_or_no == "Y":
    print(f"Alright then {username}, let's begin the game.")
else:
    print("Invalid input!\nPlease restart the game and enter 'Y' or 'N'.")
    exit()


# THE GAME
print("TO PLAY ROCK TYPE \"R\" \nTO PLAY PAPER TYPE \"P\" \nTO PLAY SCISSOR TYPE \"S\"")
print(f"THE GAME BEGINS, ALL THE BEST {username}")

import random

def the_game():
    while True:
        bot = random.choice([-1, 0, 1])
        user = input("Enter your choice: ").upper()
        userDict = {"R": 1, "P": -1, "S": 0}
        reverseDict = {1: "Rock", -1: "Paper", 0: "Scissor"}
        usernum = userDict.get(user, None)

        if usernum is None:
            print("Invalid choice! Please choose R, P, or S.")
            continue
        else:
            print(f"Your input: {reverseDict[usernum]},\nComputer chose: {reverseDict[bot]}")
            if bot == usernum:
                print("TIE")
            elif (bot == 1 and usernum == -1) or (bot == -1 and usernum == 0) or (bot == 0 and usernum == 1):
                print("You WIN!!")
            else:
                if (bot == 1 and usernum == 0) or (bot == -1 and usernum == 1) or (bot == 0 and usernum == -1):
                    print("You LOSE.")
                else:
                    print("SOMETHING WENT WRONG!!!")

        print("DO YOU WISH TO PLAY AGAIN? YES / NO")
        yes_or_no2 = input("PLEASE MAKE A CHOICE. Y for YES, N for NO: ").upper()
        if yes_or_no2 == "N":
            print("THANK YOU. HAVE A NICE DAY!")
            break
        elif yes_or_no2 == "Y":
            print(f"Alright then {username}, all the best.")
        else:
            print("Invalid input! Exiting the game.")
            break

the_game()
