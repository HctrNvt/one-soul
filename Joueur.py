import pygame


class Joueur:
    def __init__(
        self, pointDeVie: int, velocity: int, image, coordonnes: tuple, fenetre
    ):
        # Les attributs de la classs Entite
        self.fenetre = fenetre
        self.coordonnes = coordonnes
        self.corps = pygame.image.load(image).convert()
        self.rect = self.corps.get_rect()
        self.rect.topleft = (50, 50)
        # Infos joueur
        self.vie = pointDeVie
        self.velocity = velocity

    def move_right(self):
        self.rect.x += velocity

    def move_left(self):
        self.rect.x -= velocity

    def move_up(self):
        self.rect.y -= velocity

    def move_down(self):
        self.rect.y += velocity

    def checkMouvement(self, key):
        if key == pygame.K_q or key == pygame.K_LEFT:
            # On bouge à gauche
            self.move_left()
        if key == pygame.K_d or key == pygame.K_RIGHT:
            # On bouge à droite
            self.move_right()
        if key == pygame.K_z or key == pygame.K_UP:
            self.move_up()
        if key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
