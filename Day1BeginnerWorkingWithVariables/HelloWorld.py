#LESSON 1 DAY 1 - PRINTING

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# LESSON 2 DAY 1 - DEBUGGING PRACTICE

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Obsevacion cuando se usa cillas dobles no sepuede usar para sobreescribir una oracion ejemplo
#print("She said: " hello "and then left.") --> este es un error comun
#La mejor opcion seria usar comillas sencillas '' ejemplo
print('She said: " hello "and then left.')

print("Hello Word!\nHello Word!")
print("Hello" + " Isai")

#LESSON 3 DAY 1 - INPUT FUNCTION
nombre = input()
cantidad_caracteres = len(nombre)
print(cantidad_caracteres)

#There are two variables, a and b
a = input()
b = input()

#Create a third variable to help switch the values
c = a
a = b 
b = c

print("a: " + a)
print("b: " + b)