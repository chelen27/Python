texto = input('Introduce un titulo o referencia para el nombre de tu fichero')
nombre_fichero = 'archivo-' + texto + '.txt'
f = open( nombre_fichero, 'w') #apertura w= write, r=read, a= append
mensaje = input("Introduce un texto")
f.write(f'{mensaje}\n')
f.close