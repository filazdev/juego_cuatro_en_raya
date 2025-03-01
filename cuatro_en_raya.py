import os
import time

class CuatroEnRaya:
    def __init__(self,filas = 6,columnas = 7):
        self._filas = filas
        self._columnas = columnas
        self._tablero = self._crear_tablero()
        self._turno = None

    def _crear_tablero(self):
        tablero = [["." for _ in range(self._columnas)]for _ in range(self._filas)]
        return tablero

    def _mostrar_tablero(self):
        #Se muestra cabecera
        for num in range(self._columnas):
            print(f"{num:1}",end="  ")
        print()
        for fila in self._tablero:
            for elemento in fila:
                print(f"{elemento:2}",end=" ")
            print()

    def _introducir_ficha(self,columna,color):
        '''Introduce ficha en el tablero'''
        if columna >= self._columnas or columna < 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERROR: número fuera de rango, intente de nuevo")
            time.sleep(2)
            
            return False
        elif self._tablero[0][columna] != '.':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERROR: La columna no tiene espacios disponibles, seleccione otra columna.")
            time.sleep(3)
            
            return False
        else:
            for fila in range(self._filas-1,-1,-1):
                if self._tablero[fila][columna] == '.':
                    self._tablero[fila][columna] = color
                    
                    return True
        os.system('cls' if os.name == 'nt' else 'clear')
        print("ERROR: No se pudo introducir la ficha")
        time.sleep(2)
        return False

    def _revisar_filas(self,color):
        for f in range(self._filas):
            for c in range(self._columnas-3):
                if (
                    self._tablero[f][c] == color and
                    self._tablero[f][c+1] == color and
                    self._tablero[f][c+2] == color and
                    self._tablero[f][c+3] == color
                    ):
                    return True
        return False

    def _revisar_columnas(self,color):
        for c in range(self._columnas):
            for f in range(self._filas -3):
                if (
                    self._tablero[f][c] == color and
                    self._tablero[f+1][c] == color and
                    self._tablero[f+2][c] == color and
                    self._tablero[f+3][c] == color
                ):
                    return True
        return False

    def _revisar_diagonales_ascedentes(self,color):
        for f in range(3, self._filas):
            for c in range(self._columnas - 3):
                if (
                    self._tablero[f][c] == color and
                    self._tablero[f-1][c+1] == color and
                    self._tablero[f-2][c+2] == color and
                    self._tablero[f-3][c+3] == color
                ):
                    return True
        return False

    def _revisar_diagonales_descendentes(self,color):
        for f in range(self._filas - 3):
            for c in range(self._columnas - 3):
                if (
                    self._tablero[f][c] == color and
                    self._tablero[f+1][c+1] == color and
                    self._tablero[f+2][c+2] == color and
                    self._tablero[f+3][c+3] == color
                ):
                    return True
        return False

    def _comprobar_ganador(self,color):
        return (self._revisar_filas(color) or 
                self._revisar_columnas(color)or
                self._revisar_diagonales_descendentes(color)or
                self._revisar_diagonales_ascedentes(color))

    def jugar(self,player1 ='O',player2 = 'X'):
        self._turno = player2
        while True:
            self._turno = player1 if self._turno == player2 else player2
            os.system('cls' if os.name == 'nt' else 'clear')
            self._mostrar_tablero()
            try:
                columna = int(input(f"\nTurno del jugador con la ficha \"{self._turno}\"\nIngrese el número de columna: "))
            except Exception as e:
                self._turno = player1 if self._turno == player2 else player2
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"ERROR: El valor ingresado no es válido intente de nuevo.")
                time.sleep(3)
                continue
            if self._introducir_ficha(columna,self._turno):
                if self._comprobar_ganador(self._turno):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"¡Felicidades! ha ganado el jugador de la ficha \"{self._turno}\"\n")
                    self._mostrar_tablero()
                    print()
                    print("Presione cualquier tecla para salir...")
                    input()
                    break
            else:
                self._turno = player1 if self._turno == player2 else player2
                
juego = CuatroEnRaya()
juego.jugar()


