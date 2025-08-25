# Guess game : Guess the number in how many attempts?
import random

def Guess():
    number = random.randint(1, 10)
    count = 0  

    validation = input("Are you interested to play Guess game?? (Answer 'yes'): ").lower()
    if validation == 'yes':
        while True:
            guess = int(input("Guess a number between 1 and 10: "))
            count += 1  # increase attempts each guess

            if guess < number:
                print("Guess higher! 🔼")
            elif guess > number:
                print("Guess lower! 🔽")
            else:
                print(f"🎉 Congratulations! You guessed it in {count} attempts.")
                break   
    else:
        print("Thank you for visiting the game! 🙏")

Guess()
