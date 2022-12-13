"""Dada la matriz [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de la diagonal principal. Int: Los 3 elementos dela diagonalson 1,5,9"""
# matriz= [[1,2,3],[4,5,6],[7,8,9]]
# matrizFinal= []
# for i in matriz:
#     matrizFinal += i
#     index= matrizFinal[0:-1:4]    ##Porción de la secuencia o lista matriz desde i)primer elemento)  hasta j (el ultima elemento, sin incluirlo), con paso k (a cada 4 pasos)
# ultimoElemento= matrizFinal[-1]
# indexFinal= index.append(ultimoElemento)
# #print(index)
# suma= sum(index)
# print(f'Suma: {suma}')
# promedio= suma / (len(index))
# print(f'Promedio: {promedio}')


"""Dada la siguiente lista escriba un programa que pida al usuario una palabra, dicha palabra debe ser agregada al final y al inicio de la lista."""
# lista= ["Hola","Amigos","Hoy", True]
# palabra= input("Ingrese una palabra: ")
# elementoNuevo= lista[0]= palabra
# elementoNuevo= lista[-1]= palabra
# print(lista)


"""Dada una lista de numeros enteros [15,20,50,80,40,60], escriba un programa que dado un dato por le usuario, 
este sea eliminado de la lista. Tome en cuenta que el usuario ingresara datos que se encuentran dentro de la lista
Ejemplo:
Ingresa el dato a eliminar  60
Salida: [15,20,50,80,40]"""

# datos= [15,20,50,80,40,60]
# print(f'Estos son los datos actuales: {datos}')
# eliminar= int(input("Ingresa el dato a eliminar: "))
# Eliminando= datos.remove(eliminar)
# print(datos)

"""Dada una tupla de numeros (1,3,5,2,7,5,5,8,4,8,4,8,4) escriba un programa que dado un elemento por el usuario,
imprima el numero de veces que se encuentra en la tupla.
Ejemplo:
Ingrese el elemento a contar: 4
salida: 3"""
# tupla= (1,3,5,2,7,5,5,8,4,8,4,8,4)
# print("Estos son los nuemeros dentro de la tupla: (1,3,5,2,7,5,5,8,4,8,4,8,4)")
# numero= int(input("Ingrese el elemento a contar: "))
# contador= tupla.count(numero)
# print(contador)

"""Dado el diccionario que almacena la talla de algunas personas {"Marcelo": 1.80, "Jose": 1.50, "Oscar": 1.70, "Jorge": 1.40} escriba un programa que dado un nombre ingresado por el usuario imprime la talla.
Ejemplo:
Ingrese un nombre: Marcelo
Salida: 1.80 """

# diccionario= {"Marcelo": 1.80, "Jose": 1.50, "Oscar": 1.70, "Jorge": 1.40}
# print("Estas son las personas que puedes consultar sus tallas: Marcelo, Jose, Oscar, Jorge")
# nombre = input("ingrese un nombre: ")
# talla= diccionario[nombre]
# print(talla)

"""Dado el diccionario que almacena la talla de algunas personas {"Marcelo": 1.80, "Jose": 1.50, "Oscar": 1.70, "Jorge": 1.40}
escriba un programa que dada una talla ingresado por el usuario imprime el nombre.
Ejemplo:
Ingrese una talla: 1.80
Salida: Marcelo
https://uniwebsidad.com/libros/python/capitulo-8/metodos-de-retorno"""

diccionario= {"Marcelo": 1.80, "Jose": 1.50, "Oscar": 1.70, "Jorge": 1.40}
print(f"Las tallas son: ", list(diccionario.values()) )
numeroTalla = float(input("ingrese una talla: "))

tallas= list(diccionario.values())
nombres= list(diccionario.keys())
posicionTalla= tallas.index(numeroTalla)
nombre= nombres[posicionTalla]  #Muestra el nombre o elemento que esta en la posicion segun el index de la posicion Talla.

print(f"Salida: {nombre}")

"""Guarde los datos de una persona (nombre, apellido,edad) en un diccionario luego imprimalo en el siguiente formato
"Hola mi nombre es [nombre] [apellido] y tengo [edad] años."""

# datos= {}
# nombre= input("Ingrese su nombre")
# apellido= input("Ingrese su apellido: ")
# edad= input("Ingrese su edad")
# nombre= datos[nombre]
# apellido= datos[apellido]
# edad= datos[edad]

# datos= {"nombre": "Juanita", "Apellido": "Juarez", "Edad": 30}
# nombre= datos["nombre"]
# apellido= datos["Apellido"]
# edad= datos["Edad"]
# print("Hola mi nombre es: ", nombre, apellido, "y tengo", edad, "años")
