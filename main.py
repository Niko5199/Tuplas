lista_numeros = [1,2,3,4,5]
lista_strings = ['Hola','Adios','Qué']
lista_bool = [True, False]

listas = [*lista_numeros,*lista_strings]
print(listas)

def printNumbers(a,b,*c):
    for contador in c:
        print(contador)
    
printNumbers(*lista_numeros)
"""
    Las tuplas son muy parecidas a las listas
    las tuplas nos permiten almacenar diferentes tipos
    de datos strings, int, floats, bools, listas, tuplas
    diccionarios.

    La principal diferencia entre las listas y tuplas son 
    inmutables es decir una ves que nosotros definamos una tupla
    asi se quedara por el resto del programa

    Cada elemento de la tupla contiene un indice e igual que
    las listas los indices comienzan apartir del 0

    La tupla principalmente nos servira para consultar valores
    puesto que no podemos añadir o quitar elementos de ella, ni
    modificar los elementos que ella contenga

    Ahora las tuplas tienen una ventaja muy importante a la hora
    de querer compararlas con las listas, ya que las tuplas son
    mas rapidas para obtener elementos ya que en python son 
    objetos inmutables python las almacena en un espacio especial en
    memoria solo para lectura. Las tuplas son perfectas para leer 
    de manera rapida datos

"""

tupla = ('Strings',10,15.4,True,[1,2,3],(4,5,6))

print(tupla)


cursos = ('Python','Flask','Django','Rails','MongoDB')

# Obtener elemento

primer_curso = cursos[0]
print(primer_curso)