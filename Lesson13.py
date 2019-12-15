from os import system

students = [
    {'Id':1, 'Name': 'Chand','Marks':123.99},
    {'Id':2, 'Name': 'Nazmul','Marks':12.99},
    {'Id':3, 'Name': 'Munaz','Marks':23.99},
     {'Id':4, 'Name': 'Alvy','Marks':90.99},
    {'Id':5, 'Name': 'Zahid','Marks':34.20},
    {'Id':6, 'Name': 'Munna','Marks':24.10}
    ]
system('dir')
#system('tree')
#system('cls')
print("%-5s %-30s %-20s" % ("Id","Students Name","Marks"))
print("="* 50)
for std in students:
    #print("{} {} {}".format(std['Id'],std['Name'],std['Marks'])) instead of
    print("%-5s %-30s %-20s" % (std['Id'],std['Name'],std['Marks']))


































