calificaciones = [1,2,3,4,5]
nombres = ["Moises", "Camila", "Fernanda", "Pablo", "Tania"]
lista_variada = [True, 10.5, "abc", [0,1,1]]

print("Estudiantes: ", nombres[2])
print("Calificaciones: ", calificaciones[-2])
print("Lista dentro de otra: ", lista_variada[3][0])
print("Imprimir un rango o slices ", nombres[1:2])
print(lista_variada)

#agregar elementos a una lista 
nombres.append("Anibal")
print(nombres)

#remover elementos de una lista
nombres.remove("Pablo")
print(nombres)