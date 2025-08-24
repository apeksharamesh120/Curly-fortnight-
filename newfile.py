import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")

# Generate random number between 1 and 50
secret_number = random.randint(1, 50)

# Number of attempts allowed
attempts = 7

for i in range(attempts):
    guess = int(input(f"Attempt {i+1}/{attempts} - Enter your guess: "))
    
    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print(f"😢 Sorry, you've used all attempts. The number was {secret_number}.")