from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse # Importamos la libreria JSONResponse
from typing import Optional
import nltk

app = FastAPI() # crea una instancia de la clase FastAPI
app.title = "Mi primera aplicación" # definimos el titulo de la API
app.version = '0.0.1'


movies_list = [
    {"id": 1, 
     "title": "La lengua de las mariposas",
     "overview": "Un ejemplo de recuperación de la memoria histórica en el ámbito cinematográfico",
     "year": 2001,
     "rating": 9.5
      },
    {"id": 2,
     "title": "Las horas",
     "overview": "Vida y obra de la escritora Virginia Woolf",
     "year": 2024,
     "rating": 8.5
    },
    {"id": 3, 
     "title": "El señor de los anillos",
     "overview": "narra la historia de Frodo Bolsón, un hobbit que debe destruir el Anillo Único para impedir que Sauron, el Señor Oscuro, domine la Tierra Media",
     "year": 2001,
     "rating": 9.5
      },
    {"id": 4,
     "title": "La lista de Schindler",
     "overview": " narra la historia de Oskar Schindler, un empresario alemán que salvó a más de mil judíos polacos del Holocausto durante la Segunda Guerra Mundial.",
     "year": 2024,
     "rating": 8.5
    },
    {"id": 5, 
     "title": "12 hombres en pugna",
     "overview": " trata sobre el juicio de un homicidio en el que doce hombres tienen que deliberar sobre el futuro de un muchacho, dictaminando si es culpable o on",
     "year": 2001,
     "rating": 9.5
      },
    {"id": 6,
     "title": "El padre",
     "overview": "Un hombre rechaza la ayuda de su hija, a pesar de todo lo que ha envejecido",
     "year": 2024,
     "rating": 8.5
    },
    {"id": 7, 
     "title": "El código enigma",
     "overview": "Biopic sobre el matemático británico Alan Turing, famoso por haber descifrado los códigos secretos nazis contenidos en la máquina Enigma.",
     "year": 2014,
     "rating": 9.5
      },
    {"id": 8,
     "title": "Una mente brillante",
     "overview": "El genial matemático John Forbes Nash Jr. sufre de esquizofrenia, pero logra obtener el Premio Nobel de economía por su trabajo revolucionario en la teoría de juegos.",
     "year": 2001,
     "rating": 8.5
    },
    {"id": 9, 
     "title": "Las sufragistas",
     "overview": "Año 1912, las mujeres británicas llevan años reclamando pacíficamente el derecho al voto, pero siempre han sido ignoradas",
     "year": 2001,
     "rating": 9.5
      },
    {"id": 10,
     "title": "El poder del perro",
     "overview": "Los acaudalados hermanos Phil y George Burbank son las dos caras de la misma moneda. Phil es elegante y cruel, mientras que George es impasible y amable.",
     "year": 2024,
     "rating": 8.5
    },
    {"id": 11,
     "title": "Una peli cualquiera",
     "overview": "Los acaudalados hermanos Phil y George Burbank son las dos caras de la misma moneda. Phil es elegante y cruel, mientras que George es impasible y amable.",
     "year": 2024,
     "rating": 8.5
    }
]
@app.get('/', tags=["Mi Aplicacion"]) # definimos una ruta para la API utilizando el decorador @app.get
def message(): # def una funcion de la ruta
    return HTMLResponse ('<h1>Hello world</h1>') # Devolvemos un string en la respuesta de la ruta

@app.get('/movies', tags=["Movies"]) # definimos una ruta de la clase fast appi
def movies():
    return movies_list
@app.get('/movies/{id}', tags=["Movies"])#Definimos una ruta de la clase FastAPI
def get_movie(id: int):
    for item in movies_list:
        if item['id'] == id:
            return item
    return []
#Tokenizar
@app.post("/tokenize") # Decorador para indicar que es una ruta de la API
def tokenize(text:str): # Funcion que retorna un mensaje
    return preprocessar(text)

def preprocessar(text):
    import json  # Importamos la librería json para trabajar con archivos json
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('punkt')
    tokens = word_tokenize(text)
    result = {word: True for word in tokens}
    print(result)
    return JSONResponse(content={"message":result})