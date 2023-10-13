import openpyxl

# Crear un nuevo libro de trabajo (workbook)
workbook = openpyxl.Workbook()

# Crear diferentes hojas en el libro
sheet1 = workbook.active
sheet1.title = "Hoja1"

# Agregar datos a la primera hoja
sheet1['A1'] = 'Hola'
sheet1['B1'] = 'Mundo'

# Crear una segunda hoja
sheet2 = workbook.create_sheet(title="Hoja2")
sheet2['A1'] = 'Datos'
sheet2['A2'] = 1
sheet2['A3'] = 2
sheet2['A4'] = 3

# Guardar el libro de trabajo en un archivo
workbook.save('documento_excel.xlsx')

# Abrir el archivo después de guardarlo
import os

# Ruta al archivo Excel
archivo_excel = 'documento_excel.xlsx'

# Verificar si el archivo existe
if os.path.exists(archivo_excel):
    os.system('start excel.exe "%s"' % archivo_excel)
else:
    print("El archivo no se encuentra.")

print("Proceso completado.")
