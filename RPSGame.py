import random
choices = ["rock" ,"paper" ,"scissors"]
user=input("enter rock,paper,scissors:").lower()
computer= random.choice(choices)
print("your choice:",user)
print("computer choice:",computer)
if user==computer:
    print("It's a TIE!")
elif (user=="rock" and computer =="scissors") or\
     (user=="scissors" and computer=="paper") or\
     (user=="paper" and computer=="rock"):
         print("YOU WIN!")
else:
    print("COMPUTER WIN!")
