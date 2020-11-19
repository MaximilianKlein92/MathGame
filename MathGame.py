# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:31:45 2020

@author: Maximus

"""
print("""This is a mathimatical game where you get a random mathimatical 
question and earn points for correctly answering them. 
Your score will be stored. You can earn more points later on 
by answering arythmetic questions.
Have Fun!
""")

import random as rd
import os

Username = input ("Give me your name: ")

# This function will give you the scores of your previous games or 
# set a new score for you

def UserSearch (Username):
    #Read the File than splits each line using the split() funktion 
        global newUser
        
        try: 
            f = open("UserScores.txt", "r")

            for line in f:
                seperate = line.split(",")
               
                # If the first Item in the line is the username it returns it together with the score
                if seperate[0] == Username:
                    f.close()
                    newUser = False
                    return seperate

            
            print("You are new here,", Username)
            f.close()
            score = 0
            New = [Username, score]
            newUser = True
            return New
        
        # if there is no file UserScores it creates it
        except FileNotFoundError:
            print ("Welcome to your first round,", Username)
            f = open("UserScores.txt", "w")
            f.close()
            score = 0
            New = [Username, score]
            newUser = True
            return New

score = int((UserSearch(Username)[1])) 
print ("Your score is: %s" %(score))

# defining list of variables wich can be operated with
operandList = [1, 2, 3, 4, 5]
operaterList = ["","","",""]
operatorDict={1:"+", 2:"-", 3:"*", 4:"**"}

# Replaces numbers in the operant List with random numbers ranging from 1-9
def NumberGen ():
    for i in range(len(operandList)):
        operandList[i] = rd.randint(1,9)

# Assines randomly operants to the operant List
def OperatorAssin():
    for i in range(len(operaterList)):
        if operaterList[i-1] == "**":
            operaterList[i] = operatorDict[rd.randint(1,3)]
        else:
            operaterList[i] = operatorDict[rd.randint(1,4)]

# Produces a matematical question and solves it. Returning the sesult plus 
# the question as a string
def Result ():
    NumberGen()
    OperatorAssin()
    global questionString
    questionString = ""
    
    for i in range (len(operandList)):
        if i < len(operandList)-1: 
            questionString  += str(operandList[i]) + operaterList[i]
        else:
            questionString  += str(operandList[i])

    # with the funcion eval() can a string be calculated
    result = eval(questionString)  
    return result

# This funktions uptated the score in an seperate file or creates it.
def updateUserPoints (newUser, Username, score):

    # Appends the new User with the associated score
    if newUser:
        f = open("UserScores.txt", "a")
        f.write("\n%s, %s" %(Username, score))
        f.close()


    # Opens the existing File, creates a temporary file to "update" the old one
    else:
        t = open("UserScores.tmp", "w")
        f = open("Userscores.txt", "r")

        #splits the lines. Looks when the Username appiers and changes the score in the Temp file
        for line in f:
            sep = line.split(",")

            if sep[0] == Username:
                t = open("UserScores.tmp", "a")
                t.write("%s, %s\n" %(Username, score))
                t.close()

            else:
                t = open("UserScores.tmp", "a")
                t.write(line)
                t.close() 

        # Replaces the .txt Version with the .tmp Version. Making the new score accessable. 
        t.close()
        f.close()
        os.remove("UserScores.txt")
        os.rename("UserScores.tmp", "UserScores.txt")




#This function handels the interaction of the player.
# By a correct answer the score is updated.
def Round ():
    
        result = (Result ())
        Question = questionString

        Right = False

        while Right == False:
            try:
                Question = Question.replace( "**", "^" )
                Answer = int(input("What is {} : ".format(Question)))

                if Answer == result:
                    print ("That´s right. Good Job!")
                    Right = True
                    global score
                    score += 1
                
                # This asks the user if he wants to get the right answer 
                else:
                    Cheat = input("This was NOT correct. Do you want to get the answer? (j/n):")
                    if Cheat == "j":
                        print ("The answer was:", result)
                        Right = True
                    elif Cheat == "n":
                        print("Thad's the spirit!")
                    else:
                        print("I don´t know what thad was so ....")
                        
         
            except ValueError:
                print ("Please check your answer!")
                
        updateUserPoints (newUser, Username, score)


Game = True

while Game == True:
    Round()
    print("Your score is :", score)
    Again = input("Would you like to play again ? (j/n) ")
    
    if Again == "n":
        print ("See you next time!")
        Game = False
        
    elif Again == "j":
        print("Greate! Here we go again.")

    else:
        print("This was not a valid input so I assume you want to continue.")
    
