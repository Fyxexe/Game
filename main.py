import random

random_number = random.randint(0, 100)

def game(random_number):
    while True:
        input_number = int(input('Input number: '))
        
        if random_number == input_number:
            print("Congratulations, you guessed correctly")
            break  
        elif random_number > input_number:
            print("No, I guessed a higher number")
        elif random_number < input_number:
            print("No, I guessed a lower number")

question_one = input("Are you ready to start the game? [y/n]")

if question_one == "y":
    print("I guessed a number, you need to guess")
    game(random_number)
elif question_one == "n":
    exit()
else:
    print("Invalid input")
