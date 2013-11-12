# -*- coding: utf-8 -*-

"""-----------------------------------------------------------------------------
                          Datos del Fichero
  [N]ombre del Archivo:         triqui_bash.py
  [N]ombre del Programa:        Tres en Linea
  [T]ipo de Programa:           Software de aplicacion (Juego)
  [L]enguaje Utilizado:         Python 2 (v2.7)
  [A]utor:                      Emanuel García Pérez
  [U]bicacion:                  Cuernavaca, Morelos, Mexico
  [V]ersion:                    0.2
  [E]status:                    En Desarrollo
  [L]icencia:                   Licencia Publica General version 3 (GPLv3)

           Descripcion: |==============================================|
                        | Programa del juego "Tres en Linea(Triqui)"   |
                        | que permite a dos jugadores independientes   |
                        | jugarlo en una terminal de comandos.         |
                        |==============================================|
-----------------------------------------------------------------------------"""



 # Modulos importados.
import os
import random

class TriquiPython:
    """ Juego Triqui (Tres en Línea, Tres en Raya, Gato) en consola. """

    def __init__(self):
         # Constantes estaticas del programa.
        self.__nombre = 'Tres en Línea'
        self.__version = '0.2'
        self.__codificacion = 'UTF-8'
        self.__autor = 'Emanuel GP'
        self.__estatus = 'En Desarrollo'
        self.__licencia = 'GPLv3'

         # Variables/Constantes dinamicas del programa.
        self.__simbolos = ('X', 'O')
        self.__turno = 0
        self.__casillas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.__tablero = """
                                 |     |
                              %s  |  %s  |  %s
                            _____|_____|_____
                                 |     |
                              %s  |  %s  |  %s
                            _____|_____|_____
                                 |     |
                              %s  |  %s  |  %s
                                 |     |
                         """

    def datos(self):
        """ Método que muestra en pantalla los datos del programa. """
        print "\t\tAcerca de...\n"
        print "Nombre del Programa:         ", self.__nombre
        print "Version Actual:              ", self.__version
        print "Codificación Utilizada:      ", self.__codificacion
        print "Estatus del Programa         ", self.__estatus
        print "Licencia del Programa:       ", self.__licencia
        print "Autor del Programa:          ", self.__autor

    def dibuja_tablero(self):
        """ Método que dibuja en pantalla el tablero del juego. """
        print self.__tablero % (
                                self.__casillas[0],
                                self.__casillas[1],
                                self.__casillas[2],
                                self.__casillas[3],
                                self.__casillas[4],
                                self.__casillas[5],
                                self.__casillas[6],
                                self.__casillas[7],
                                self.__casillas[8],
                                )

    def selecciona_jugador_inicial(self):
        """ Método que selecciona 'aleatoriamente' el jugador que iniciará la
            partida actual. """
        aleatorio = random.randint(1,100)
        if aleatorio%2 == 0:
            self.actualiza_valores(0)
        else:
            self.actualiza_valores(1)

    def actualiza_valores(self, valor1=None, valor2=None):
        """ Método que actualiza los valores de las variables que controlan
            el flujo del juego. """
        if type(valor1) == int:
            self.__turno = valor1
        elif type(valor1) == str:
            indice = self.__casillas.index(valor2)
            self.__casillas[indice] = valor1

    def verifica_estado_actual_tablero(self):
        """ Método que verifica el estado actual del tablero para cotejar si hay
            algún ganador, un empate o si hay casillas libres aún en el tablero
            para continuar la partida. """
        pass

    def comprueba_jugada(self, valor, lista):
      """ Método que verifica si el jugador en turno eligio una casilla 
          valida del tablero para marcar. """
      for item in lista:
        if valor == item:
            return True
      return False

    def main(self):
        """ Método principal del programa que controla el flujo del juego. """
        while True:
            os.system("clear")
            print "\t\tTres en Línea\n"
            print "[1] Iniciar partida"
            print "[2] Información del programa"
            print "[3] Salir"
            opcion = raw_input("Ingresa una opción para continuar: ")

            if opcion == "1":
                jugada = "primera"
                while True:
                    os.system("clear")
                    self.dibuja_tablero()
                    if jugada == "primera":
                        self.selecciona_jugador_inicial()
                    print "Turno del jugador [%s]." % (self.__simbolos
                                                      [self.__turno])
                    jugada = raw_input("Digita la letra de la casilla a marcar"+
                                        "(escribe <S> para salir de la "+
                                         "partida): ")
                    jugada = jugada.upper()
                    if self.__turno == 0 and (jugada == "X" or jugada == "O"):
                        jugada = "Z"
                    elif self.__turno == 1 and (jugada == "X" or jugada == "O"):
                        jugada = "Z"
                    if jugada == "S":
                        self.__casillas = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                                           'H', 'I']
                        break
                    else:
                        valor_jugada = self.comprueba_jugada(
                                                              jugada,
                                                              self.__casillas,
                                                            )
                        if valor_jugada:
                            self.actualiza_valores(self.__simbolos
                                                   [self.__turno],
                                                   jugada,
                                                   )
                            if self.__turno == 0:
                                self.__turno = 1
                            else:
                                self.__turno = 0
            elif opcion == "2":
                os.system("clear")
                self.datos()
                continuar = raw_input("\nPresione <Enter> para continuar..")
            elif opcion == "3":
                os.system("clear")
                break
        exit(0)



if __name__ == '__main__':
    triqui = TriquiPython()
    triqui.main()









