# Reto 12 Camilo Sanchez

# PUNTO 1:  Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

-  ## endswith()
   verifica si una cadena termina con una determinada subcadena. Devuelve True si la cadena termina con la subcadena, False en caso contrario.
   
-  ## startswith()
   verifica si una cadena comienza con una determinada subcadena. Devuelve True si la cadena comienza con la subcadena, False en caso contrario.
   
-  ## isalpha()
   verifica si una cadena contiene solo caracteres alfabéticos. Devuelve True si la cadena contiene solo caracteres alfabéticos, False en caso contrario.
   
-  ## isalnum()
   verifica si una cadena contiene solo caracteres alfabéticos o numéricos. Devuelve True si la cadena contiene solo caracteres alfabéticos o numéricos, False en caso contrario
   
-  ## isdigit()
   verifica si una cadena contiene solo dígitos. Devuelve True si la cadena contiene solo dígitos, False en caso contrario.
   
-  ## isspace()
   verifica si una cadena contiene solo espacios en blanco. Devuelve True si la cadena contiene solo espacios en blanco, False en caso contrario.
   
-  ## istitle()
   verifica si una cadena está en mayúsculas. Devuelve True si la cadena está en mayúsculas, False en caso contrario.
   
-  ## istitle()
   verifica si una cadena está en mayúsculas. Devuelve True si la cadena está en mayúsculas, False en caso contrario.
   
-  ## isupper()
   verifica si una cadena está en mayúsculas. Devuelve True si la cadena está en mayúsculas, False en caso contrario.7

# PUNTO 2: Cantidad de vocales
````python
#funcion de str a enteros
def num_vocales(x: str)->int: 
  #se inicia un contador en 0
  letra = 0
  #se recorre la variable 
  for i in x: 
      if i.isalpha() and i in "aeiou" or i in "AEIOU":
          #si se encuentra entre los valores predeterminados suma 1 a la cuenta 
          letra += 1 
  return letra


if __name__ == "__main__":
  #se asigna la varioable con el texto que queremos leer
  texto = "mbox-short.txt" 
  #se abre el archivo y se ejecuta la funcion
  with open(texto, "r") as file: 
      vocales = num_vocales(file.read())
      print(f"Hay {vocales} vocales en el archivo.") 
      
````

# PUNTO 3: Cantidad de consonantes

````python
def numConsonantes(x: str)->int: 
  letras = 0
  for i in x: 
      #mismo precedimiento, simplemente se verifica que NO sean vocales
      if i.isalpha() and i not in "aeiou" and i not in "AEIOU": 
          letras += 1
  return letras


if __name__ == "__main__":
  texto ='mbox-short.txt' 
  with open(texto,"r") as file: 
      Consonantes = numConsonantes(file.read())
      print(f"Hay {Consonantes} consonantes en el archivo.") 
````

# PUNTO 4: Listado de las 50 palabras que más se repiten

````python
#se importa el modulo de collections
import collections
#funcion para contar las palabras
def palabras_repetidas(archivo):
    #se abre el archivo y se separan las palbras con split
    with open(archivo, "r") as file:
        texto = file.read()
        palabras = texto.split()
        #se define la variable unsando Counter que nos permite contar strs en este caso "palabras"
        contador = collections.Counter(palabras)
        #se define que cantidad de palabras requiere al recorrer la lista
        for palabra, veces in contador.most_common(50):
            print(f"La palabra '{palabra}' se repite {veces} veces.")


if __name__ == "__main__":
    #se ejecuta
    palabras_repetidas("mbox-short.txt")
````





   
