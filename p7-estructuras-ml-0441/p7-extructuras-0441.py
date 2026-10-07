# Ramirez Azul NC 0441
# Practica 7 Estructuras

print("========Ejemplo 1=========")
print("Sentencia if")
a = 33
b = 200
if b > a:
    print("b es mayor que a")

print("========Ejemplo 2=========")
print("Python Elif")
a = 33
b = 33
if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")

print("========Ejemplo 3=========")
print("Python Else")
a = 200
b = 33
if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")

print("========Ejemplo 4=========")
print("Bucles for")
fruits = ["manzana", "platano", "cereza"]
for x in fruits:
    print(x)
    if x == "platano":
        break

print("========Ejemplo 5=========")
print("Bucles while")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("Programa realizado por Ramirez Azul NC 0441")