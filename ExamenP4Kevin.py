import locale
locale.setlocale(locale.LC_ALL, "es")


# Clases #
class Libro:
    def __init__(self, titulo, autor, editorial, fecha_publicacion, descripcion):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
        self.descripcion = descripcion

class Editorial:
    def __init__(self, nombre, ubicacion, website):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.website = website

class Usuario:
    def __init__(self, id, nombre_completo, tipo):
        self.id = id
        self.nombre_completo = nombre_completo
        self.tipo = tipo

#Creacion de Listas de cada usuario
libros_usuario1 = []  # <--------- Libros y anotaciones de usuario 1 <------------------
anotaciones_usuario1 = ['','','','','']
libro_en_uso_usuario1 = ''

libros_usuario2 = []  # <--------- Libros y anotaciones de usuario 2 <------------------
anotaciones_usuario2 = ['','','','','']
libro_en_uso_usuario2 = ''

# Creacion de usuarios
usuario1 = Usuario('118610670', 'Kevin Cordoba Rivera', 'Estudiante')
usuario2 = Usuario('603450876', 'Pepito Arias Madrigal', 'Profesor')

#Creacion de los libros disponibles en la biblioteca
libros_existentes = []

# Anadiendo libros
libro1 = Libro("Soledad", "Gabriel García Márquez", "Sudamericana", "30 de mayo de 1967", "Una novela clásica de realismo mágico.")
libro2 = Libro("1984", "George Orwell", "Secker & Warburg", "8 de junio de 1949", "Una novela distópica sobre un futuro totalitario.")
libro3 = Libro("Ruisenior", "Harper Lee", "J.B. Lippincott & Co.", "11 de julio de 1960", "Una historia sobre racismo y moralidad en el sur de Estados Unidos.")
libro4 = Libro("Quijote", "Miguel de Cervantes", "Francisco de Robles", "17 de enero de 1605", "Una de las obras cumbres de la literatura española.")
libro5 = Libro("Potter", "J.K. Rowling", "Bloomsbury", "26 de junio de 1997", "El primer libro de la famosa serie de Harry Potter.")

libros_existentes.append(libro1)
libros_existentes.append(libro2)
libros_existentes.append(libro3)
libros_existentes.append(libro4)
libros_existentes.append(libro5)

# Inicializar editoriales    

editoriales = []

editorial1 = Editorial('Sudamericana', 'Ciudad del Este, Alto Paraná, Paraguay', 'www.sudamericana.com')
editorial2 = Editorial('Secker & Warburg', 'Springfield, Illinois, Estados Unidos', 'www.seckerandwarburg.com')
editorial3 = Editorial('J.B. Lippincott & Co.', 'Melbourne, Victoria, Australia', 'www.jblippincottco.com')
editorial4 = Editorial('Francisco de Robles', 'Buenos Aires, Buenos Aires, Argentina', 'www.franciscodeRobles.com')
editorial5 = Editorial('Bloomsbury', 'London, England, United Kingdom', 'www.bloomsbury.com')

editoriales.append(editorial1)
editoriales.append(editorial2)
editoriales.append(editorial3)
editoriales.append(editorial4)
editoriales.append(editorial5)


# Funciones
def buscaLibro(nom_libro):
    for i, libro in enumerate(libros_existentes):
        if libro.titulo == nom_libro:
            return i
    return -1

def buscaAnotaciones1(pos):
    return anotaciones_usuario1[pos] 

def buscaAnotaciones2(pos):
    return anotaciones_usuario2[pos] 

print('===================================== \n' )
print('Bienvenido a la Biblioteca Digital Kevin SA :) \n')

# Empezando Main Code
while True:
    print('Digite el usuario con el que desea ingresar.')
    user = int(input('\n 1. Kevin Cordoba Rivera \n 2. Pepito Arias Madrigal \n---> '))

    if user == 1:

        # imprimir usuario 1
        print('Usted ha seleccionado al siguiente usuario:\n')
        print(f'ID Usuario: {usuario1.id}')
        print(f'Nombre Usuario: {usuario1.nombre_completo}')
        print(f'Tipo Usuario: {usuario1.tipo}')


        if libro_en_uso_usuario1 == '':
            print('El usuario no se encuentra utilizando ningun libro.\n')
        else:
            print(f'El usuario se encuentra utilizando el libro: {libro_en_uso_usuario1}\n')
        
        #Seguir en esta linea
        print('Lista de libros favoritos del usuario:\n')

        for i in libros_usuario1:
            print(f'{i}\n')

        opc = int(input(' 1. Añadir libro a lista de favoritos \n 2. Utilizar un libro \n 3. Libros y anotaciones del usuario \n 4. Informacion de editoriales \n 5. Salir \n '))
        if opc == 1: #Anadiendo libro
            print('\nLista de libros disponibles:\n')
            for i in libros_existentes:
                print('=====================================')
                print(f' Titulo: {i.titulo} \n Autor: {i.autor}')

            libro_a_anadir = input('Digite el libro que desea añadir:\n ')
            verificador = buscaLibro(libro_a_anadir) # <-- Guardando posicion si encuentra libro, si no encuentra guarda -1

            if verificador !=-1:
                print(' \nEl libro se encontro exitosamente!')
                libros_usuario1.append(libro_a_anadir)
                print('Lista de favoritos del usuario:')
                for i in libros_usuario1:
                    print('=====================================')
                    print(f'{i}')
                print()

                anot = int(input('Desea realizar anotaciones?\n1. Si\n2. No\n'))
                if anot == 1:
                    anotacion = input('Digite su anotacion:\n')
                    anotaciones_usuario1[verificador] = anotacion
                else:
                    anotaciones_usuario1[verificador] = ''

                # Seguir
                resultado = buscaLibro(libro_a_anadir)
                if resultado != -1:
                    anotacioness = buscaAnotaciones1(resultado)
                    print(f'\nAnotaciones Guardadas: {anotacioness} \n')
                
            else:
                print('Libro no encontrado.')

        elif opc == 2:
            print('Utilizar un libro')
            libro_a_utilizar = input('Digite el libro que desee utilizar:\n')
            buscador = buscaLibro(libro_a_utilizar)

            if buscador != -1:
                libro_en_uso_usuario1 = libro_a_utilizar
            else:
                print('Este libro no se encuentra disponible para utilizar.')

        elif opc == 3:
            print('Lista de libros favoritos del usuario con sus anotaciones:')
            index = 1
            for i in libros_usuario1:
                print(f'Libro {index}: {i}')
                index += 1
            #print('anotaciones')
            index = 1
            for i in anotaciones_usuario1:
                if i != '':
                    print(f'Anotacion del libro {index}: {i}')
                    index += 1
        elif opc == 4:
            for i in editoriales:
                print('=====================================')
                print(f'Nombre: {i.nombre}')
                print(f'Ubicacion: {i.ubicacion}')
                print(f'website: {i.website}')

        elif opc == 5:
            print('Gracias por utilizar este programa :)')
            break

    elif user == 2:
        # imprimir usuario 2
        print('Usted ha seleccionado al siguiente usuario:\n')
        print(f'ID Usuario: {usuario2.id}')
        print(f'Nombre Usuario: {usuario2.nombre_completo}')
        print(f'Tipo Usuario: {usuario2.tipo}')

        if libro_en_uso_usuario2 == '':
            print('El usuario no se encuentra utilizando ningun libro.\n')
        else:
            print(f'El usuario se encuentra utilizando el libro: {libro_en_uso_usuario2}\n')
        
        #Seguir en esta linea
        print('Lista de libros favoritos del usuario:\n')

        for i in libros_usuario2:
            print(f'{i}\n')

        opc = int(input(' 1. Añadir libro a lista de favoritos \n 2. Utilizar un libro \n 3. Libros y anotaciones del usuario \n 4. Informacion de Editoriales \n 5. Salir \n '))
        if opc == 1: #Anadiendo libro
            print('\nLista de libros disponibles:\n')
            for i in libros_existentes:
                print('=====================================')
                print(f' Titulo: {i.titulo} \n Autor: {i.autor}')

            libro_a_anadir = input('Digite el libro que desea añadir:\n ')
            verificador = buscaLibro(libro_a_anadir) # <-- Guardando posicion si encuentra libro, si no encuentra guarda -1

            if verificador !=-1:
                print(' \nEl libro se encontro exitosamente!')
                libros_usuario2.append(libro_a_anadir)
                print('Lista de favoritos del usuario:')
                for i in libros_usuario2:
                    print('=====================================')
                    print(f'{i}')
                print()

                anot = int(input('Desea realizar anotaciones?\n1. Si\n2. No\n'))
                if anot == 1:
                    anotacion = input('Digite su anotacion:\n')
                    anotaciones_usuario2[verificador] = anotacion
                else:
                    anotaciones_usuario2[verificador] = ''

                # Seguir
                resultado = buscaLibro(libro_a_anadir)
                if resultado != -1:
                    anotacioness = buscaAnotaciones1(resultado)
                    print(f'\nAnotaciones Guardadas: {anotacioness} \n')
                
            else:
                print('Libro no encontrado.')

        elif opc == 2:
            print('Utilizar un libro')
            libro_a_utilizar = input('Digite el libro que desee utilizar:\n')
            buscador = buscaLibro(libro_a_utilizar)

            if buscador != -1:
                libro_en_uso_usuario2 = libro_a_utilizar
            else:
                print('Este libro no se encuentra disponible para utilizar.')

        elif opc == 3:
            print('Lista de libros favoritos del usuario con sus anotaciones:')
            index = 1
            for i in libros_usuario2:
                print(f'Libro {index}: {i}')
                index += 1
            #print('anotaciones')
            index = 1
            for i in anotaciones_usuario1:
                if i != '':
                    print(f'Anotacion del libro {index}: {i}')
                    index += 1

        elif opc == 4:
            for i in editoriales:
                print('=====================================')
                print(f'Nombre: {i.nombre}')
                print(f'Ubicacion: {i.ubicacion}')
                print(f'website: {i.website}')

        elif opc == 5:
            print('Gracias por utilizar este programa :)')
            break

    else:
        print('Opcion no valida, por favor intentar nuevamente...\n')
        

