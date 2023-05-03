import random
avail_Choice=["Rock","Paper","Scissor"]
while True:
    print("Welcome to Rock Paper Scissor Game:")
    YourWin=0
    ComputerWin=0
    for i in range(1,6):
        print("Round",i,"Begin:")
        print("Please Select any One of these Options:")
        print("1-Rock","2-Paper","3-Scissor",sep="\n")
        Your_Choice=int(input())
        if Your_Choice==1:
            print("You Selected: Rock")
            Your_choice="Rock"
        elif Your_Choice==2:
            print("You Selected: Paper")
            Your_Choice="Paper"
        elif Your_Choice==3:
            print("You Selected: Scissor")
            Your_Choice="Scissor"
        else:
            print("Invalid Choice")
            break
        Computer_Choice=random.choice(avail_Choice)
        print("Computer selected:",Computer_Choice)
        if Your_Choice==Computer_Choice:
            print("Oops! Match is Drawn , No point to Both User and Computer")
        elif (Your_Choice=="Paper" and Computer_Choice=="Rock") or (Your_Choice=="Rock" and Computer_Choice=="Scissor") or (Your_Choice=="Scissor" and Computer_Choice=="Paper"):
            YourWin+=1
            print("You won this Round")
        else:
            ComputerWin+=1
            print("Computer won this Round")
    if YourWin>ComputerWin:
        print("Hurray! You won the game.")
        print("The final Scores are:","Your Score:",YourWin,"Computer Score:",ComputerWin,sep=" ")
    elif ComputerWin>YourWin:
        print("Sorry! You lost the game,Computer Won.")
        print("The final Scores are:", "Your Score:", YourWin, "Computer Score:", ComputerWin, sep=" ")
    else:
        print("This Whole match is Drawn.")
        print("The final Scores are:", "Your Score:", YourWin, "Computer Score:", ComputerWin, sep=" ")
    User_Choice=input("DO YOU WANT TO PLAY AGAIN??(YES or No)\n IF NO THEN ENTER EXIT..")
    if User_Choice=="YES" or User_Choice=="yes" or User_Choice=="Yes" or User_Choice=="yES":
        continue
    else:
        break
