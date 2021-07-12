import random

number = random.randint(1,9)
chances = 0


while chances < 5 :
    
    guess = input("Guess a number between 1-9 : ")
    if(guess < number):
        print("Your guess was lower then the number , guess again")
    elif(guess > number):
        print("Your guess was higher then the number , guess again")
    else :
        print("You won congratulations!!")
        break
    chances = chances + 1
    



if not chances < 5 :
    print("You lose !! Better luck next time . The number was " , number)

    