a=input("Do you want to play? ").lower()
if(a!="yes"):
    quit()
else:
    print("let's play")
    score=0
answer=input("what is the full form of CN ? ").lower()
if(answer=="computer network"):
    print("correct answer")
    score=score+1
else:
    print("Sorry")
    score=score-1
answer=input("what is the full form of WWW ? ").lower()
if(answer=="world wide web"):
    print("correct answer")
    score=score+1
else:
    print("Sorry")
    score=score-1    
answer=input("what is the full form of RAM ? ").lower()
if(answer=="random acess memory"):
    print("correct answer")
    score=score+1
else:
    print("Sorry")
    score=score-1
answer=input("what is the full form of GOAT ? ").lower()
if(answer=="greatest of all time"):
    print("correct answer")
    score=score+1
else:
    print("Sorry")
    score=score-1    
answer=input("what is the full form of ROM ? ").lower()
if(answer=="read only memory"):
    print("correct answer")
    score=score+1
else:
    print("Sorry")
    score=score-1
answer=input("what is the full form of ANFA ? ").lower()
if(answer=="all nepalese football association"):
    print("correct answer")
    score=score+1
else:
    print("Sorry")
    score=score-1    
print(f"YOU scored {score}/6 ")    