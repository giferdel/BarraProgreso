from progress.bar import Bar
import os, random

# OPCIÓN BARRA 3 CON .
def bar_escritura():
    bar3 = Bar('Escribiendo:', fill='.', siffix='%(porcent)d%%')
    caracteres = ['X','O']
    datos = os.getcwd()+ os.sep + 'datos.txt'
    archivo = open(datos, 'w')
    for i in range(100):
        cadena = ''
        long = 500
        for num in range(long):
            cadena += caracteres[random.randint(0,1)]
        archivo.write(cadena + '\n')
        bar3.next()
    bar3.finish()
    archivo.close