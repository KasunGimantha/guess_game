import random
#welcoming to game
print(f'{'*'*10}Welcome to Guess the Number!{'*'*10}')

print('What number range you like to guess:')
a = int(input('from '))
b = int(input('to '))

print('Number is generating ✨')
print()
print('Your number is generated.😎')
print(f'The number is between {a} and {b}🙄')
print('Can you guess it?')
#generating random number
random_number = random.randint(a, b)

player_number = None

i = 0

while (random_number != player_number):

    player_number = int(input("Enter your Number.Try your luck!👉: "))

    if player_number < a or player_number > b:
        print("Your guess is out of the specified range. Please guess a number between the given range!")
    else:
        # Provide hints based on the guess
        if random_number < player_number:
            print("Your guess is high")
        elif random_number > player_number:
            print("Your guess is low")

    print('*'*10)
    i = i+1

else:
    print('You win! Congradualtions🎉🍾🙌😃')

print(f'It took you {i} guesses to guess the number')
