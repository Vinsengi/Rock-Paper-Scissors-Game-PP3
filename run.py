
rock_ASCII_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# the above valuable value has been borrowed from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

paper_ASCII_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
## the above valuable value has been borrowed from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

Scissors_ASCII_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# # the above valuable value has been borrowed from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe


print("------------------------------------------------")
print(f"Hello, Welcome to the ROCK, PAPER, SCISSORS Game!\nThis Game is between YOU and the COMPUTER......Who gonna winn??? Let's start and wish you both all the best!\nHere we go...")
print("------------------------------------------------")
#Game Procedures:

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

#1. Tell the user to chose between R for Rock, or P for Paper or S for Scissors
#One, two, three...go. Please make your choice:  Type R for Rock or P for Paper or S for Scissors....\n"
POSSIBLE_CHOICES = ('R', 'P', 'S')
user_choice = input("Enter your choice. Type R or P or S: ").upper()
if user_choice not in POSSIBLE_CHOICES:
    print(f"Please follow the instructions correctly. Possible choices are {POSSIBLE_CHOICES}")
else:
    if user_choice == 'R':
        print(f"You chose {user_choice} for the ROCK:{rock_ASCII_art}")
    elif user_choice == 'P':
        print(f"You chose {user_choice} for the PAPER:{paper_ASCII_art}")
    elif user_choice == 'S':
        print(f"You chose {user_choice} for the SCISSORS:{Scissors_ASCII_art}")
