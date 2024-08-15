import random

random_number = random.randint(0, 50)
guesses = 10

print("Welcome to this number guesser game!")
print("....................................")
print("Instructions📃 : Pick a number between 1-50.\nTry to guess the secret number before you run out of guesses.\nGood luck!")
print("....................................")
input("Press Enter to start!")

while guesses > 0:
    user_guess = input('Make a guess: ')
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('🚫Please type a number next time')
        continue

    if user_guess > 50:
        print('Please pick a number less than 50.')
        continue

    guesses -= 1

    if user_guess == random_number:
        print('You got it right!🎊')
        break
    elif user_guess > random_number:
        print('You were above the number.⬆️')
        print("You have",guesses,"guesses left")
        print("============================")
    else:
        print('You were below the number.⬇️')
        print("You have",guesses,"guesses left")
        print("============================")

    if guesses == 0:
        print("You ran out of guesses 0️⃣")
        print("Game Over 😔")
        break

if guesses > 0 and user_guess == random_number:
    print('You got it in', 10 - guesses, 'guesses.')
else:
    print('The number was', random_number)