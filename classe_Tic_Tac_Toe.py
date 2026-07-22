#
# File: classe_Tic_Tac_Toe.py
#
# Author: M. Battiston
#
# Version: 1.0
#
# Description: Classe per gestire la logica del gioco del Tris (TicTacToe):
#              controllo delle mosse, cambio turno, verifica della vittoria e pareggio.
#

class TicTacToe:
    '''Classe che rappresenta e gestisce una partita a Tris (TicTacToe)'''
    def __init__(self, giocatore_iniziale):
        '''Inizializza la griglia di gioco 3x3 e imposta il giocatore di partenza.'''
        self.tabella = [[' ', ' ', ' '],
                        [' ', ' ', ' '],
                        [' ', ' ', ' ']]
        
        self.giocatore_corrente = giocatore_iniziale

    def mossa(self, riga, colonna):
        '''Verifica la validità di una mossa ed esegue l'inserimento del simbolo'''

        if colonna < 0 or colonna > 3 or riga < 0 or riga > 3:
            print('Posizione non valida: fuori dalla tabella.')
            return False
        elif self.tabella[riga][colonna] == ' ':
            self.tabella[riga][colonna] = self.giocatore_corrente
            return True
        else:
            print('Casella già occupata')
            return False

    def cambio_giocatore(self):
        '''Scambia giocatore'''

        if self.giocatore_corrente == 'X':
            self.giocatore_corrente = 'O'
        else:
            self.giocatore_corrente = 'X'

    def controlla_vittoria(self):
        '''Controlliamo le condizione di vittoria'''
        
        giocatore = self.giocatore_corrente
        
        for i in range(3):
            if self.tabella[0][i] == self.tabella[1][i] == self.tabella[2][i] == giocatore:
                return True                             # Stop se le righe sono piene
        
        for j in range(3):
            if self.tabella[j][0] == self.tabella[j][1] == self.tabella[j][2] == giocatore:
                return True                             # Stop se le righe sono piene
        
        if self.tabella[0][0] == self.tabella[1][1] == self.tabella[2][2] == giocatore:
            return True                                 # Stop se la diagonale principale è piena
    
        if self.tabella[0][2] == self.tabella[2][2] == self.tabella[2][0] == giocatore:
            return True                                 # Stop se la diagonale secondaria è piena
    
        return False
        
    def tabella_piena(self):
        '''Controlliamo se la tabella è piena'''
        for rig in self.tabella:
            for casella in rig:
                if casella  == ' ':
                    return False            # La tabella non è piena 
        return True                       # Tabella piena, non ci sono spazi vuoti 

    def stampa_tabella(self):
        '''Mostriamo la griglia nel terminale'''
        print('\n     0   1   2 ')
        print()
 
        for i in range(3):
            r0 = str(self.tabella[i][0])
            r1 = str(self.tabella[i][1])
            r2 = str(self.tabella[i][2])

            print(f'{i}    {r0} | {r1} | {r2}')

            if i < 2:
                print('    -----------')

        print()