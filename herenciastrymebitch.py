class Padre:
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        
class Hijo(Padre):
    def __init__(self, id, nombre, apellido, pasatiempo):
        super().__init__(id, nombre, apellido)
        self.pasatiempo = pasatiempo

hijos = []

id = input('Digite su id\n')
nom = input('Digite su nombre\n')
ape = input('Digite su apellido\n')
pasatiempo = input('Digite su pasatiempo\n')

objHijo1 = Hijo(id, nom, ape, pasatiempo)
hijos.append(objHijo1)

print('\nSegundo Hijo\n')
id = input('Digite su id\n')
nom = input('Digite su nombre\n')
ape = input('Digite su apellido\n')
pasatiempo = input('Digite su pasatiempo\n')

objHijo2 = Hijo(id, nom, ape, pasatiempo)
hijos.append(objHijo2)

print('========================')
for i in hijos:
    print(f'Id: {i.id} \nNombre: {i.nombre} \nApellido: {i.apellido} \nPasatiempo: {i.pasatiempo}')
    print('========================')


    













