class Persona:
    def __init__(self, nombre, apellido, anhonac):
        self.nombre = nombre
        self.apellido = apellido
        self.anhonac = anhonac

personas_registradas = []
print("Bienvenido a mi programa :) \n")
while True:
    
    opc = int(input("1. Registrar a una persona \n2. Imprimir Personas registradas \n3. Salir \n"))

    if opc == 1:
        nombre = input("Digite su nombre: \n")
        apellido = input("Digite su apellido: \n")
        anhonac = int(input("Digite su anho de nacimiento: \n"))
        personaa = Persona(nombre, apellido, anhonac)
        personas_registradas.append(personaa)

        opc2 = int(input('Desea imprimir los datos de la personas registrada?\n 1.Si \n 2.No\n'))
        if opc2 == 1:
            print(f'Nombre: {personaa.nombre}')
            print(f'Apellido: {personaa.nombre}')
            print(f'Anho nacimiento: {personaa.nombre} \n')
            print(f'Edad: {2023 - anhonac} \n')
        else:
            print('ok \n')

    elif opc == 2:
        for i in personas_registradas:
                print(f'Nombre: {i.nombre}\nApellido: {i.apellido}\nAnho nacimiento: {i.anhonac}\n ============================')
    else:
        print('Gracias por utilizar el programa :)')
        break
        


















