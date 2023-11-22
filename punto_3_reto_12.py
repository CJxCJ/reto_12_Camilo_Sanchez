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