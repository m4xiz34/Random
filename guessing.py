import random
playing = True
number = random.randint(1,20)

while playing:
    print("Guess a number between 1 and 20 to see if you get it right! (guessing game):")
    guess = int(input("Answer: "))
    
    if number == guess:
        print("CONGRATULATIONS! You're correct! The answer IS", number)
        break
    else:
        print("That doesn't seem right... Try again!")
