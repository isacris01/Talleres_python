#-------------------------------------------EJERCICIO 1-------------------------------------------------
nota1=int(input("ingresa la primera calificacion: "))
nota2=int(input("ingresa la segunda calificacion: "))
nota3=int(input("ingresa la tercera calificacion: "))
lista=[nota1,nota2,nota3]
print(lista)
promedio=nota1+nota2+nota3/3
print(f"El promedio de las calificaciones es: {promedio}")
#-------------------------------------------EJERCICIO 2-------------------------------------------------
productos={
    "lapiz": 1000,
    "borrador": 800,
    "cuaderno":2200
}
print(productos)
porcentaje=float(input("ingrese el porcentaje de aumento(%): "))
productos["lapiz"]+=productos["lapiz"]*(porcentaje/100)
productos["borrador"]+=productos["borrador"]*(porcentaje/100)
productos["cuaderno"]+=productos["cuaderno"]*(porcentaje/100)
print(productos)
#-------------------------------------------EJERCICIO 3-------------------------------------------------
tem1=float(input("temperatura 1 en °c: "))
tem2=float(input("temperatura 2 en °c: "))
tem3=float(input("temperatura 3 en °c: "))
tem4=float(input("temperatura 4 en °c: "))
tem5=float(input("temperatura 5 en °c: "))
celsius=(tem1,tem2,tem3,tem4,tem5)
f1=tem1*9/5+32
f2=tem2*9/5+32
f3=tem3*9/5+32
f4=tem4*9/5+32
f5=tem5*9/5+32
fahrenheit=(f1,f2,f3,f4,f5)
print("temperaturas en °c:",celsius)
print("temperaturas en °F:",fahrenheit)
#-------------------------------------------EJERCICIO 4-------------------------------------------------
edades=[int(input("ingresa la primera edad: ")),int(input("ingresa la segunda edad: ")),int(input("ingresa la tercera edad: ")),int(input("ingresa la cuarta edad: ")),int(input("ingresa la quinta edad: "))]
promedio=sum(edades)/len(edades)
print(f"Mayor: {max(edades)},Menor: {min(edades)},promedio: {promedio}")
#-------------------------------------------EJERCICIO 5-------------------------------------------------
frutas={
    "sandia":3000,
    "fresa":2500,
    "banano":2800
}
print(frutas)
total=0
for fruta,precio in frutas.items():
    kilos=float(input(f"cuantos kilos  de {fruta} quieres?(${precio}por kilo:"))
total2=kilos*precio
print(f"el precio total a pagar ${total2:.2f}")
#-------------------------------------------EJERCICIO 6-------------------------------------------------
num1=int(input("ingresa un numero: "))
num2=int(input("ingresa otro numero: "))
num3=int(input("ingresa otro numero: "))
num4=int(input("ingresa otro numero: "))
num5=int(input("ingresa otro numero: "))
numeros=(num1,num2,num3,num4,num5)
suma=sum(numeros)
print(f"tupla ingresada: ",numeros)
print(f"suma total de los numeros: ",suma)
#-------------------------------------------EJERCICIO 7-------------------------------------------------
inventario=[]
for i in range(3):
    nombre=input(f"Ingrese el nombre del producto {i+1}: ")
    cantidad=int(input(f"Ingrese la cantidad de {nombre}: "))
    precio=float(input(f"Ingrese el precio de {nombre}: "))
    producto={"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)
total=sum(item["cantidad"]*item["precio"] for item in inventario)
print("Total del inventario: $", total)
#-------------------------------------------EJERCICIO 8-------------------------------------------------
p1=int(input("Ingrese el primer precio: "))
p2=int(input("Ingrese el segundo precio: "))
p3=int(input("Ingrese el tercer precio: "))
p4=int(input("Ingrese el cuarto precio: "))
p5=int(input("Ingrese el quinto precio: "))
precios=[p1, p2, p3, p4, p5]
descuento=int(input("Ingrese el descuento en porcentaje (%): "))
nuevo1=p1-(p1*descuento/100)
nuevo2=p2-(p2*descuento/100)
nuevo3=p3-(p3*descuento/100)
nuevo4=p4-(p4*descuento/100)
nuevo5=p5-(p5*descuento/100)
precios_descuento=[nuevo1, nuevo2, nuevo3, nuevo4, nuevo5]
print("Precios originales:", precios)
print("Precios con descuento:", precios_descuento)
#-------------------------------------------EJERCICIO 9-------------------------------------------------
nota1=float(input("Ingrese la primera nota: "))
nota2=float(input("Ingrese la segunda nota: "))
nota3=float(input("Ingrese la tercera nota: "))
nota4=float(input("Ingrese la cuarta nota: "))
notas=(nota1, nota2, nota3, nota4)
nota_mayor=max(notas)
nota_menor=min(notas)
print("Notas ingresadas:", notas)
print("Nota más alta:", nota_mayor)
print("Nota más baja:", nota_menor)
#-------------------------------------------EJERCICIO 10-------------------------------------------------
medidas= {
    "km": 1000,
    "m": 1,
    "cm": 0.01
}
print(medidas)
unidad=input("Escribe la unidad (km, m o cm): ")
cantidad=float(input("Escribe la cantidad a convertir: "))
if unidad=="km":
    resultado=cantidad * 1000
elif unidad=="m":
    resultado=cantidad * 1
elif unidad=="cm":
    resultado=cantidad * 0.01
else:
    resultado=None
    print("Unidad no válida")
if resultado is not None:
    print("Equivale a", resultado, "metros.")
#-------------------------------------------EJERCICIO 11-------------------------------------------------
