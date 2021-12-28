import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9")
while chances < 5 :
    guess = int(input("Enter your Guess"))
    if guess == number:
        print("You Won!")
        break
    elif guess < number:
        print("Your Guess is low. Try guessing a higher number.")
    else:
        print("Your Guess is high. Try guessing a lower number.")
    chances+=1
if not chances<5:
    print("You Lose, The number is",number)