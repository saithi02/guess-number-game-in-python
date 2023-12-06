import random
number = random.randint(1, 100)
def intro():
    player_name = input("Hello, what is your name? ")
    print('I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number between 1 and 100 then you will guess, alright? \nDon\'t forget! You have only 3 chances so guess:'.format(player_name))
def game():
    number_of_guesses = 0
    while number_of_guesses < 3:
        guess = int(input())
        if guess<=100 and guess>=1:
            number_of_guesses += 1
            if guess < number:
                print('Your estimate is too low, go up a little!')
            if guess > number:
                print('Your estimate is too high, go down a bit!')
            if guess == number:
                break
        if guess>100 or guess<1: #if they aren't in the range
            print("Silly Goose! That number isn't in the range!")
            print("Please enter a number between 1 and 200")

    if guess == number:
        print( 'Congratulations , you guessed the number in {} tries!'.format(number_of_guesses))
    else:
        print('Close  you couldn\'t guess the number. \nWell, the number was {}.'.format(number))
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    intro()
    game()
    print("Do you want to play again?")
    playagain=input()