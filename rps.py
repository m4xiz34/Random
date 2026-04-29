import random

options = ["Rock", "Paper", "Sissors"]

user_choice = input("Choose! Rock, Paper, or sissors? (Capital Letter must be added at the start in order for it to work): ")
computer_choice = random.choice(options)

print(user_choice)
print(computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
    
elif user_choice == ("Rock") and computer_choice == ("Sissors"):
    print("Rock smashes sissors. You win!")

elif user_choice == ("Sissors") and computer_choice == ("Paper"):
    print("You can cut through the paper. You win!")

elif user_choice == ("Paper") and computer_choice == ("Rock"):
    print("Paper wraps around Rock. You win!")
    
else:
    print("You lose... Better luck next time!")
