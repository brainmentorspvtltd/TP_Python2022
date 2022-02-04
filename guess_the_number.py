# mini game - guess the number game
import random

cpu = random.randint(1,100)
counter = 5
game = True
while game:
    user = int(input("Enter your guess : "))

    if cpu == user:
        print("Congrats, You have guess the number...")
        game = False
        break
    elif cpu > user:
        print("You have guessed a smaller number...")
    elif cpu < user:
        print("You have guessed a larger number...")
    counter -= 1
    print("Chances Left :",counter)
    if counter == 0:
        print("Game Over...You Lost...Number was",cpu)
        game = False
