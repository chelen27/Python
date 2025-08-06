"""Imprimir un cuadrado y un triangulo con asteriscos o cualquier 
otra letra usando la estructura de repetiion for"""

limite = int(input ("Ingrese el numero para su trinagulo"))
tam = int(input("Ingrese el valor para el cuadrado: "))

for x in range (limite):
    print(" ❤ "  * x  )

print("\n")

for x in range (tam):
    print (" ⭐ " * tam)
