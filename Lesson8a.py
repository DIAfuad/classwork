"""
init variable
while condition:
    Statements
      ...    
"""
#alternative of For loop
#while loop
i=1
while i<=5:
    print(i,end='\t')
    i = i+1
print("\n")
print(40*"_")
j=10
while j<=20:
    print(j,end="\t")
    j = j+1
print("\n")
print(50*"_")    
z=10
while z<=20:
    print(z,end="\t")
    z = z+2
print("\n")
print(50*"_")

f=20
while True: #infinity loop
    if f>=40:
        break #breaking infinity loop
    print(f,end="\t")
    f = f+1

#creating a menu
while True :   
    print("====== Main Menu ======")
    print("1. Add")
    print("2. List")
    print("3. Edit")
    print("4. Exit")
    print("Enter your selection : ",end="")

    choice = input()

    if choice =="1":
        print("Add New Record")
    elif choice == "2":
        print("List Record")    
    elif choice == "3":
        print("Edit Record")
    elif choice == "4":
        print("Exit from program")
        break
    else:
        print("Invalid Selection")




