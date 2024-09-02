import pygame
from game import Game
from gui import GUI

def main():
    pygame.init()
    gui = GUI()
    mode = gui.show_main_menu()  # Obtenez le mode de jeu choisi par l'utilisateur
    game = Game(mode)
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
