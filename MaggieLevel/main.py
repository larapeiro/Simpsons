import requests
import time
import csv

 
  
while True:

  #Extraemos los datos del JSON
  URL: str = "https://thesimpsonsquoteapi.glitch.me/quotes"
  respuesta = requests.get(url = URL)
  datos= respuesta.json()
  frase_simpson: str= datos[0]['quote']
  autor: str= datos[0]['character']
  
  #Añadimos las condicionales indicando la ruta donde tiene que almacenarse y la información que almacena el diccionario
  if autor == 'Lisa Simpson':
    my_dict = {'quote': frase_simpson, 'character':autor}
    with open('MaggieLevel/Lisa/lisa.csv', 'a') as csvfile:
      w = csv.DictWriter(csvfile, my_dict.keys())

      w.writerow(my_dict)
    
  elif autor == 'Homer Simpson':
    my_dict = {'quote': frase_simpson, 'character':autor}
    with open('MaggieLevel/Homer/homer.csv', 'a') as csvfile:
      w = csv.DictWriter(csvfile, my_dict.keys())

      w.writerow(my_dict)

  else:
      
    my_dict = {'quote': frase_simpson, 'character':autor}
    with open('MaggieLevel/General/general.csv', 'a') as csvfile:
      w = csv.DictWriter(csvfile, my_dict.keys())

      w.writerow(my_dict)

  #Tiempo que indicamos para que vuelva a correr el código
  time.sleep(30)