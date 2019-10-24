motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(motorcycles[0])
print(motorcycles[1])
print(motorcycles[2])

motorcycles[0] = 'hero'
print(motorcycles)

fruits =[]
fruits.append('Orange')
fruits.append('Mango')
fruits.append('Banana')

fruits.insert(1,'Apple')
print('After Sort :')
fruits.sort() 
print(fruits)

print('After Remove :')
fruits.remove('Apple')
print(fruits)

print('After Reverse :')
fruits.reverse()
print(fruits)
