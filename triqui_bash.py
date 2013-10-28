"""········································································

                          Datos del Fichero
  [N]ombre del Archivo:         triqui_bash.py
  [N]ombre del Programa:        Tres en Linea
  [T]ipo de Programa:           Software de aplicacion (Juego)
  [L]enguaje Utilizado:         Python 2 (v2.7.3)
  [E]ditor Utilizado:           Sublime Text 2
  [A]utor:                      Emanuel Garcia Perez
  [U]bicacion:                  Cuernavaca, Morelos, Mexico
  [V]ersion:                    0.1
  [E]status:                    En Desarrollo
  [L]icencia:                   Licencia Publica General version 3 (GPLv3)

           Descripcion: |==============================================|
                        | Programa del juego "Tres en Linea(Raya)" que |
                        | permite a dos jugadores independientes       |
                        | jugarlo en una terminal de comandos.         |
                        |==============================================|

           Instrucciones: |--------------------------------------------|
                          |1) Los simbolos a utilizar para marcar las  |
                          |   casillas por cada jugador en su          |
                          |   respectivo turno seran <X> y <O>.        |
                          |--------------------------------------------|
                          |2) Cada jugador podra elegir unicamente     |
                          |   una casilla a marcar en su turno actual  |
                          |   y debera confirmar su eleccion antes de  |
                          |   que su oponente empieze su turno para    |
                          |   elegir y marcar alguna casilla.          |
                          |--------------------------------------------|
                          |3) La eleccion del jugador que iniciara la  |
                          |   partida se realizara de manera aleatoria.|
                          |--------------------------------------------|
                          |4) Para que a un jugador se le considere    |
                          |   como el ganador de la partida, debera    |
                          |   tener marcadas con su correspondiente    |
                          |   simbolo tres casillas continuas en linea |
                          |   horizontalmente, verticalmente o en      |
                          |   diagonal; a continuacion se muestran los |
                          |   patrones validos para que un jugador     |
                          |   gane la partida:                         |
                          |                                            |
                          |       |      |             |      |        |
                          |    *  |   *  |  *          |      |        |
                          | ______|______|______ ______|______|______  |
                          |       |      |             |      |        |
                          |       |      |          *  |   *  |   *    |
                          | ______|______|______ ______|______|______  |
                          |       |      |             |      |        |
                          |       |      |             |      |        |
                          |       |      |             |      |        |
                          |                                            |
                          |       |      |             |      |        |
                          |       |      |          *  |      |        |
                          | ______|______|______ ______|______|______  |
                          |       |      |             |      |        |
                          |       |      |          *  |      |        |
                          | ______|______|______ ______|______|______  |
                          |       |      |             |      |        |
                          |    *  |   *  |   *      *  |      |        |
                          |       |      |             |      |        |
                          |                                            |
                          |       |      |             |      |        |
                          |       |   *  |             |      |  *     |
                          | ______|______|______ ______|______|______  |
                          |       |      |             |      |        |
                          |       |   *  |             |      |  *     |
                          | ______|______|______ ______|______|______  |
                          |       |      |             |      |        |
                          |       |   *  |             |      |  *     |
                          |       |      |             |      |        |
                          |                                            |
                          |       |      |             |      |        |
                          |    *  |      |             |      |  *     |
                          | ______|______|______ ______|______|______  |
                          |       |      |             |      |        |
                          |       |   *  |             |   *  |        |
                          | ______|______|______ ______|______|______  |
                          |       |      |             |      |        |
                          |       |      |   *      *  |      |        |
                          |       |      |             |      |        |
                          |                                            |
                          |--------------------------------------------|
                          |5) La partida concluira cuando haya algun   |
                          |   ganador o bien no haya mas casillas a    |
                          |   marcar y se considere un empate entre    |
                          |   ambos contrincantes.                     |
                          |--------------------------------------------|

········································································"""

