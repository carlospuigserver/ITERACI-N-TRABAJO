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

#EJERCICIO 10

#EJERCICIO 11

#EJERCICIO 12

