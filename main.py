#EJERCICIO 6

#EJERCICIO 7

resultado=[]
print("Elige un número que quieras editar")

num=int(input())
print("Elige una base en la que quieras poner el número que has elegido")

base_num= int(input())


def edici(num,base_num):
  if base_num > 36:
    print(num)

  elif base_num < 2:
    print("La base no es válida")

  else:
    resultado.append(num%base_num)

    if num//base_num ==0:
      print(f"La solución es {resultado}")

    else:
      num=num//base_num
      edici(num, base_num)

  edici(num,base_num)
      




#EJERCICIO 8

entrada = input("Introduce una cadena de texto separada por :" )

n = len(entrada)

SEPARADOR = ":"

lista = entrada.split(":")

print("""
nº      Cadena
""")

subcadenas = list(entrada).count(":")

for numero in range (subcadenas+1):
    posicion = numero +1
    print(posicion, "       ", lista[numero])


  
  
  


  
  
  
#EJERCICIO 9

import sys

lista=[]

def adjuntar():
  print("Elige una palabra para introducirla en el diccionario")

  palabra= str(input())

  lista.append(palabra)
  print(lista)
  print("¿Deseas añadir palabras? elige entre 'si'o 'no' ")

  eleccion=str(input())

  if eleccion == "si"
    adjuntar()

  if eleccion == "no"

  elecc()


def eliminar():

  print ("Selecciona la palabra que desees borrar ")
  borrar=str(input())
  lista.remove(f"{borrar}")
  print(lista)
  elecc()


def ordenar():
  lista.sort()
  print(lista)


def elecc():
  print("Elige una de las siguientes opciones: adjuntar, eliminar, ordenar, o acabar")

  eleccion=str(input())

  if eleccion=="adjuntar"
    adjuntar()


  if eleccion=="eliminar"
    eliminar()

  if eleccion=="ordenar"
    ordenar()

  if eleccion=="acabar"
    print(lista)

    sys.exit

adjuntar()





  

#EJERCICIO 10






#EJERCICIO 11


elecc=int(input("De que manera quieres encontrar el mcd, a partir de Euclides o sumas y restas"))

num1=int(input("Escribe un número que quieras usar:"))

num2=int(input("Escribe otro número que quieras usar:")


if elecc == "Euclides":

  def mcd(num1,num2):
      if num2 == 0:
           return num1
      return mcd ( num2, num1 % num2)

  resultado= mcd ( num1, num2)
  print(f"El mcd resultante de {num1} y {num2} es {result}")


elif elecc == "sumas y restas":
  def mcd(num1, num2):
    if (num1 == 0):
        return num2

    if (num2 == 0):
        return num1

    if (num1 == num2):
        return num1

    if (num1 > num2):
        return mcd( num1-num2, num2)

    return mcd ( num1, num2-num1)  


  if(mcd(num1, num2)):
    result= mcd(num1, num2)
    print(f"El mcd  de {num1} y {num2} es {result})




else:
    print("En este caso no podemos realizar el mcd")











#EJERCICIO 12

#ALGORITMO1
#VARIABLE
limite = int(input("Selecciona el número límite: "))

#REALIZACIÓN
range(limite)

listanumero = []

print(range(limite))

for i in range(limite):
    listanumero.append(i**2)
    if i**2>limite:
        break

listanumero.pop(-1)

print(listanumero)