# INTERNAL/EXTERNAL DEPENDENCIES
import random
import time
from colored import fg, bg, attr
from termcolor import colored

background_color = bg("black") + fg("#0000ff")
text_color = bg("white") + fg("black")
text_style = attr("bold") 
result_color = bg("red") 
congs_color = bg("yellow")
comp_congs_color = bg("red")
cont_color = bg("White")
print(f"{background_color }{text_style}ROCK-PAPER-SCISSORS-GAME-PP3")
# GAME DESIGN PROCESSURE:

# 1. Tell the user to chose R for Rock, or P for Paper or S for Scissors
# 2. Get the user's Input
# 3. Convert the users Input into capital letter (R, P and S)
# 4. Validate Inputs from the users and print an error if Invalid (Invalid are all choices different from R, P and S)
# 5. Computer's choice ( this will be a random choice from the R, P, S)
# 6. Compare the choice of the user and of the computer
# 7. print the choices
# 8. Determine the winner round by comparring the choices according the Games Rules
# 9. ask the user if they want to continue playing
# 10. if NOT, terminate the Game, other wise continue
# 11. Declare the ultimate winner (who won 7 rounds first)



# GLOBAL VALUABLES

RPS_ASCII_Art = { 'R' : """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", 'P': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", 'S':"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""  }


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
# from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe


# PLAYING THE GAME STARTS HERE:

print("🪨 📄 ✂️ "*7)
print("-"*50)
print(f"Hello, and Welcome to the ROCK, PAPER, SCISSORS Game!\nThis Game is between YOU and the COMPUTER......Who gonna winn??? Let's start and I wish you both all the best!\nHere we go...1, 2, 3,...Ready? Go...\n")
print(f"Here is the reminder about the Abbreviations:\n R stands for Rock \n P stands for Paper and\n S stands for Scissors")
print()
print(f"Rules of the Game: ")
print(f"Players deliver hand signals representing rock, paper, or scissors, with the outcome determined by these three rules: ")
print(f" 1. Rock wins against scissors.\n 2. Scissors win against paper.\n 3. Paper wins against rock.") # from  https://wrpsa.com/the-official-rules-of-rock-paper-scissors/
print()
print("THE FIRST TO WIN 7 ROUNDS, WINNS!!")
print("-"*50)
print("🪨 📄 ✂️ "*7)
print()
POSSIBLE_CHOICES = ('R', 'P', 'S')
computer_score = 0
user_score = 0
rounds_count = 0

while True:
   
    rounds_count += 1
    print()
    print(f"ROUND NUMBER: {rounds_count}")
    
    # 1. Tell the user to chose R for Rock, or P for Paper or S for Scissors
    # 2. Get the user's Input
    # 3. Convert the users Input into capital letters (R, P and S)
    user_choice = input("Enter your choice. Type R or P or S:--- \n").upper()
    

    # 4. Validate Inputs from the users and print an error if Invalid 
    # Invalid choices are different from R, P and S
    if user_choice not in POSSIBLE_CHOICES:
        print(f"Please try again. Possible choices are {POSSIBLE_CHOICES}")
        continue
    else:
        if user_choice == 'R':
            print(f"You chose {user_choice} for the ROCK 🪨:{rock}")
        elif user_choice == 'P':
            print(f"You chose {user_choice} for the PAPER 📄:{paper}")
        elif user_choice == 'S':
            print(f"You chose {user_choice} for the SCISSORS ✂️:{scissors}")

    # 5. COMPUTER'S CHOICES
    computer_choice = random.choice(POSSIBLE_CHOICES)
    print(f"Your Opponent, the computer, chose {computer_choice} {RPS_ASCII_Art[computer_choice]}")    

    # 6. compare the choice of the user and of the computer and
    # 8. Determine the winner, comparring the choices according the Games Rules
    def who_is_the_winner():
        if user_choice == computer_choice:
            return "It's a DRAW 😂😂😂 Let's do it again ", None \

        elif (
            (user_choice == 'R' and computer_choice == 'S') or
            (user_choice == 'S' and computer_choice == 'P') or
            (user_choice == 'P' and computer_choice == 'R')):
            return "You won this round 🎉🎉🎉", "user"
           
        else:
            return "Sorry, you lost this one 😢😢😢", "computer"\
            

    winner_is, winner = who_is_the_winner()
    print(f"{winner_is}")

    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

    # Check if either player has 7 out of total rounds
    if user_score == 7: 
        print("------------------------------------------------")
        print("------------------------------------------------")
        print(f"{congs_color}GAME OVER!!!...\nCongratulations! You are the overall winner! with {user_score} won rounds! 🎉🎉🎉💃🕺💃🕺👯") 
        break 
    elif computer_score == 7: 
        print(f"{comp_congs_color}GAME OVER!! \nThe computer is the overall winner in the last {rounds_count} combined rounds with {computer_score} won rounds! Better luck next time! 😢") 
        break
    # 9. ask the user if they want to continue playing    
    wanna_try_again = input("Do you wanna try again ? Type any thing but n to continue or n to end the game: \n").upper()
    if wanna_try_again == 'N':
        print(f"{cont_color}OK, No worries, Tschüss for now, was nice playing with you 👋 Please come back at any time!")
        break
print("------------------------------------------------"*2)
print(f"{result_color}Final Results: \nYou won: {user_score} out of {rounds_count} rounds  and \nComputer won: {computer_score} out of {rounds_count} rounds")




