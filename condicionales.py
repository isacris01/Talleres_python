
"""numero1=float(input("ingrese un numero:"))
if numero1 > 0:
    print("positivo")
elif numero1 < 0 :
    print(f"es negativo por que es{numero1}")
else:
    print(f"es cero{numero1}")
#2 .Calcular el mayor de dos numeros ingresados
num1=float(input("ingrese un numero:"))
num2=float(input("ingrese otro numero:"))
if num1>num2:
    print(f"el numero mayor es {num1}")
elif num2>num1:
    print(f"el numero ayor es {num2}")
else:
    print(f"ambos numeros son iguales.")
#-----------------------------------EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMATICAS-----------------
#----------------------------------------EJERCICIO 1-------------------------------------------------
numero1=float(input("ingrese un numero:"))
if numero1 > 0:
    print("positivo")
elif numero1 < 0 :
    print(f"es negativo por que es{numero1}")
else:
    print(f"es cero{numero1}")
#----------------------------------------EJERCICIO 2-------------------------------------------------
num1=float(input("ingrese un numero:"))
num2=float(input("ingrese otro numero:"))
if num1>num2:
    print(f"el numero mayor es {num1}")
elif num2>num1:
    print(f"el numero ayor es {num2}")
else:
    print(f"ambos numeros son iguales.")
#----------------------------------------EJERCICIO 3-------------------------------------------------
numero=float(input("ingrese un numero:"))
if numero % 2 == 0:
    print("El numero es par: ")
else:
    print("el numero es impar")
#----------------------------------------EJERCICIO 4-------------------------------------------------
numero2=float(input("ingrese un numero:"))
if 10<=numero2 <=20 :
    print(f"el numero {numero2} esta entre 10 y 20 ")
else:
    print(f"el numero {numero2} NO esta entre 10 y 20")
#----------------------------------------EJERCICIO 5-------------------------------------------------
num1=float(input("ingrese el primer numero:"))
num2=float(input("ingrese el segundo numero:"))
num3=float(input("ingrese el tercer numero:"))
if num1>num2 and num1>num3:
    print(f"el numero mayor es {num1}")
elif num2>num1 and num2>num3:
    print(f"el numero mayor es {num2}")
else:
    print(f"el numero mayor es {num3}")
#----------------------------------------EJERCICIO 6-------------------------------------------------
precio=float(input("Ingresa el precio: "))
if precio > 100:
    descuento=precio * 0.10
    total_final=precio - descuento
else:
    total_final=precio
print("El precio final es:", total_final)
#----------------------------------------EJERCICIO 7-------------------------------------------------
edad=float(input("ingrese su edad:"))
if edad>= 18:
    print("puede votar por que es mayor de edad ")
else:
    print("no puede votar,por que es menor de edad")"""
#----------------------------------------EJERCICIO 8-------------------------------------------------
precio=float(input("Ingresa el precio: "))
tipo=input("Ingresa el tipo de cliente (VIP o normal): ")
if tipo=="VIP":
    precio_final=precio * 0.80
else:
    precio_final=precio
print("El precio final es:", precio_final)
#----------------------------------------EJERCICIO 9-------------------------------------------------

