import Entite


class Monstre(Entite):
    def __init__(
        self,
        pointDeVie: int,
        vitesse: int,
        image,
        coordonnes: tuple,
        fenetre,
        attaque: int,
    ):
        super().__init__(pointDeVie, vitesse, image, coordonnes, fenetre)
        self.attaque = attaque

    # def attaqueJoueur(self, cible: Joueur):
    #    cible.vie -= self.attaque
    #    # à faire
    #    pass

    def deplacer(self, fenetre, newPosition: tuple):
        # à faire
        pass

    def deplacerVers(self, coordonnees: tuple):
        # à faire
        pass
