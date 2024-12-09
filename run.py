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
import time

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
print(f"Hello, and Welcome to the ROCK, PAPER, SCISSORS Game!\nThis Game is between YOU and the COMPUTER......Who gonna winn??? Let's start and I wish you both all the best!\nHere we go...1, 2, 3,...Ready? Go...\n")
print(f"Here is the reminder about the Abbreviations:\n R stands for Rock \n P stands for Paper and\n S stands for Scissors")
print()
print(f"Rules of the Game: ")
print(f"Players deliver hand signals representing rock, paper, or scissors, with the outcome determined by these three rules: ")
print(f" 1. Rock wins against scissors.\n 2. Scissors win against paper.\n 3. Paper wins against rock.") # from  https://wrpsa.com/the-official-rules-of-rock-paper-scissors/

print("------------------------------------------------")

POSSIBLE_CHOICES = ('R', 'P', 'S')
# allocated_time = 60
# startTime = time.time()
# game_over = False

# while game_over == False:
#     #game code


    
#     time.sleep(1)

    
#     time_gone = time.time() - startTime
#     if time_gone >= allocated_time:
#         game_over = True

# print("Schneller bitte!!")
computer_score = 0
user_score = 0
rounds_count = 0

while True:
    rounds_count +=1
    print(f"Round Number: {rounds_count}")
    
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
            print(f"You chose {user_choice} for the ROCK 🪨:{rock}")
        elif user_choice == 'P':
            print(f"You chose {user_choice} for the PAPER 📄:{paper}")
        elif user_choice == 'S':
            print(f"You chose {user_choice} for the SCISSORS ✂️:{scissors}")

    #5. COMPUTER'S CHOICES
    computer_choice = random.choice(POSSIBLE_CHOICES)
    print(f"Your Opponent, the computer, chose {computer_choice} {RPS_ASCII_Art[computer_choice]}")    

    #6. compare the choice of the user and of the computer and
    #8. Determine the winner for the played round by comparring the choices according the Games Rules
    def who_is_the_winner():
        if user_choice == computer_choice:
            return "It's a DRAW 😂😂😂 Let's do it again ", None \

        elif (
            (user_choice == 'R' and computer_choice == 'S') or
            (user_choice == 'S' and computer_choice == 'P') or
            (user_choice == 'P' and computer_choice == 'R')):
            return "You won this round 🎉🎉🎉💃🕺", "user"
           
        else:
            return "Sorry, you lost this one 😢😢😢", "computer"\
            

    winner_is, winner = who_is_the_winner()
    print(f"{winner_is}")

    if winner == "user":
        user_score +=1
    elif winner == "computer":
        computer_score +=1
    
    
    
    # Check if either player has won two out of three rounds 
    if user_score == 7: 
        print("------------------------------------------------")
        print("------------------------------------------------")
        print(f"GAME OVER!!!...\nCongratulations! You are the overall winner! with {user_score} won rounds! 🎉🎉🎉") 
        break 
    elif computer_score == 7: 
        print(f"GAME OVER!! \nThe computer is the overall winner in the last {rounds_count} combined rounds with {computer_score} won rounds! Better luck next time! 😢") 
        break
    #9. ask the user if they want to continue playing    
    wanna_try_again = input("Do you wanna try again ? Type any thing but n to continue or n to end the game: ").upper()
    if wanna_try_again == 'N':
        print("OK, No worries, Tschüss for now, was nice playing with you 👋 Please come back at any time!")
        break
print("------------------------------------------------")
print(f"Final Results: \nYou won: {user_score} out of {rounds_count} rounds  and \nComputer won: {computer_score} out of {rounds_count} rounds")




