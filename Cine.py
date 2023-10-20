# Numeros random
import random # Pa ids de tiquetes
numero_aleatorio = random.randint(1, 100)  # Genera un número entre 1 y 100 (ambos inclusive)
print(numero_aleatorio)

class Cliente():
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

class Pelicula():
    def __init__(self, id_pelicula, titulo, duracion):
        self.id = id_pelicula
        self.titulo = titulo
        self.duracion = duracion

class Ventas():
    def __init__(self, id_tiquete, id_cliente, nom_cliente, id_pelicula):
        self.tiquete = id_tiquete
        self.cliente = id_cliente
        self.nomCliente = nom_cliente
        self.idPelicula = id_pelicula
        
def buscaPeli(id, peliculas):

    buscador = False

    for i in peliculas:
        if id == i.id:
            buscador = True
            return buscador
        
    return buscador

clientes = []
peliculas = []
ventas = []

def agregaCliente(id_cliente, nombre, apellido):
    nuevo_cliente = Cliente(id_cliente, nombre, apellido)
    clientes.append(nuevo_cliente)
    #print('Cliente agregado exitosamente\n')

def agregaPelicula(id_pelicula, titulo, duracion):
    nueva_pelicula = Pelicula(id_pelicula, titulo, duracion)
    peliculas.append(nueva_pelicula)
    #print('Pelicula agregada exitosamente\n')

def agregaVenta(id_tiquete, id_cliente, nom_cliente, id_pelicula):
    nueva_venta = Ventas(id_tiquete, id_cliente, nom_cliente, id_pelicula)
    ventas.append(nueva_venta)
    #print('Venta realizada exitosamente\n')


# Inicializando Peliculas
agregaPelicula(1, 'Peppa Pig, la pelicula', '3 horas')
agregaPelicula(2, 'The Rat Kid', '2 horas')
agregaPelicula(3, 'Kung fuck panda', '1 horas')


print('Bienvenido a Kevin Cinemas :)\n')
while True:
    opc = int(input('\n\n1. Agregar Pelicula \n2. Realizar Venta \n3. Imprimir Peliculas \n4. Imprimir Clientes \n5. Imprimir Peliculas con determinada letra inicial \n6. Imprimir Ventas \n'))

    if opc == 1:
        id_peli = int(input('Digite el id de la pelicula\n'))
        titu_peli = input('Digite el titulo de la pelicula\n')
        duracion_peli = input('Digite la duracion de la pelicula\nFormato Ejemplo: "3 horas"\n')
        agregaPelicula(id_peli, titu_peli, duracion_peli)
    elif opc == 2:
        id_pelicula = int(input('Digite el id de la pelicula a disfrutar\n'))
        if buscaPeli(id_pelicula, peliculas) == True:
            numero_aleatorio = random.randint(len(peliculas), 100)
            id_tiquete = numero_aleatorio
            # Capturando informacion del cliente
            ced = input('Ingrese su cedula \n')
            nom = input('Ingrese su nombre \n')
            apel = input('Ingrese su apellido \n')
            # Agregando Cliente
            agregaCliente(ced, nom, apel)
            # Agregando Venta id_tiquete, id_cliente, nom_cliente, id_pelicula
            agregaVenta(id_tiquete, ced, nom, id_pelicula)

    elif opc == 3:
        for i in peliculas:
            print('=======================================')
            print (f'ID Pelicula" {i.id} \nTitulo: {i.titulo} \nDuracion: {i.duracion}')

        print('=======================================')
    elif opc == 4:
        for cliente in clientes:
            print ('\n=======================================')
            print(f' ID Cliente: {cliente.id} \n Nombre Cliente: {cliente.nombre} \n Apellido Cliente: {cliente.apellido}')

    elif opc == 5:
        letra = input('\nDigite la letra inicial:')
        for peli in peliculas:
            if peli.titulo[0] == letra:
                print(f'{peli.titulo}')

    elif opc == 6:
        for i in ventas:
            print('=======================================')
            print (f' Tiquete: {i.tiquete} \n Ced Cliente: {i.cliente} \n Nombre Cliente: {i.nomCliente} \n ID Pelicula: {i.idPelicula}')

    else:
        print('\n\nGracias por utilizar nuestros servicios :)')
        break    


        
                 








