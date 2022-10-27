![N|Solid](https://static.simpsonswiki.com/images/thumb/0/0a/Simpson_family_s27.png/200px-Simpson_family_s27.png)
# Fundamentos - Entregable 0  
## The Simpsons 

El Entregable 0 correspondiente al módulo de Fundamentos supone el primer reto al que los alumnos del MDA tenemos que hacer frente. En dicho ejercicio pondremos en práctica y de manera conjunta todo lo aprendido en las diferentes sesiones del modulo:

- GIT
- Unix
- Python
- Docker
- Docker-Compose

## Análisis del caso 
El objetivo es crear un código python que consuma datos de una api sobre los Simpsons y guarde la información en ficheros csv y carpetas según su personaje y de manera automática.

## Niveles

Este ejercicio se divide en varios niveles según su complejidad siendo únicamente obligatorios los dos primeros niveles.

- ##### Nivel Maggie:
    
    Este primer nivel es el más básico. Consta de 4 pasos:
    1. Usando google colab crear un notebook que consuma la api de los simpsons y haga una
consulta cada 30seg a la API
    2. El código debe guardar cada quote en un csv dentro de una carpeta con el nombre del
personaje (Lisa y Homer) y en un fichero que llamaremos general (Todos).
    3. Generar un fichero Docker que copie el código dentro del contenedor y se ejecute de
manera autónoma. El Docker debe tener el código en una carpeta app
    4. El fichero docker debe crear al menos las carpetas Lisa y Homer e inicialmente solo coger
citas de ellos dos.

- ##### Nivel Lisa:

    Este segundo nivel es de dificultad media. Consta de 3 pasos:
    1. Mejorad el código para descargar la imagen del personaje y guardadla en la carpeta del
mismo.
    2. El código debe mantener un diccionario de palabras y escribir en cada iteración en un
fichero el conteo de palabras que lleva.
a. The;1
b. Great;2
    3. El código debe crear de manera dinámica las carpetas con nuevos personajes
    
- ##### Nivel Bart:

    Este tercer nivel es el de mayor dificultad y su entrega es voluntaria. Consta de 4 pasos:
    1. Construid un Docker-compose con una imagen de un contenedor de Jupyter
    2. Dentro del Jupyter generad un notebook con una gráfica mostrando las
palabras más habituales en las quotes
    3. Mostrar un listado de las carpetas y las fotos de los personajes en el jupyter
    4. Docker-compose debe ser capaz de hacer build del contenedor original

## Mi experiencia con el Entregable 0
Perfil no técnico, miedo a la "pantalla negra", poco conocimiento de código para la exigencia del ejercicio...
El primer ejercicio (Maggie) fue "relativamente sencillo" puesto que se realizo en clase y tuvimos mucha ayuda para su elaboración. Al principio, dudaba si podría conseguirlo, pero al final entendí lo que se pedía y con paciencia y MUCHA AYUDA lo conseguí.

![N|Solid](https://media4.giphy.com/media/elLS45yY6efXa/giphy.gif?cid=ecf05e470y2ri8ljxyrhhlamk8twckjf4e54x39piozfze9u&rid=giphy.gif&ct=g)

El ejercicio de Lisa, en mi opinión, fue de un nivel demasiado elevado. Me costaba mucho entender que se me pedía y eso solo hizo que empeorar el nivel de frustración. Al final opté por "mejorar" el archivo de Maggie. Recurrí a San Google y a todos los foros de Python habidos y por haber. Aquí es cuando me dí cuenta que lo difícil no era el código en sí, sino saber qué estas copiando, es decir, COMPRENDER cada parte del código usando la lógica.

![N|Solid](https://media0.giphy.com/media/3o6MbdaV12BHr9Y4yA/giphy.gif?cid=790b7611b49a461e65a40be330e3c0982e53ce9f9d881f12&rid=giphy.gif&ct=g)

Y bueno, por último, el de Bart solo puedo decir una cosa:

![N|Solid](https://media3.giphy.com/media/26ybwvTX4DTkwst6U/giphy.gif?cid=ecf05e477qjfnxp62jqaczej6hfp53oeyzdlqh7t0d9sawkl&rid=giphy.gif&ct=g)

## Cosas que  he aprendido

##### - Nadie nace sabiendo

![N|Solid](https://media4.giphy.com/media/3orif0rjs49gsPWg1y/giphy.gif?cid=790b76118c449f15e13a4fd2b2ca9edfd66c523aa0b2ca7f&rid=giphy.gif&ct=g)

##### - Es normal sentirse frustrado

![N|Solid](https://media0.giphy.com/media/xT5LMVrEF6eYgXDddK/giphy.gif?cid=ecf05e47xz0ch3suo06sh1icch3qswrqxjeea4ec9lmaou9d&rid=giphy.gif&ct=g)

##### - Con esfuerzo, no hay nada imposible

![N|Solid](https://media3.giphy.com/media/26ufirhvR4jQ1SOn6/giphy.gif?cid=ecf05e4740nv60dw6naihwxyqpdeo9rcgji2nx6hh8a70isj&rid=giphy.gif&ct=g)