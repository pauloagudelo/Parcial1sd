# -*- coding: utf-8 -*-

import json
import time
import os

peliculas=list()
peliculas_1=list()
sillas=list()

def menu():
    lista = ["Bienvenido al Cinema", "1. Crear Peliculas", "2. Eliminar Peliculas", "3. Listar Peliculas", "4. Ver Peliculas",
             "5. Sillas Disponible", "6. Salir", "Digite la opción >>"]
    cadena = json.dumps(lista)
    return cadena

def menu_1():
    lista = ["Bienvenido al Cinema", "1. Listar Peliculas", "2. Comprar Entradas",
             "3. Ver Pelicula", "4. Salir", "Digite la opción >>"]
    cadena = json.dumps(lista)
    return cadena

def usuarios():
    lista = ["Ingrese usuario y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def validar_usuario(cadena):
    if(cadena == "fernando"):
        return True
    else:
        return False

def crear_pelicula(nombre,costo,silla):

    hora = time.strftime("%X")
    pelicula1=[nombre, costo, silla, hora]
    peliculas.append(pelicula1)
    silla1=[silla]
    sillas.append(silla1)
    lista=["Pelicula Creada Exitosamnete ", "presione enter para volver al menu"]
    cadena = json.dumps(lista)
    return cadena

def comprar(nombre,cliente,cedula):

    hora = time.strftime("%X")
    pelicula1=[nombre, cliente, cedula, hora]
    peliculas_1.append(pelicula1)
    lista=["Pelicula Comprada Exitosamnete ", "presione enter para volver al menu"]
    cadena = json.dumps(lista)
    return cadena

def imprimir_pelicula():
    lista = peliculas
    lista.append('\n'+ "Escoja pelicula a eliminar y presione entrer")
    cadena = json.dumps(lista)
    return cadena

def listar_pelicula():
    lista = peliculas
    lista.append("presione entrer para volver al menu")
    cadena = json.dumps(lista)
    return cadena

def listar_pelicula_1():
    lista = peliculas_1
    lista.append("presione entrer para volver al menu")
    cadena = json.dumps(lista)
    return cadena

def listar_silla():
    lista = sillas
    lista.append(" Sillas disponibles, presione entrer para volver al menu")
    cadena = json.dumps(lista)
    return cadena

def eliminar_pelicula(pelicula):
    peliculas.pop(pelicula)
    lista = ["Pelicula Eliminada Exitosamnete ", "presione enter para volver al menu"]
    cadena = json.dumps(lista)
    return cadena

def getnum_3():
    lista = ["Ingrese # pelicula a eliminar y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def getnum_1():
    lista = ["Ingrese el nombre y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def getnum_2():
    lista = ["Ingrese el costo y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def getnum_3():
    lista = ["Ingrese el # silla y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def getnum_4():
    lista = ["Ingrese el nombre y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def getnum_5():
    lista = ["Ingrese el cliente y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def getnum_6():
    lista = ["Ingrese el # cedula y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena


