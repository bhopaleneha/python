#progarm for calculator

def addition(num1,num2):
    add=num1+num2
    print(add)
def subtraction(num1,num2):
    sub=num1-num2
    print(sub)

def multiplication(num1,num2):
    mul=num1*num2
    print(mul)

def division(num1,num2):
    div=num1/num2
    print(div)




print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
print("5. exit")


while True:
    choice = int(input('enter ur choice : '))
    if (choice <= 4):
         print("enter two numbers on which u wish to perform the operation:")
         num1=int(input("enter the first number : "))
         num2= int(input("enter the second number : "))
         if choice == 1:
             addition(num1,num2)
         elif choice == 2:
             subtraction(num1,num2)
         elif choice == 3:
             multiplication(num1,num2)
         else :
             division(num1,num2)
    elif choice ==5:
        break
    else:
        print("wrong")
        
     
    
    
   
        
    
