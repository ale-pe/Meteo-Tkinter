import requests, json 
from tkinter import *
from tkinter.messagebox import *

#A remplir

#Lire README.MD pour avoir un API KEY
api_key = "Lire README.MD pour avoir un API KEY"
ville = "Paris"


url = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+ville+"&units=metric"

response = requests.get(url) 
  

x = response.json()


if x["cod"] != "404": 

    y = x["main"] 
    temp_actuelle = y["temp"] 
    temp_min = (y["temp_min"])
    temp_max = y["temp_max"]
    hum = y["humidity"]
    pres = y["pressure"]
    ventvitesse = x["wind"]["speed"]
    z = x["weather"]  
    description = z[0]["description"] 
    pays = x["sys"]["country"]


F = Tk()
F.title('Météo')
F['bg']='#40E0D0' 
affichage1 = StringVar()
affichage1.set("Météo à : "+ville+", "+pays )


F1 = Frame(F,bg="white",borderwidth=2,relief=GROOVE)
F1.pack(padx=10,pady=10)

Label(F1,textvariable=affichage1,bg="white").pack(padx=10,pady=10)

#########################

F2 = Frame(F,bg="white",borderwidth=2,relief=GROOVE)
F2.pack(padx=10,pady=10)

affichage2 = StringVar()
affichage2.set("Température actuelle : "+str(temp_actuelle)+"°C")
affichage3 = StringVar()
affichage3.set("Température minimale : "+str(temp_min)+"°C")
affichage4 = StringVar()
affichage4.set("Température maximale : "+str(temp_max)+"°C")

Label(F2,textvariable=affichage2,bg="white").pack(padx=10,pady=10)
Label(F2,textvariable=affichage3,bg="white").pack(padx=10,pady=10)
Label(F2,textvariable=affichage4,bg="white").pack(padx=10,pady=10)

#########################

F3 = Frame(F,bg="white",borderwidth=2,relief=GROOVE)
F3.pack(padx=10,pady=10)

affichage5 = StringVar()
affichage5.set("Pression : "+str(pres)+" hpa")
affichage6 = StringVar()
affichage6.set("Humidité : "+str(hum)+" %")
affichage7 = StringVar()
affichage7.set("Vitesse du vent : "+str(ventvitesse)+" m/s")
affichage8 = StringVar()
affichage8.set("Description : "+str(description))

Label(F3,textvariable=affichage5,bg="white").pack(padx=10,pady=10)
Label(F3,textvariable=affichage6,bg="white").pack(padx=10,pady=10)
Label(F3,textvariable=affichage7,bg="white").pack(padx=10,pady=10)
Label(F3,textvariable=affichage8,bg="white").pack(padx=10,pady=10)
