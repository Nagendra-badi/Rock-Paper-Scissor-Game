import random
user_choice = input("Choose rock, paper or scissor: ").lower()
computer_choice = random.choice(["rock",'paper',"scissor"])
print("Computer Choice is: ",computer_choice)

# Rocks beats Scissors -> Rock wins
# Paper beats Rock -> Paper wins
# SCissor beats Paper -> Scissor wins
# if both same -> Tie

if user_choice == computer_choice:
    print("It\' a Tie.")
elif user_choice == "rock":
    if computer_choice == "scissor":
        print("You win.")
    else:
        print("You lose!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win.")
    else:
        print("You lose!")
elif user_choice == "scissor":
    if computer_choice == "paper":
        print("You win.")
    else:
        print("You lose!")
else:
    print("invalid choice")