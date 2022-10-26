"""
 * -> Lista
  _ -> Omitimos valores, con el guion bajo
  le indicamos a python que la lista que desesctructuramos
  no nos interesa y que queremos hacer caso omiso de ella
"""

numeros = (1,2,3,4,5,6,7,8,9,10)
uno, _, tres,_, *resto, diez= numeros

print(uno)
print(tres)
print(resto)
print(diez)
print(type(resto))  