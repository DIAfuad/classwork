#dictionary
#the names are called 'key' and the numbers are called 'value'
Dict = {'Ali':18,'Rahim':12,'Karim':22,'Joya':25}
print('All Item : ')
print(Dict)
print('Print by key Rahim : ')
print(Dict['Rahim'])

Boys={'Ali':18,'Rahim':12,'Karim':22}
Girls={'Joya':25,'Zakia':30,'Ela':11}

studentX=Boys.copy()
studentY=Girls.copy()

print('All Boys : ')
print(studentX)
print('All Girls : ')
print(studentY)

#We use the method Dict.update to 
print('add Sarah to our existing dictionary')
Dict.update({"Sarah":9})
print(Dict)
print('if exist update dictionary')
Dict.update({'Karim':12})
print(Dict)

print('Delete by Key : ')
del Dict['Ali']
print(Dict)

print(type(studentX))
print(dir(dict))
#Items-.items is a method
print('Print Items : ')
print("Students Name : %s" % Dict.items())
print('Convert dic to list : ')
print("Students Name: %s" % list(Dict.items()))

#loop
print('Print Only Keys : ')
for key in Dict.keys():
    print(key)
print('Print Only values')    
for val in Dict.values():
    print(val)
print('Print only Key and Value : ')
for key in Dict.keys():
    print(key + " - " + str(Dict[key]))

#sorting means putting in alphabetic order

Students = list(Dict.keys())
Students.sort()
print("SORTED KEYS : " + str(Students))

print("Key and Value")
for S in Students:
    print( S + " - " + str(Dict[S]))





