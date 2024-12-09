#ROCK-PAPER-SCISSORS-GAME-PP3
#GAME DESIGN PROCESSURE:

#1. Tell the user to chose between R for Rock, or P for Paper or S for Scissors
#2. Get the user's Input
#3. Convert the users Input into capital letter (R, P and S)
#4. Validate Inputs from the users and print an error if Invalid (Invalid are all choices different from R, P and S)
#5. Let the computer make a choice( this will be a random choice from the R, P, S)
#6. compare the choice of the user and of the computer
#7. print the choices
#8. Determine the winner for the played round by comparring the choices according the Games Rules
#9. ask the user if they want to continue playing
#10. if NOT, terminate the Game, other wise continue
#11. After thrre rounds, declare the ultimate winner (who won twice in the 3 rounds)

#INTERNAL LIBRARIES
import random

#GLOBAL VALUABLES
RPS_ASCII_Art = {'R':"""
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
# the above valuable value has been borrowed from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
## the above valuable value has been borrowed from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# # the above valuable value has been borrowed from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe


# PLAYING THE GAME STARTS HERE:

print("------------------------------------------------")
print(f"Hello, Welcome to the ROCK, PAPER, SCISSORS Game!\nThis Game is between YOU and the COMPUTER......Who gonna winn??? Let's start and wish you both all the best!\nHere we go...1, 2, 3,...Ready? Go...\n")

print("------------------------------------------------")

POSSIBLE_CHOICES = ('R', 'P', 'S')

while True:
    #1. Tell the user to chose between R for Rock, or P for Paper or S for Scissors
    #2. Get the user's Input
    #3. Convert the users Input into capital letters (R, P and S)
    user_choice = input("Enter your choice. Type R or P or S: ").upper()

    #4. Validate Inputs from the users and print an error if Invalid (Invalid are all choices different from R, P and S)
    if user_choice not in POSSIBLE_CHOICES:
        print(f"Please follow the instructions correctly. Possible choices are {POSSIBLE_CHOICES}")
        continue
    else:
        if user_choice == 'R':
            print(f"You chose {user_choice} for the ROCK:{rock}")
        elif user_choice == 'P':
            print(f"You chose {user_choice} for the PAPER:{paper}")
        elif user_choice == 'S':
            print(f"You chose {user_choice} for the SCISSORS:{scissors}")

    #5. COMPUTER'S CHOICES
    computer_choice = random.choice(POSSIBLE_CHOICES)
    print(f"Your Opponent, the computer, chose {computer_choice} for {RPS_ASCII_Art[computer_choice]}")    

    #6. compare the choice of the user and of the computer and
    #8. Determine the winner for the played round by comparring the choices according the Games Rules
    #def who_is_the_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a DRAW 😂 Let's do it again ")
    elif (
        (user_choice == 'R' and computer_choice == 'S') or
        (user_choice == 'S' and computer_choice == 'P') or
        (user_choice == 'P' and computer_choice == 'R')):
        print("You won 🎉🎉🎉")
    else:
        print("Sorry, you lost this one 😢")

    #9. ask the user if they want to continue playing    
    wanna_try_again = input("Do you wanna try again? Type y or n : ").upper()
    if wanna_try_again == 'N':
        print("OK, No worries, Tschüss for now, was nice playing with you 👋 Please come back at any time!")
        break
#winner_is = who_is_the_winner()
#print(f"And the WINNER IS {winner_is} 🎉🎉🎉✂️")



