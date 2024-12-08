import pygame
import sys

# Définir les paramètres de la grille
GRID_SIZE = 15  # Taille de la grille (15x15 cases)
CELL_SIZE = 40  # Taille d'une case en pixels
MARGIN = 20  # Marge autour de la grille
SCREEN_SIZE = (GRID_SIZE * CELL_SIZE + 2 * MARGIN, GRID_SIZE * CELL_SIZE + 2 * MARGIN)

# Créer une liste de mots (simplifiée pour l'exemple)
words = [
    {"word": "ANTICYTHERE", "clue": "Premier ancêtre des ordinateurs (calculs astronomiques)", "x": 0, "y": 0, "orientation": "H"},
    {"word": "PASCAL", "clue": "Inventeur de la Pascaline", "x": 0, "y": 2, "orientation": "H"},
    {"word": "TURING", "clue": "Théoricien de la calculabilité", "x": 2, "y": 0, "orientation": "V"},
    {"word": "COLOSSUS", "clue": "Machine ayant cassé le code Lorenz", "x": 4, "y": 1, "orientation": "H"},
]

# Initialisation de pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Jeu de mots croisés")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (50, 50, 255)

# Police
font = pygame.font.Font(None, 24)

# Fonction pour dessiner la grille
def draw_grid():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(MARGIN + x * CELL_SIZE, MARGIN + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

# Fonction pour placer les mots dans la grille
def place_words():
    for word_data in words:
        word = word_data["word"]
        x, y = word_data["x"], word_data["y"]
        orientation = word_data["orientation"]
        for i, char in enumerate(word):
            cell_x = x + i if orientation == "H" else x
            cell_y = y if orientation == "H" else y + i
            rect = pygame.Rect(
                MARGIN + cell_x * CELL_SIZE,
                MARGIN + cell_y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, BLUE, rect)  # Case colorée
            text = font.render(char, True, WHITE)
            screen.blit(
                text,
                (MARGIN + cell_x * CELL_SIZE + 10, MARGIN + cell_y * CELL_SIZE + 10),
            )

# Fonction principale
def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_grid()
        place_words()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
