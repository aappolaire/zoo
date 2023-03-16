# Animal
#Définition de la classe Animal

class Animal:

    def __init__(self, nom, poids, taille): #poids en kg, taille en m
        #self.__poids_animal = poids
        #self.__taille_animal = taille
        self.nom_animal = nom
        self.poids_animal = poids
        self.taille_animal = taille

    def se_deplacer(self):
        pass
    
    @property
    def nom_animal(self):
        return self.__nom_animal

    @property
    def poids_animal(self):
        return self.__poids_animal

    @property
    def taille_animal(self):
        return self.__taille_animal

    @poids_animal.setter
    def poids_animal(self, poids):
        if poids < 0 :
            raise ValueError (" Attention ! Un animal ne peut pas avoir un poids nul ou négatif ! ")
        self.__poids_animal = poids

    @taille_animal.setter
    def taille_animal(self, taille):
        if taille < 0 :
            raise ValueError (" Attention ! Un animal ne peut pas avoir une taille négative ! ")
        self.__taille_animal = taille

    @nom_animal.setter
    def nom_animal(self, nom):
        self.__nom_animal = nom

    def __str__(self):
        return f"{self.nom_animal}, poids = {self.poids_animal} kg, taille = {self.taille_animal} m"

class Serpent(Animal):

    def se_deplacer(self):
        return "je rampe"

class Oiseau(Animal):

    def __init__(self, nom, poids, taille, altitude_max): #altitude_max en mètres
        super().__init__(nom, poids, taille) #L'utilisation de super ne nécéssite pas de rappeler le self. ce serait nécessaire avec le nom de la classe
        self.altitude_max = altitude_max

    def se_deplacer(self):
        return "je vole"