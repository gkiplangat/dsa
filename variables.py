def name():
    # Declare the global variables
    global name
    global fruits
    name = input("Enter your name: ")
    fruits = ['Apple', 'Banana', 'mango',['Carrots', 'Tomatoes']]

name()
print("Dear " +name+", Welcome to Riara University")

for i in name:
    print(i)

for fruit in fruits:
    print(fruit)
print(fruits[3][1])