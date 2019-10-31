"""
if test expression:
    statement(s)   
else:
    statement(s)
"""
#decision making program/command
players = ['torun','Sourav','Ashik','Rakib','Pritom']

for name in players:
    if name=='Sourav':
        print(name.upper())
    else:
        print(name.lower())    
age = 22
if age >=18:
   print("You are old enough to vote!") 
else:
    print("Sorry,you are too young to vote!")

#elif is for multiple decision making programs/commands
#m=1
m= int(input('Enter Month [1-3] : '))
if m==1:                            #== is for comparision
    print('January')
elif m==2:
    print('February')
elif m==3:
    print('March')
else:
    print('Invalid Month')













