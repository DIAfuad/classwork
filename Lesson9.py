from os import system
while True:
    print('----------------Main Menu--------------------')
    print("1. Beef Burger")
    print("2. Kacchi")
    print("3. Borhani")
    print("4. Ruti")
    print("Enter Your Selection: ",end="")
    choice=input()

    if choice == "1":
        print("Beef Burger")
    elif choice == "2":
        print("Kacchi")
    elif choice == "3":
        print('Borhani')
    elif choice == "4":
        print('Ruti')
        break

    else:
        print("Invalid Selection")                
input("Press Enter To Continue ....")
#cls=clear system
system('cls')





















































