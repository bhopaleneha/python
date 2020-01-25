import random

secret_number=random.randint(1,20)
print("start of our compettition")

for i in range(1,4):
    print("start ur guessing")
    guess=int(input("enter the number u wish"))
    if guess<secret_number:
        print("the number is too less")
    elif guess>secret_number:
        print("the number is too large")
        break
    
if guess==secret_number:
        print("ohhh awesome")

else:
    print("better luck next time "+str(secret_number))
        
              
