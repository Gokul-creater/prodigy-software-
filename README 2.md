#TASK 2 
Here's a Python program that implements a simple guessing game. The program generates a random number between 1 and 100 (inclusive) and prompts the user to guess the number. It provides feedback if the guess is too high or too low and continues until the user correctly guesses the number. After the correct guess, it displays the number of attempts it took to win the game.

```python
import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts to win the game.")
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()
```

### Explanation:

1. **Imports**: 
   - `random` module is imported to generate random numbers.

2. **Function `guessing_game()`**:
   - Prints a welcome message and instructions for the game.
   - Generates a random number (`secret_number`) using `random.randint(1, 100)`.
   - Initializes `attempts` counter to track the number of guesses.

3. **Game Loop** (`while True`):
   - Prompts the user to input their guess.
   - Validates the input to ensure it's an integer between 1 and 100.
   - Compares the user's guess to `secret_number` and provides feedback:
     - "Too low!" if the guess is less than `secret_number`.
     - "Too high!" if the guess is greater than `secret_number`.
     - Congratulates the user and displays the number of attempts if the guess is correct.
   - Breaks out of the loop when the correct number is guessed.

4. **Input Handling**:
   - Uses `input()` to get user input and `int()` to convert it to an integer.
   - Handles exceptions (e.g., `ValueError`) for invalid inputs.

5. **Execution**:
   - `if __name__ == "__main__":` ensures that the `guessing_game()` function is executed when the script is run directly.

### Usage:

- Run the script (`python guessing_game.py`).
- Enter your guess when prompted.
- Continue guessing until you correctly guess the number.
- After winning, the program displays how many attempts it took.

This guessing game provides a fun and interactive way for users to practice guessing numbers within a specified range and includes input validation to ensure a smooth user experience.
