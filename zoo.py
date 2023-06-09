#Définition de la classe Zoo

from animal import Animal


class Zoo:

    def __init__(self,liste_nouveaux_animaux): #liste_animaux est une liste d'un ou plusieurs animaux
        liste_animaux = []
        self.liste_animaux = liste_animaux
        self.set_liste_animaux(liste_nouveaux_animaux)

    def set_liste_animaux(self, liste_nouveaux_animaux):
        for animal in (liste_nouveaux_animaux) :
            if  isinstance(animal,Animal) :
                self.liste_animaux.append(animal)
            else:
                raise ValueError (" Attention ! Un des éléments n'est pas un animal ! ")

    def ajouter_animal(self, animal):
        self.liste_animaux.append(animal)

    def __add__(self, autre_zoo):
        animaux_nouveau_zoo = self.liste_animaux + autre_zoo.liste_animaux
        return Zoo(animaux_nouveau_zoo)