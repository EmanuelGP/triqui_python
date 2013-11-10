# -*- coding: utf-8 -*-

"""-----------------------------------------------------------------------------
                          Datos del Fichero
  [N]ombre del Archivo:         triqui_bash.py
  [N]ombre del Programa:        Tres en Linea
  [T]ipo de Programa:           Software de aplicacion (Juego)
  [L]enguaje Utilizado:         Python 2 (v2.7.3)
  [E]ditor Utilizado:           Sublime Text 2
  [A]utor:                      Emanuel García Pérez
  [U]bicacion:                  Cuernavaca, Morelos, Mexico
  [V]ersion:                    0.1
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

class TriquiPython:
    """ Juego Triqui (Tres en Línea, Tres en Raya, Gato) en consola. """

    def __init__(self):

         # Constantes estaticas del programa.
        self.__nombre = 'Tres en Línea' 
        self.__version = '0.1' 
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
        pass 

    def dibuja_tablero(self):
        """ Método que dibuja en pantalla el tablero del juego. """
        pass 

    def selecciona_jugador_inicial(self):
        """ Método que selecciona 'aleatoriamente' el jugador que iniciará la 
            partida actual. """
        pass 

    def actualiza_valores(self):
        """ Método que actualiza los valores de las variables que controlan 
            el flujo del juego. """
        pass 

    def verifica_estado_actual_tablero(self):
        """ Método que verifica el estado actual del tablero para cotejar si hay
            algún ganador, un empate o si hay casillas libres aún en el tablero 
            para continuar la partida. """
        pass 

    def main(self):
        """ Método principal del programa que controla el flujo del juego. """
        pass 




if __name__ == '__main__':
    pass 