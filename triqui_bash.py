# -*- coding: utf-8 -*-

"""-----------------------------------------------------------------------------
                          Datos del Fichero
  [N]ombre del Archivo:         triqui_bash.py
  [N]ombre del Programa:        Tres en Linea
  [T]ipo de Programa:           Software de aplicacion (Juego)
  [L]enguaje Utilizado:         Python 2 (v2.7)
  [A]utor:                      Emanuel García Pérez
  [U]bicacion:                  Cuernavaca, Morelos, Mexico
  [V]ersion:                    0.3
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
    self.nombre = 'Tres en Línea'
    self.version = '0.3'
    self.condificacion = 'UTF-8'
    self.autor = 'Emanuel GP'
    self.estatus = 'En Desarrollo'
    self.licencia = 'GPLv3'

     # Variables/Constantes dinamicas del programa.
    self.simbolos = ('X', 'O')
    self.turno = 0
    self.casillas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    self.tablero = """
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
    print "Nombre del Programa:         ", self.nombre
    print "Version Actual:              ", self.version
    print "Codificación Utilizada:      ", self.condificacion
    print "Estatus del Programa         ", self.estatus
    print "Licencia del Programa:       ", self.licencia
    print "Autor del Programa:          ", self.autor

  def dibuja_tablero(self):
    """ Método que dibuja en pantalla el tablero del juego. """
    print self.tablero % (self.casillas[0], self.casillas[1], self.casillas[2],
                          self.casillas[3], self.casillas[4], self.casillas[5],
                          self.casillas[6], self.casillas[7], self.casillas[8])

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
      self.turno = valor1
    elif type(valor1) == str:
      indice = self.casillas.index(valor2)
      self.casillas[indice] = valor1

  def verifica_estado_actual_tablero(self, jugador, casilla):
    """ Método que verifica el estado actual del tablero para cotejar si hay algún ganador, un 
        empate o si hay casillas libres aún en el tablero para continuar la partida. """
    estado = ""
    if casilla == 'A':
      if (self.casillas[0]==jugador and self.casillas[1]==jugador and self.casillas[2]==jugador) or \
         (self.casillas[0]==jugador and self.casillas[3]==jugador and self.casillas[6]==jugador) or \
         (self.casillas[0]==jugador and self.casillas[4]==jugador and self.casillas[8]==jugador):
         estado = "GANADOR"
    elif casilla == 'B':
      if (self.casillas[0]==jugador and self.casillas[1]==jugador and self.casillas[2]==jugador) or \
         (self.casillas[1]==jugador and self.casillas[4]==jugador and self.casillas[7]==jugador):
         estado = "GANADOR"
    elif casilla == 'C':
      if (self.casillas[0]==jugador and self.casillas[1]==jugador and self.casillas[2]==jugador) or \
         (self.casillas[2]==jugador and self.casillas[4]==jugador and self.casillas[6]==jugador) or \
         (self.casillas[2]==jugador and self.casillas[5]==jugador and self.casillas[8]==jugador):
         estado = "GANADOR"
    elif casilla == 'D':
      if (self.casillas[0]==jugador and self.casillas[3]==jugador and self.casillas[6]==jugador) or \
         (self.casillas[3]==jugador and self.casillas[4]==jugador and self.casillas[5]==jugador):
        estado = "GANADOR"
    elif casilla == 'E':
      if (self.casillas[0]==jugador and self.casillas[4]==jugador and self.casillas[8]==jugador) or \
         (self.casillas[1]==jugador and self.casillas[4]==jugador and self.casillas[7]==jugador) or \
         (self.casillas[2]==jugador and self.casillas[4]==jugador and self.casillas[6]==jugador) or \
         (self.casillas[3]==jugador and self.casillas[4]==jugador and self.casillas[5]==jugador):
        estado = "GANADOR"
    elif casilla == 'F':
      if (self.casillas[2]==jugador and self.casillas[5]==jugador and self.casillas[8]==jugador) or \
         (self.casillas[3]==jugador and self.casillas[4]==jugador and self.casillas[5]==jugador):
        estado = "GANADOR"
    elif casilla == 'G':
      if (self.casillas[0]==jugador and self.casillas[3]==jugador and self.casillas[6]==jugador) or \
         (self.casillas[2]==jugador and self.casillas[4]==jugador and self.casillas[6]==jugador) or \
         (self.casillas[6]==jugador and self.casillas[7]==jugador and self.casillas[8]==jugador):
        estado = "GANADOR"
    elif casilla == 'H':
      if (self.casillas[1]==jugador and self.casillas[4]==jugador and self.casillas[7]==jugador) or \
         (self.casillas[6]==jugador and self.casillas[7]==jugador and self.casillas[8]==jugador):
        estado = "GANADOR"
    elif casilla == 'I':
      if (self.casillas[0]==jugador and self.casillas[4]==jugador and self.casillas[8]==jugador) or \
         (self.casillas[2]==jugador and self.casillas[5]==jugador and self.casillas[8]==jugador) or \
         (self.casillas[6]==jugador and self.casillas[7]==jugador and self.casillas[8]==jugador):
        estado = "GANADOR"
    if estado != "":
      return (jugador, estado)
    else:
      for item in self.casillas:
        if item=='X' or item=='O':
          continue
        else:
          return True
      return False

  def comprueba_jugada(self, casilla, casillas):
    """ Método que verifica si el jugador en turno eligio una casilla 
        valida del tablero para marcar. """
    for item in casillas:
      if casilla == item:
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
            print "Turno del jugador [%s]." % (self.simbolos[self.turno])
            jugada = raw_input("Digita la letra de la casilla a marcar"+
                                "(escribe <S> para salir de la partida): ")
            jugada = jugada.upper()
            if self.turno == 0 and (jugada == "X" or jugada == "O"):
              jugada = "Z"
            elif self.turno == 1 and (jugada == "X" or jugada == "O"):
              jugada = "Z"
            if jugada == "S":
              self.casillas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
              break
            else:
              valor_jugada = self.comprueba_jugada(jugada, self.casillas)
              if valor_jugada:
                self.actualiza_valores(self.simbolos[self.turno], jugada)
                if self.turno == 0:
                  self.turno = 1
                else:
                  self.turno = 0
              estado_actual = self.verifica_estado_actual_tablero(self.simbolos[self.turno], jugada)
              if type(estado_actual) == tuple:
                print "\n >> JUEGO TERMINADO  <<"
                print " %s: %s\n" % (estado_actual[1], estado_actual[0])
                continuar = raw_input("\nPresione <Enter> para continuar...")
                break 
              elif estado_actual:
                print "\n\tPartida en juego..."
              else:
                print "\n >> JUEGO TERMINADO  <<"
                print "\t EMPATE..."
                continuar = raw_input("\nPresione <Enter> para continuar...")
                break 
        elif opcion == "2":
          os.system("clear")
          self.datos()
          continuar = raw_input("\nPresione <Enter> para continuar...")
        elif opcion == "3":
          os.system("clear")
          break



if __name__ == '__main__':
  triqui = TriquiPython()
  triqui.main()
  exit(0)








