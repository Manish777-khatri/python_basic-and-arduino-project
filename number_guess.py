import random
c=int(input("Enter the range of number: "))
champain=random.randint(1,c)
guess=int(input("Guess the number:"))
count=1
while guess !=champain:
    if guess<champain:
        print("guess higher")
        guess=int(input("Guess the number:"))
        count+=1   
    else:
        print("guess lower")
        guess=int(input("Guess the number:"))
        count+=1    
print("congrautlations !!")
print(count)