name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input(
    "You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? (left/right) ").lower()

if answer == "left":
    answer = input(
        "You come to a river. You can walk around it or swim across. Type 'walk' to walk around and 'swim' to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator. You lose!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and you lost the game. You lose!")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? (cross/back) ").lower()

    if answer == "back":
        print("You go back and lose. You lose!")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ")

        if answer == "yes":
            print("You talk to the stranger, and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger, and they are offended. You lose!")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

elif answer == "look around":
    print("You look around and find a hidden path! You venture down the path and find a treasure chest. You WIN!")

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
