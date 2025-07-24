import random

mylist = ["rock", "paper", "scissors"]
computer_choice = random.choice(mylist)

user_answer = input("rock, paper, or scissors? ").lower()

print(f"Computer chose: {computer_choice}")
print(f"You chose: {user_answer}")

if user_answer == computer_choice:
    print("It is a tie!")
elif (user_answer == "rock" and computer_choice == "scissors") or \
     (user_answer == "scissors" and computer_choice == "paper") or \
     (user_answer == "paper" and computer_choice == "rock"):
    print("You win!")
elif user_answer in mylist:
    print("Computer wins!")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
