# -*- coding: utf-8 -*-

from socket import socket, error
from threading import Thread
import funciones_servidor2
import json


class Cliente(Thread):

    '''funcion que genera hilos'''
    def __init__(self, con, dire):
        Thread.__init__(self)
        self.conexion = con
        self.direccion= dire


    def run(self):
        while True:
            try:
                a=False
                b=False
                while (a!= True):
                    while (b!=True):
                        mensaje_cliente=self.conexion.recv(1024)
                        mensaje_cliente = funciones_servidor2.validar_usuario(mensaje_cliente)
                        usuario=mensaje_cliente
                        menu = False
                        b=True
                    while (usuario == True):
                        while (menu != True):
                            mensaje_cliente=funciones_servidor2.menu()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            operacion=mensaje_cliente
                            if operacion ==1 :
                                mensaje_cliente = funciones_servidor2.getnum_1()
                                self.conexion.send(mensaje_cliente)
                                num_1 = str(self.conexion.recv(1024))
                                mensaje_cliente = funciones_servidor2.getnum_2()
                                self.conexion.send(mensaje_cliente)
                                num_2 = int(self.conexion.recv(1024))
                                mensaje_cliente = funciones_servidor2.getnum_3()
                                self.conexion.send(mensaje_cliente)
                                num_3 = str(self.conexion.recv(1024))
                                mensaje_cliente = funciones_servidor2.crear_pelicula(num_1,num_2,num_3)
                                self.conexion.send(mensaje_cliente)

                            if operacion ==2:

                                mensaje_cliente = funciones_servidor2.imprimir_pelicula()
                                self.conexion.send(mensaje_cliente)
                                num_2 = int(self.conexion.recv(1024))
                                mensaje_cliente = funciones_servidor2.eliminar_pelicula(num_2)
                                self.conexion.send(mensaje_cliente)

                            if operacion == 3:

                                mensaje_cliente = funciones_servidor2.listar_pelicula()
                                self.conexion.send(mensaje_cliente)

                            if operacion == 4:
                                mensaje_cliente = funciones_servidor2.listar_pelicula_1()
                                self.conexion.send(mensaje_cliente)

                            if operacion == 5:
                                mensaje_cliente = funciones_servidor2.listar_silla()
                                self.conexion.send(mensaje_cliente)

                            if operacion == 6:
                                mensaje_cliente=funciones_servidor2.usuarios()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = self.conexion.recv(1024)
                                mensaje_cliente = funciones_servidor2.validar_usuario(mensaje_cliente)
                                menu= True
                                usuario= False

                    menu_1=False
                    while (menu_1!= True):
                        mensaje_cliente = funciones_servidor2.menu_1()
                        self.conexion.send(mensaje_cliente)
                        mensaje_cliente = int(self.conexion.recv(1024))
                        operacion = mensaje_cliente

                        if operacion == 1:
                            mensaje_cliente = funciones_servidor2.listar_pelicula()
                            self.conexion.send(mensaje_cliente)

                        if operacion == 2:
                            mensaje_cliente = funciones_servidor2.getnum_4()
                            self.conexion.send(mensaje_cliente)
                            num_1 = str(self.conexion.recv(1024))
                            mensaje_cliente = funciones_servidor2.getnum_5()
                            self.conexion.send(mensaje_cliente)
                            num_2 = str(self.conexion.recv(1024))
                            mensaje_cliente = funciones_servidor2.getnum_6()
                            self.conexion.send(mensaje_cliente)
                            num_3 = int(self.conexion.recv(1024))
                            mensaje_cliente = funciones_servidor2.comprar(num_1,num_2,num_3)
                            self.conexion.send(mensaje_cliente)

                        if operacion == 3:
                            mensaje_cliente = funciones_servidor2.listar_pelicula_1()
                            self.conexion.send(mensaje_cliente)

                        if operacion == 4:
                            mensaje_cliente = funciones_servidor2.usuarios()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = self.conexion.recv(1024)
                            menu_1 = True
                            usuario=True
                            menu= False



            except error:
                print("[%s] Error de lectura "%self.name)
                break
            else:
                if mensaje_cliente:
                    self.conexion.send(mensaje_cliente)



def main():
    server = socket()
    server.bind(("localhost", 9090))
    server.listen(1)


    while True:
        con, dire = server.accept()
        hilo= Cliente(con, dire)
        hilo.start()
        print("conexion de %s:%d " %dire)
        #hilo =Thread(target=funciones_servidor2.menu,args=())
        #hilo.start()

if __name__ == '__main__':
    main()

