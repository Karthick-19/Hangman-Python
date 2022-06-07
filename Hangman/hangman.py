from words import word#Generate a random word in word collection list
import random

def easymode():#Easy mode function
    s=random.choice(word)#Variable to generate random world
    turns=10#Predefined no of turns
    User_guess=''
    ValidW=set('abcdefghijklmnopqrstuvwxyz')#Valid Characters for guesses

    while len(s)>0:
        EW=''
        missed=0

        for letter in s:#letter RW generated by Compiler
            if letter in User_guess:#If user guess matches generated random word
                EW=EW+letter
            else:
                EW=EW+" _ "#generate _ 
        if EW==s:#If all letters are correctly guessed
            print(EW)
            print("You Saved him..!!")
            break 
        
        print('Guess the word: ',EW)
        guess=input()

        if guess in ValidW:
            User_guess=User_guess+guess
        else:
            print("Enter a valid character")
            guess=input()
        if guess not in s:
            turns-=1

            if turns==9:
                print("9 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
            
            if turns==8:
                print("8 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")

            if turns==7:
                print("7 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("         |           ")

            if turns==6:
                print("6 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("         |           ")
                print("        /            ")

            if turns==5:
                print("5 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("         |           ")
                print("        / \           ")

            if turns==4:
                print("4 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("      +--|           ")
                print("        / \           ")

            if turns==3:
                print("3 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("      +--|--+           ")
                print("        / \           ")

            if turns==2:
                print("2 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("           |         ")
                print("         O           ")
                print("      +--|--+           ")
                print("        / \           ")

            if turns==1:
                print("Only 1 turn left Play carefully..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         |         ")
                print("         O           ")
                print("      +--|--+           ")
                print("        / \           ")       

            if turns==0:
                print("You let an innocent die..;((")
                break

def mediummode():
    s=random.choice(word)
    User_guess=''
    turns=7
    ValidW=set('abcdefghijklmnopqrstuvwxyz')

    while len(s)>0:
        MW=''
        missed=0

        for letter in s:
            if letter in User_guess:
                MW=MW+letter
            else:
                MW=MW+' _ '
        if MW==s:
            print(MW)
            print("You Saved him..!!")
            break

        print("Guess the Word ",MW)
        guess=input()

        if guess in ValidW:
            User_guess=User_guess+guess
        else:
            print("Enter a valid character")
            guess=input()

        if guess not in s:
            turns-=1

            if turns==6:
                print("6 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")

            if turns==5:
                print("5 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("         |           ")

            if turns==4:
                print("5 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("         |           ")
                print("        / \           ")

            if turns==3:
                print("3 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("      +--|--+           ")
                print("        / \           ")

            if turns==2:
                print("2 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("           |         ")
                print("         O           ")
                print("      +--|--+           ")
                print("        / \           ")

            if turns==1:
                print("Only 1 turn left Play carefully..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         |         ")
                print("         O           ")
                print("      +--|--+           ")
                print("        / \           ") 

            if turns==0:
                print("You let an innocent die..;((")
                break

def hardmode():
    s=random.choice(word)
    User_guess=''
    turns=4
    ValidW=set('abcdefghijklmnopqrstuvwxyz')

    while len(s)>0:
        MW=''
        missed=0

        for letter in s:
            if letter in User_guess:
                MW=MW+letter
            else:
                MW=MW+' _ '
        if MW==s:
            print(MW)
            print("You Saved him..!!")
            break

        print("Guess the Word ",MW)
        guess=input()

        if guess in ValidW:
            User_guess=User_guess+guess
        else:
            print("Enter a valid character")
            guess=input()

        if guess not in s:
            turns-=1

            if turns==3:
                print("3 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("         |           ")

            if turns==2:
                print("2 Turns left..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         O           ")
                print("         |           ")
                print("        / \           ")

            if turns==1:
                print("Only 1 turn left Play carefully..!!")
                print("_ _ _ _ _ _ _ _ _ _ ")
                print("         |         ")
                print("         O           ")
                print("      +--|--+           ")
                print("        / \           ")

            if turns==0:
                print("You let an innocent die..;((")
                break

name=input("Enter your name: ")
print(f"Welcome to Hangman {name}\nEnjoy playing..")
level=input("Select Difficulty level:\nEasy\nMedium\nHard\n").lower()
if level=="easy":
    easymode()
elif level=="medium":
    mediummode()
elif level=="hard":
    hardmode()
else:
    print("Enter proper input!!")
    
        
        
