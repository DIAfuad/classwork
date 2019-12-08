#CLASS means classification/ a group of methods are placed in CLASS

print('--------------------- Class -------------------------')

class Calculator:
   def Add(self,a,b):
    c= a+b
    print("Additional is {}".format(c))

   def Sub(self,a,b):
    c= a-b
    print("Subtraction is {}".format(c))

   def Multi(self,a,b):
    c=a*b
    print("Multiplication is {}".format(c))    

   def Div(self,a,b):
    c=a/b
    print("Division is {}".format(c))

c1 = Calculator()
c1.Add(10,3)





