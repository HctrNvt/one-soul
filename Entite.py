import pygame
from pygame.locals import *  # noqa: F403

entites = []


class Entite:
    def __init__(
        self, pointDeVie: int, vitesse: int, image, coordonnes: tuple, fenetre
    ):
        # Les attributs de la classs Entite
        self.fenetre = fenetre
        self.coordonnes = coordonnes
        self.corps = pygame.image.load(image).convert()
        self.rect = self.corps.get_rect()
        self.rect.topleft = (50, 50)
        # Infos joueur
        self.vie = pointDeVie
        self.vitesse = vitesse
        # On ajoute a la grande liste de toute les entités
        entites.append(self)
        self.dessiner(coordonnes)

    def dessiner(self, coordonnees: tuple):
        self.fenetre.blit(self.corps, (coordonnees[0], coordonnees[1]))
