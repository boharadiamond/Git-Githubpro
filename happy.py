import random

print("🎉 Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 10: ")
    attempts += 1

    if not guess.isdigit():
        print("⛔ Please enter a valid number!")
        continue

    guess = int(guess)

    if guess == secret_number:
        print(f"✅ Correct! You guessed it in {attempts} tries. 🎉")
        break
    elif guess < secret_number:
        print("📉 Too low. Try again.")
    else:
        print("📈 Too high. Try again.")
