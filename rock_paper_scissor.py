import random
computer=random.choice([-1,0,1])
youstr=input("Enter your choice:")
youDict={"r":-1,"p":0,"s":1}
reverseDict={-1:"Rock",0:"Paper",1:"Scissor"}
you=youDict[youstr]
print(f"Your choice is {reverseDict[you]}\nComputer's choice is {reverseDict[computer]}")

if(computer==you):
    print("It's a draw!") 
else:
    if((computer==-1 and you==0) or (computer==0 and you==1) or (computer==1 and you==-1)):
        print("You Win!")
    elif((computer==-1 and you==1) or (computer==0 and you==-1) or (computer==1 and you==0)):
        print("You Lose!")  
    else:
        print("Something is wrong")
    