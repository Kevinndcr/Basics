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
            

