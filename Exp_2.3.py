# INTERACTIVE GUESSING GAME

import random

secret_no = random.randint(1, 10)

print("GUESS THE NUMBER\nYou will get 3 chances to choose a number between 1 to 10.\nIf your number matches with the secret number, you win!")
print()
i = 1
while i <= 3:
    n = int(input(f"Attempt {i}: Guess the number: "))

    if n < secret_no:
        print("Your guess is too low.TRY AGAIN.")

    elif n > secret_no:
        print("Your guess is too high.TRY AGAIN.")

    else:
        print("CONGRATULATION!!\nYour guess is correct.\n~YOU WIN~")
        break

    i += 1

else:
    print(f"Your 3 attempts are over. Your secret number was {secret_no}")