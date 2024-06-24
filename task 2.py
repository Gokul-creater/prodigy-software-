import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!\n")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number within the range of 1 to 100.\n")
                continue
            
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("Too high! Try a lower number.\n")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly.")
                print(f"It took you {attempts} attempts.\n")
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

    print("Thank you for playing the Guessing Game!")

if __name__ == "__main__":
    guessing_game()
