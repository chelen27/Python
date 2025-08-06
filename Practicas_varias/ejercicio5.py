print("Programa que imprime los números pares entre dos numeros dados")
inicio = int(input("Ingrese el valor de inicio: \n"))
limite = int(input("Ahora el valor de Fin: \n"))

for x in range (inicio, limite):
    if x % 2 == 0:
        print(f" | {x}", end = " ")