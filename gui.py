import pygame
import sys

class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Morpion Avancé")

    def draw_button(self, text, x, y, width, height, color, hover_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        # Vérifiez si la souris est sur le bouton
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, hover_color, (x, y, width, height))
            if click[0] == 1:  # Clic gauche
                return True
        else:
            pygame.draw.rect(self.screen, color, (x, y, width, height))
        
        font = pygame.font.SysFont(None, 55)
        text_surf = font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surf, (x + (width / 2 - text_surf.get_width() / 2), y + (height / 2 - text_surf.get_height() / 2)))
        
        return False

    def show_main_menu(self):
        while True:
            self.screen.fill((255, 255, 255))  # Arrière-plan blanc
            
            # Boutons
            if self.draw_button("IA VS V1", 300, 200, 200, 60, (0, 200, 0), (0, 255, 0)):
                return 'AI'
            if self.draw_button("V1 VS V2", 300, 300, 200, 60, (0, 0, 200), (0, 0, 255)):
                return 'Adversaire'
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def update_display(self, board, blocked_cells):
        self.screen.fill((255, 255, 255))  # Arrière-plan blanc
        font = pygame.font.SysFont(None, 55)
        
        # Dessin du plateau
        for row in range(5):
            for col in range(5):
                rect = pygame.Rect(col * 100, row * 100, 100, 100)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
                if board[row][col] == 'X':
                    pygame.draw.line(self.screen, (255, 0, 0), rect.topleft, rect.bottomright, 2)
                    pygame.draw.line(self.screen, (255, 0, 0), rect.bottomleft, rect.topright, 2)
                elif board[row][col] == 'O':
                    pygame.draw.circle(self.screen, (0, 0, 255), rect.center, 40, 2)
        
        # Dessin des cases bloquées
        for (row, col) in blocked_cells:
            rect = pygame.Rect(col * 100, row * 100, 100, 100)
            pygame.draw.rect(self.screen, (128, 128, 128), rect)
        
        pygame.display.update()
