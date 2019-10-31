magicians = ['olive','meem','sazid']
for magician in magicians:
    print(magician,end='\t')
print('\n')
for value in range(1,5):
    print(value)

numbers = list(range(1,7))#list means third bracket([]) after running the program
print(numbers)

x = list(range(1,10,3))#the last intiger in the bracket is called incriment which increases by the intiger after running the program
print(x)

digits = [11,2,3,4,25,7,18,90]
print("The minimum value is : {}".format(min(digits)))
print("The maximum value is : {}".format(max(digits)))
print("The sum of values are : {}".format(sum(digits)))

players = ['Torun','sourov','rakib','ashik','pritom']
print(players[0:2])
print(players[2:4])
print(players[-1])
print(players[2:])
print(players[:3])
print(players[:])

#copy to my_players
my_players = players[:]
print(my_players)
