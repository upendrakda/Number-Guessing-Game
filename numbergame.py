import random
def getnum(a,b):
    num = random.randint(a, b)
    return num

def check(n, x):
    if(x>n):
        print("It's less than",x)
    elif(x<n):
        print("It's greater than",x)

def playagain():
    c=int(input("\nEnter your choice:"))
    if(c==1):
        start()
    elif(c==2):
        exit()
    else:
        print("Invalid Choice!! Valid: 1 or 2")
        playagain()

def invalid():
    print("Invalid Choice! Enter between 1 to 4!!")
    play()


def start():
    print("\n--Number Guessing Game--")
    print("How to Play? Press zero(0).")
    print("\nChoose Level")
    print("1.Easy \n2.Medium \n3.Hard \n4.Extreme")
    play()

def play():
    choice=int(input("What's Your Choice! \nEnter number:"))
    if(choice == 0):
        print("\n** Welcome to the Number Guessing Game! **\n")
        print("Instructions:")
        print("a. Choose level and enter a number to guess the secret number.")
        print("b. The computer will tell you if your guess is too high, too low, or correct.")
        print("c. Keep guessing until you get it right.")
        print("d. Type 7777 anytime for a hint (shows number range).")
        print("e. Game Over when guessed correctly and will show how many attempts you took.")
        print("-------------------------------------------------------------------------------")
        print("1.Play Now \t2.Exit")
        playagain()
        



    elif(choice == 1):
        print("\nLevel: Easy")
        print("**For Hint: 7777")
        n= getnum(1,50)
        i=0
        while True:
            x= int(input("\nEnter your Guess:"))
            if(x==7777):
                print("It's a number between 1 to 50\n")

            elif(x==n):
                i+=1
                print("\nWell Done! You took",i,"attempts to guess this.")
                print("--------------------------------------------------")
                print("1.Play Again \t2.Exit")
                playagain()

            else:
                i+=1
                check(n, x)

    elif(choice==2):
        print("\nLevel: Medium")
        print("**For Hint: 7777")
        n= getnum(1,250)
        i=0
        while True:
            x= int(input("\nEnter your Guess:"))
            if(x==7777):
                print("It's a number between 1 to 250\n")

            elif(x==n):
                i+=1
                print("\nWell Done! You took",i,"attempts to guess this.")
                print("--------------------------------------------------")
                print("1.Play Again \t2.Exit")
                playagain()

            else:
                i+=1
                check(n, x)

    elif(choice==3):
        print("\nLevel: Hard")
        print("**For Hint: 7777")
        n= getnum(1,800)
        i=0
        while True:
            x= int(input("\nEnter your Guess:"))
            if(x==7777):
                print("It's a number between 1 to 800\n")

            elif(x==n):
                i+=1
                print("\nWell Done! You took",i,"attempts to guess this.")
                print("--------------------------------------------------")
                print("1.Play Again \t2.Exit")
                playagain()

            else:
                i+=1
                check(n, x)

    elif(choice==4):
        print("\nLevel: Extreme")
        print("**For Hint: 7777")
        n= getnum(1,2000)
        i=0
        while True:
            x= int(input("\nEnter your Guess:"))
            if(x==7777):
                print("It's a number between 1 to 2000\n")

            elif(x==n):
                i+=1
                print("\nWell Done! You took",i,"attempts to guess this.")
                print("--------------------------------------------------")
                print("1.Play Again \t2.Exit")
                playagain()

            else:
                i+=1
                check(n, x)

    else:
        invalid()

start()