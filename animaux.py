# Animal
#Définition de la classe Animal

class Animal:

    def __init__(self, poids, taille): #poids en kg, taille en m
        #self.__poids_animal = poids
        #self.__taille_animal = taille
        self.poids_animal = poids
        self.taille_animal = taille

    def se_deplacer(self):
        pass
    
    @property
    def poids_animal(self):
        return self._poids_animal

    @property
    def taille_animal(self):
        return self._taille_animal

    @poids_animal.setter
    def poids_animal(self, poids):
        if poids < 0 :
            raise ValueError (" Attention ! Un animal ne peut pas avoir un poids nul ou négatif ! ")
        self._poids_animal = poids

    @taille_animal.setter
    def taille_animal(self, taille):
        if taille < 0 :
            raise ValueError (" Attention ! Un animal ne peut pas avoir une taille négative ! ")
        self._taille_animal = taille

class Serpent(Animal):

    def se_deplacer(self):
        return "je rampe"

class Oiseau(Animal):

    def __init__(self, poids, taille, altitude_max): #altitude_max en mètres
        super().__init__(poids, taille) #L'utilisation de super ne nécéssite pas de rappeler le self. ce serait nécessaire avec le nom de la classe
        self.altitude_max = altitude_max

    def se_deplacer(self):
        return "je vole"