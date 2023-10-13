# Importar locale para compatibilidad con el idioma
import locale
locale.setlocale(locale.LC_ALL, "es")

# --------------- Como imprimir -------------------
entero = 20
flotante = 3.14

print ("El valor entero es {0} y el valor flotante es {1}".format(entero, flotante))

# o tambien se puede imprimir:

print (f"El valor entero es {entero} y el valor flotante es {flotante}")

# para declarar constantes, se simula a traves de funciones

def pi():
    return 3.144444

print ("\nEl valor de pi es: {0} ".format(pi()))


# Notas
# con el %s se trabajan valores STRING
# con el %d se trabajan valores ENTEROS
# con el %f se trabajan valores FLOTANTES

# Trabajando con Varaibles Strings
nombre = input("Digite su nombre ")
print("Hola, %s \n\n" %nombre)

# Trabajando con Variables Enteras
numero = int(input("Digite un numero "))
print("El numero que se digito fue: %d \n\n" %numero )

# Trabajando con flotantes
flotante2 = 9.999999
print("El valor del numero flotante es: %f \n " %flotante2)


# Mi primera suma 
num1 = int(input("Digite un numero para sumar \n"))
num2 = int(input("Digite otro numero para sumar \n"))

print("\n{0} + {1} = {2}" .format(num1, num2, num1 + num2))

# o tambien se puede realizar de la siguiente manera:

print (f"\nla suma de {num1} + {num2} = {num1 + num2} \n")


# --------- Mi primer Contador ---------
contador = 0

print ("Se pueden hacer contadores de la siguiente manera: \n")

contador += 1
print("{0}" .format(contador))
contador += 1
print("{0}" .format(contador))
contador += 1
print("{0}" .format(contador))

print ("\n\n")

#If's en Python

kevinEdad = int(input("digite la edad de Kevin \n"))

if kevinEdad == 20 or kevinEdad == 21:
    print ("Perfecto, usted si sabe xd \n")
elif kevinEdad > 20:
    print ("No estoy asi de viejo xd \n")
else:
    print("Tampoco estoy tan chamaco xd \n")

#Ciclos for en Python + listas/vectores
Animales = ["Loro", "Lobo", "Pez", "Perro", "Gato"]

print ("La lista de animales contiene: \n")
for i in Animales:
    print(f"{i}")

print("\n\n")

#Switch Case's en Python (Se Simulan)
numero1 = 10
numero2 = 2
opc = int (1)

while opc >= 1 and opc <4:
        
        opc = int(input("Digite su opcion.\n1. Sumar valores \n2. Multiplicar valores \n3. Dividir valores \n4. Salir\n\n"))
        if opc == 1:
            print(f"\n{numero1} + {numero2} = {numero1 + numero2} \n")
        elif opc == 2:
            print(f"\n{numero1} x {numero2} = {numero1 * numero2} \n")  
        elif opc == 3:
            print(f"\n{numero1} / {numero2} = {numero1 / numero2} \n")
        elif opc == 4:
             print ("\nSaliendo del programa..")






