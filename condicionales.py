# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:57:44 2024

@author: jorge
"""
"""
Sistema de orientación vocacional

artes -> Teatro
deporte -> Medicina deportiva
matematicas -> Ingenieria

"""
"""
artes = False
deporte = False
matematicas = False

if artes == True :
    print("Estudia teatro")
elif deporte == True:
    print("Estudia medicina deportiva")
elif matematicas == True:
    print("Estudia ingenierias")
else:
    print("Consulta un asesor vocacional")
    
"""

"""
Club juvenil deportivo
"""
edad = int(input("Introduce tu edad: "))

if edad >= 12 and edad <= 14:
    print("Club juvenil A")
elif edad > 14 and edad <= 17:
      print("Club juvenil B")
elif  edad == 18:
       print("Club profesional")
else:
          print("Busca un club adecuado para tu edad")