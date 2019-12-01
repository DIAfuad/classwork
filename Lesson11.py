from os import system
#def defines method
def Add(a,b):
    c= a+b
    print("Additional is {}".format(c))

def Sub(a,b):
    c= a-b
    print("Subtraction is {}".format(c))

def Multi(a,b):
    c=a*b
    print("Multiplication is {}".format(c))    

def Div(a,b):
    c=a/b
    print("Division is {}".format(c))



system('cls')
while True :
    print("--------------Main Menu--------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("Enter Your Selection : ",end="")
    choice = input()

    if choice=='1':
        x=int(input("Enter first value : "))
        y=int(input("Enter second value : "))
        Add(x,y)
    elif choice=='2':
        e=int(input("Enter 1st Value : "))
        f=int(input("Enter 2nd Value : "))
        Sub(e,f)
    elif choice=='3':
          e=int(input("Enter 1st Value : "))
          f=int(input("Enter 2nd Value : "))
          Multi(e,f)
    elif choice=='4':
          e=int(input("Enter 1st Value : "))
          f=int(input("Enter 2nd Value : "))
          Div(e,f)
    elif choice=='5':
        print("Exit from program")
        break
    else:
        print("Invalid Selection")

    input("Press Enter to continue....")
    system('cls')






















