from ast import Expression
import random
from tkinter import *
def endlessplay():
    
    score=0
    userinput=input("Choose your move (1 for stone , 2 for scissor, 3 for paper)  - ")

    while(userinput != "quit"):
        try:
            userinput = int(userinput)
            # Taking Input from user

            lists=[1,2,3]
            compinput= random.choice(lists)

            if(userinput == compinput):
                print("Draw")
                score = score
                print("Your score is",score)
                userinput=input("Choose your move (1 for stone , 2 for scissor, 3 for paper)  - ")
                compinput= random.choice(lists)



            if({userinput == 1 and compinput==2} or {userinput == 2 and compinput==3} or {userinput == 3 and compinput==1}):
                print("You win")
                score+=1
                print("Your score is",score)
                userinput=input("Choose your move (1 for stone , 2 for scissor, 3 for paper)  - ")
                compinput= random.choice(lists)


                
            if({userinput == 1 and compinput==3} or {userinput == 2 and compinput==1} or {userinput == 3 and compinput==2}):
                print("You lose")
                score-=1
                print("Your score is",score)
                userinput=input("Choose your move (1 for stone , 2 for scissor, 3 for paper)  - ")
                compinput= random.choice(lists)
            else:
                print("pls enter a valid input")
                userinput=input("Choose your move (1 for stone , 2 for scissor, 3 for paper)  - ")
                compinput= random.choice(lists)


                
        except:
            print("pls enter a valid input")
            userinput=input("Choose your move (1 for stone , 2 for scissor, 3 for paper)  - ")
            compinput= random.choice(lists)

def competetive():
    chances=0
    score=0
    permascore=0
    while(chances <= 10):
        userinput=input("Choose your move (1 for stone , 2 for scissor, 3 for paper)  - ")
        try:
            userinput = int(userinput)
            # Taking Input from user

            lists=[1,2,3]
            compinput= random.choice(lists)

            if(int(userinput) == int(compinput)):
                print("Draw")
                score = score
                print("Your score is",score)
                print(f"Your score out of 10 is {permascore}")
                chances+=1

                
                compinput= random.choice(lists)


            elif(userinput == 1 and compinput==2 ):
                print("You win")
                score+=1
                permascore+=1

                print("Your score is",score)
                print(f"Your score out of 10 is {permascore}")
                chances+=1

                compinput= random.choice(lists)
            elif(userinput == 2 and compinput==3):
                print("You win")
                score+=1
                print("Your score is",score)
                print(f"Your score out of 10 is {permascore}")
                chances+=1
                permascore+=1

                compinput= random.choice(lists)
            elif(userinput == 3 and compinput==1):
                print("You win")
                score+=1
                print("Your score is",score)
                chances+=1
                permascore+=1

                compinput= random.choice(lists)

                
            elif(userinput == 1 and compinput==3):
                print("You lose")
                score-=1
                print("Your score is",score)
                print(f"Your score out of 10 is {permascore}")
                chances+=1

                userinput=input("Choose your move (1 for stone , 2 for scissor, 3 for paper)  - ")
                compinput= random.choice(lists)
            elif(userinput == 2 and compinput==1):
                print("You lose")
                score-=1
                print(f"Your score out of 10 is {permascore}")
                chances+=1
            elif(userinput == 3 and compinput==2):
                print("You lose")
                score-=1
                print("Your score is",score)
                print(f"Your score out of 10 is {permascore}")
                chances+=1


                
        except:

            print("pls enter a valid input")
            compinput= random.choice(lists)
        print("Game Summary")
    print(f"Your score out of 10 is {score}")




main_root = Tk()
main_root.title("Stone Paper Scissor")
main_root.geometry("777x402")

Label(main_root,text="Stone Paper Scissor",font="lucida 18 bold").grid(ipadx=200)

whichmodestore=StringVar()
whichmodestore.set("")
whichmode = Label(main_root,text="Which mode do you want to play (endless or competetive) - ")
whichmode.grid(row=2,column=0)

Button(main_root,text="Endless",command=endlessplay).grid(row=2,column=1)
Button(main_root,text="Competetive",command=competetive).grid(row=2,column=2)



score=0

main_root.mainloop()