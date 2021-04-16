# -*- coding: utf-8 -*-
import nltk
import numpy as np 
import random
import string
import urllib.request  # the lib that handles the url stuff
from inscriptis import get_text 

#https://computerhoy.com/reportajes/tecnologia/inteligencia-artificial-469917
default_url = "https://es.wikipedia.org/wiki/Inteligencia_artificial"
print("\nBOTY analizará una página web para aprender de ella.")
print("Actualmente la URL para el aprendizaje de BOTY es:",default_url)
print("Escriba '1' si desea continuar con la URL asiganada. De lo contrario, ingrese una nueva URL.")

while True:
    inp = input()

    if inp != "1":
        url = inp
    else:
        url = default_url

    try:
        html = urllib.request.urlopen(url).read(20000).decode('utf-8')    
        text = get_text(html) 
        raw = text.lower() #Pasa a todos los rows del archivo fuente de información a minusculas
        break
    except:
        print("La entrada no corresponde a un URL entendible para BOTY. Pruebe ingresar una similar a la ya asignada o presione '1' para continuar.")

nltk.download('punkt') #Solo usar una unica vez 
nltk.download('wordnet') #Solo usar una unica vez
nltk.download('stopwords')
stop_words_sp = set(nltk.corpus.stopwords.words('spanish'))

sent_tokens = nltk.sent_tokenize(raw) #Genera una lista de oraciones
word_tokens = nltk.word_tokenize(raw) #Genera una lista de palabras

#Se define la estructura o funcionalidad para obtener la raiz de las palabras
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
#Se eliminan los signos de puntuación 
del_puntuacion = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(del_puntuacion)))

SALUDOS = ("hola", "buenos dias", "buenas tardes", "buenas noches", "hey", "que tal",)
RESPUESTA_SALUDOS = ["hola", "hola, ¿como estas?", "hey", "buen dia", "¿en que puedo ayudarte?"]

#Verificación de saludos
def saludo(oracion):
    """Si el usuario saluda, Boty retorna una repuesta de saludo"""
    for word in oracion.split():
        if word.lower() in SALUDOS:
            return random.choice(RESPUESTA_SALUDOS)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Función que genera las respuestas del bot
def repuesta(respuesta_usr):
    respuesta_boty=''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=stop_words_sp)
    tfidf= TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        respuesta_boty = respuesta_boty+"Lo siento, no te comprendo"
        return respuesta_boty
    else:
        respuesta_boty = respuesta_boty+sent_tokens[idx]
        return respuesta_boty

flag = True
print("\nBOTY: Hola, mi nombre es Boty. Contestare todas tus preguntas sobre los juegos olimpicos, si deseas salir escribe adios")
print("(Sugerencias) Prueba decir 'Hola' y/o una palabra relacionada con la página web.")

while(flag==True):
    respuesta_usr = input()
    respuesta_usr = respuesta_usr.lower()
    if(respuesta_usr!='adios'):
        if(respuesta_usr=='gracias' or respuesta_usr=='gracias a usted'):
            flag=False
            print("BOTY: Bienvenido(a)..")
        else:
            if(saludo(respuesta_usr)!=None):
                print("BOTY: "+saludo(respuesta_usr))
            else:
                sent_tokens.append(respuesta_usr)
                word_tokens = word_tokens+nltk.word_tokenize(respuesta_usr)
                palabras_finales = list(set(word_tokens))
                print("BOTY: ",end="")
                print(repuesta(respuesta_usr))
                sent_tokens.remove(respuesta_usr)
    else:
        flag = False
        print("BOTY: ¡Hasta pronto! que tenga un buen dia..")

#referencia: https://youtu.be/K4kSXeLRvY4