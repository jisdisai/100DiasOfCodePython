# Esto es un comentario
if 3 > 5:
    print("esto no se va a imprimir ")
# es otra funcion
if 5 > 3:
    print("5 es mayor que 3 ")


# Variables
x = 5
y = "Chanchito Feliz"
print(x, y)

correo = "salgadoisai64@gmail.com"
print(correo)

_mi_var = "soy feliz"
MIVAR = "probando"  # cuando todo es mayuscula normalmente se usa para variables que cuyo valor no cambia
a, b, c = "mrrobot", "anonymous", "day-cero"  # Multiple variables
valor1 = valor2 = valor3 = "Batman"


# Concatenacion
inicio = "Hola"
final = "mundo"
print(inicio + final)
print(inicio, final)

# String
palabra = "Hola mundo"
oracion = "Hola mundo"

# Numeros
enteros = 28  # integer
decimales = 20.2  # float
complejo = 1j  # imaginario
print(palabra, oracion, enteros, decimales, complejo)

# Listas
lista = [11, 2, 3]
lista2 = lista.copy()
lista.append(4)
# lista.clear()
print(lista2)
print(lista.count(3))
print(len(lista), len(lista2))

largoLista = len(lista)
largoLista2 = len(lista2)

print(largoLista, largoLista2)

lista = ["Hola", "Mundo", "loco que soy"]
# print(lista[0])
# lista.pop()
# print(lista)
# lista.remove("Mundo")
lista.reverse()
lista.sort()
print(lista)
tupla = ("hola", "Mundo", "usando", "tupla")
listaDeTupla = list(tupla)
listaDeTupla.append("chiquitita")
print(listaDeTupla)
# print(tupla.index("tupla"))

rango = range(6)
print(rango)

diccionario = {"nombre": "Faby", "genero": "F", "edad": 30}

print(diccionario)
# Acceder a un valordel  diccionario
print(diccionario["nombre"])
# ser mas implicito y acceder a un metodo
print(diccionario.get("genero"))
# Cambiar un valor de un diccionario
diccionario["nombre"] = "Ester"
print(diccionario)

diccionario["casada"] = "no"
print(diccionario)
# diccionario.pop("casada")
# diccionario.popitem()
# copianiña = diccionario.copy()
copianiña = dict(diccionario)
# del diccionario["casada"]
diccionario.clear()
print(diccionario, copianiña)

rock = {"nombre": "crazy", "decada": 80}
pelicula = {"nombre": "armagedon", "decada": 90}

musica = {"crazy": rock, "armagedon": pelicula}

print(musica)

lapiz = dict(nombre="bic", cantidad=10)
print(lapiz)

verdadero = True
falso = False

print(verdadero, falso)
