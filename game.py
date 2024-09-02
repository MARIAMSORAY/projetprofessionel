import pygame
from gui import GUI
from ai import AI
from utils import random_blocked_cells

class Game:
    def __init__(self, mode):
        pygame.init()
        self.mode = mode
        self.gui = GUI()
        self.ai = AI()
        self.board = [[None for _ in range(5)] for _ in range(5)]
        self.current_player = 'X'  # 'X' ou 'O'
        self.blocked_cells = random_blocked_cells()

    def check_winner(self):
        # Implémentez la logique pour vérifier si un joueur a gagné
        for row in range(5):
            for col in range(5):
                if self.check_line(row, col):
                    return True
        return False

    def check_line(self, row, col):
        # Vérifiez les lignes, colonnes, et diagonales pour 4 symboles alignés
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 0
            for i in range(-3, 1):
                r, c = row + i * dr, col + i * dc
                if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True
        return False

    def handle_event(self, event):
        # Implémentez la gestion des événements pour les clics de souris et les tours de jeu
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = x // 100, y // 100  # Assurez-vous que la taille des cases correspond
            if self.board[row][col] is None and (row, col) not in self.blocked_cells:
                self.board[row][col] = self.current_player
                if self.check_winner():
                    print(f"{self.current_player} gagne!")
                    # Réinitialisez le jeu ou faites autre chose
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_event(event)
            self.gui.update_display(self.board, self.blocked_cells)
            # Appel à la méthode AI si c'est le tour de l'IA
            if self.current_player == 'O' and self.mode == 'AI':
                self.ai.make_move(self.board)
                self.current_player = 'X'
        pygame.quit()
