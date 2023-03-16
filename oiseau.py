from animal import *

class Oiseau(Animal):

    def __init__(self, nom, poids, taille, altitude_max): #altitude_max en mètres
        super().__init__(nom, poids, taille) #L'utilisation de super ne nécéssite pas de rappeler le self. ce serait nécessaire avec le nom de la classe
        self.altitude_max = altitude_max

    def se_deplacer(self):
        return "je vole"