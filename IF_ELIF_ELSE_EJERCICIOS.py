"""vocales=(input("ingrese una vocal: "))
if vocales== "e" :
    print(f"la vocal {vocales} en mayusculas es E")
elif vocales=="a":
    print(f"la vocal {vocales} en mayusculas es A")
elif vocales=="i" :
    print(f"la vocal {vocales} en mayusculas es I")
elif vocales=="o" :
    print(f"la vocal {vocales} en mayusculas es O")
elif vocales=="u" :
    print(f"la vocal {vocales} en mayusculas es U")
else:
    print(f"{vocales} no es una vocal")
#EJEMPLO 1
comando="SALIR"
if comando=="ENTRAR":
    print("Bienvenido al sistema.")
elif comando=="SALUDO":
    print("Hola!¿como estas?")
elif comando=="SALIR":
    print("saliendo del sistma.")
else:
    print("no se reconoce el comando.")
#-------------------------------------EJERCICIO 1---------------------------------------------------
# Se solicita al usuario que ingrese un número
num=int(input("ingrese un numero: "))
# Se evalúa si el número es mayor que 0 (positivo)
if num>0:
    print(f"el numero {num} es positivo")
# Se evalúa si el número es exactamente 0
elif num==0:
    print(f"el numero {num} es 0 ")
# Se evalúa si el número es menor que 0 (negativo)
elif num<0:
    print(f"el numero {num} es negativo ")
else:
    print("esta opcion no es validad con las condicciones .")
#-------------------------------------EJERCICIO 2---------------------------------------------------
#Se solicita al usuario que ingrese los números
num=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))
#Se compara si el primer número es mayor que el segundo
if num>num2:
    print(f"el numero mayor es {num}")
elif num2>num:
#Se compara si el segundo número es mayor que el primero
    print(f"el numero mayor es {num2}")
else:
    print("esta opcion no cumple con las condicciones .")
#-------------------------------------EJERCICIO 3---------------------------------------------------
#Determina si un número es par o impar.
num=int(input("ingrese un numero: "))
# Si el residuo de dividir el número entre 2 es 0, es par
if num % 2 == 0:
    print(f"El número {num} es par.")
else:
# Si no, es impar
    print(f"El número {num} es impar.")
#-------------------------------------EJERCICIO 4---------------------------------------------------
# Se solicita al usuario que ingrese un número
num=int(input("ingrese un numero: "))
# Se verifica si el número entre 10 y 20
if num>10 and num <20: 
    print(f"el numero {num} esta entre 10 y 20")
# Si no se cumple la condición, se muestra el siguente mensaje 
else:
    print(f"el numero {num} no esta entre 10 y 20")
#-------------------------------------EJERCICIO 5---------------------------------------------------
#Se solicita al usuario que ingrese los números
num=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero numero: "))
num3=int(input("ingrese el tercer numero numero: "))
# Comparamos si el primer número es mayor que los otros dos
if num >= num2 and num >= num3:
    print(f"El número mayor es: {num}")
# Si no, verificamos si el segundo número es mayor o igual que los otros dos
elif num2 >= num and num2 >= num3:
    print(f"El número mayor es: {num2}")
# Si ninguna de las anteriores se cumple, entonces el tercero es el mayor
else:
    print(f"El número mayor es: {num3}")
#-------------------------------------EJERCICIO 6---------------------------------------------------
# Se solicita al usuario el valor total de la compra
total=float(input("Ingrese el total de la compra: $"))
# Se evalúa si el total es mayor a $100
if total > 100:
# Se aplica un descuento del 10%
    descuento = total * 0.10
    precio_final = total - descuento
    print(f"Se aplicó un 10% de descuento. El precio final es: ${precio_final}")
else:
# Si no supera $100, no hay descuento
    print(f"No se aplica descuento. El precio final es: ${total}")
#-------------------------------------EJERCICIO 7---------------------------------------------------
#Se pide al usuario que ingrese su edad
edad=int(input("ingrese su edad: "))
#se verifica que sea igual o mayor de cero para que pueda votar
if edad>=18:
    print(f"su edad es {edad} y puede votar")
#si no,no puede votar
else:
    print(f"su edad es {edad} y NO puede votar")
#-------------------------------------EJERCICIO 8---------------------------------------------------
# Se solicita al usuario el precio del producto
precio=int(input("ingresa el precio del producto: "))
# Se solicita el tipo de cliente (VIP o normal)
tipo_cliente=input("ingresa el tipo de cliente(VIP o normal)")
# Se verifica si el cliente es VIP
if tipo_cliente == "VIP":
# Se calcula el descuento del 20%
    descuento = precio * 0.20
    precio_final = precio - descuento
    print(f"Cliente VIP: se aplicó un 20% de descuento. Precio final: ${precio_final:}")
else:
# Si no es VIP, no se aplica descuento
    print(f"Cliente normal: no hay descuento. Precio final: ${precio:}")
#-------------------------------------EJERCICIO 9---------------------------------------------------
# Se solicita al usuario que ingrese un número 
num=int(input("ingrese un numero: "))
# Se verifica si el número es multiplo de 5 y 3
if num % 5 == 0 and num % 3 == 0:
    print(f"El número {num} es múltiplo de 5 y de 3 al mismo tiempo.")
else:
    print(f"El número {num} NO es múltiplo de 5 y de 3 al mismo tiempo.")
#-------------------------------------EJERCICIO 10---------------------------------------------------
# Se solicita el número principal
num=int(input("ingrese un numero: "))
# Se solicitan los dos divisores
divi1=int(input("Ingrese el primer divisor: "))
divi2=int(input("Ingrese el segundo divisor: "))
# Se evalúa si el número es divisible entre ambos divisores
if num % divi1 == 0 and num % divi2 == 0:
    print(f"El número {num} es divisible entre {divi1} y {divi2}.")
#si no
else:
    print(f"El número {num} NO es divisible entre {divi1} y {divi2}.")
#-------------------------------------EJERCICIO 11---------------------------------------------------
# Se crea la lista con 5 números
numeros=[1,2,3,4,5]
# Se accede al tercer número
tercer_numeros =numeros[2]
# Se evalúa si el tercer número es mayor que 10
if tercer_numeros >= 10:
    print(f"el numero {tercer_numeros} es Mayor a 10")
else :
    print(f"el numero {tercer_numeros} es Menor a 10")"""
#-------------------------------------EJERCICIO 12---------------------------------------------------
numeros3=[3,5,7,9]
#-------------------------------------EJERCICIO 16---------------------------------------------------
#se crea la tupla
numeros=(5,8,12,20)
# Se accede al primer valor (índice 0) y al último valor (índice -1)
primer_valor=numeros[0]
ultimo_valor=numeros[-1]
# Se evalúa si el primer valor es menor que el último
if primer_valor < ultimo_valor:
    print("Orden ascendente")
else:
    print("Orden descendente")
#-------------------------------------EJERCICIO 17---------------------------------------------------
edades=(25,32,28)
segundo_num=edades(1)
if segundo_num >30:
    edad
  






