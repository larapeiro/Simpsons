import requests
import csv
import time
import os
import string

#Definimos la función que contiene el contador de palabras
def contador(str, contador_palabras):
  contador = contador_palabras
  palabras=str.split()

  for palabra in palabras:
    if palabra in contador:
      contador[palabra] += 1
    else:
      contador[palabra] = 1

  return contador

dict_palabras=dict()

while True:
#Extraemos los datos del JSON
  URL = "https://thesimpsonsquoteapi.glitch.me/quotes"
  try:
    respuesta = requests.get(URL,timeout=30)
  except requests.exceptions.Timeout as error:
    print(error)
    time.sleep(30)

  #Añadimos la condición de respuesta. Fuente: https://keepcoding.io/blog/trabajar-con-codigos-estado-de-respuesta-http/#Condicion_de_la_respuesta
  if respuesta.status_code >= 200 and respuesta.status_code < 300:
    #Definimos los datos que obtenemos
    datosjson= respuesta.json()
    frase_simpson= datosjson[0]["quote"]
    personaje= datosjson[0]["character"]
    imagen= datosjson[0]["image"]
     
    #Usamos str.translate para eliminar los signos de puntuación de la cadena de texto con el método de .maketrans().
    #Fuente: https://datagy.io/python-remove-punctuation-from-string/
    datos= {"Personaje": datosjson[0]["character"].translate(str.maketrans("","", string.punctuation)).split(), "Frase": datosjson[0]["quote"]}

  print("{}: {}".format(" ".join(datos["Personaje"]), datos["Frase"]))
  #Indicamos el diccionario que tiene que actualizarse a través de la función definida anteriormente y sus atributos
  dict_palabras=contador(frase_simpson, dict_palabras)
#Generamos el documento que contendrá el contador
  with open('palabras.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for key, value in dict_palabras.items():
      writer.writerow([key, value]) 

#Creamos el directorio para cada personaje. Para ello, en primer lugar tenemos que comprobar si ya existe el directorio o no.
# Fuente: https://www.delftstack.com/es/howto/python/python-create-directory/#crear-directorio-en-python-usando-los-m%25C3%25A9todos-path.exists-y-makedirs-del-m%25C3%25B3dulo-os
  if not os.path.exists("_".join(datos["Personaje"])):
    os.makedirs("_".join(datos["Personaje"]))

#A continuación, tenemos que almacenar la frase de cada personaje en su correspondiente csv indicando la ruta (LisaLevel)

  with open ("_".join(datos["Personaje"]) + '/' + 'quotes' + "" + "_".join(datos["Personaje"]) + '.csv', 'a') as directorio:
    w = csv.DictWriter(directorio, datos.keys())
    if directorio.tell() == 0:
      w.writeheader()
      
      w.writerow({'Personaje':" ".join(datos["Personaje"]), 'Frase': datos["Frase"]})
  
#Descargamos y almacenamos la imagen del personaje en su carpeta correspondiente indicando la ruta (LisaLevel)
  with open("_".join(datos["Personaje"]) + '/' + "".join(datos["Personaje"]) +'.png', 'wb') as handler:
    if handler.tell() == 0:
      imagen_personaje= requests.get(imagen).content
      handler.write(imagen_personaje)

time.sleep(30)