import requests
import time
import csv
#def Simpsons():
  

 
  
while True:
  URL: str = "https://thesimpsonsquoteapi.glitch.me/quotes"
  respuesta = requests.get(url = URL)
  datos= respuesta.json()
  frase_simpson: str= datos[0]['quote']
  autor: str= datos[0]['character']
  #list=[]
  #list.extend(datos.values())
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

  
  time.sleep(30)