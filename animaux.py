# Animal
#Définition de la classe Animal

class Animal:

    def __init__(self, poids, taille): #poids en kg, taille en m
        #self.__poids_animal = poids
        #self.__taille_animal = taille
        self.set_poids_animal(poids)
        self.set_taille_animal(taille)

    def se_deplacer(self):
        pass
    
    #getters
    def get_poids_animal(self):
        return self.__poids_animal

    def get_taille_animal(self):
        return self.__taille_animal

    #setters
    def set_poids_animal(self, poids):
        while True:
            try:
                poids > 0
                break
            except ValueError:
                print(" Attention ! Un animal ne peut pas avoir un poids nul ou négatif ! ")
        self.__poids_animal = poids

    def set_taille_animal(self, taille):
        while True:
            try:
                taille > 0
                break
            except ValueError:
                print(" Attention ! Un animal ne peut pas avoir une taille nulle ou négative ! ")
        self.__taille_animal = taille

class Serpent(Animal):

    def se_deplacer(self):
        return "je rampe"

class Oiseau(Animal):

    def __init__(self, poids, taille, altitude_max): #altitude_max en mètres
        super().__init__(poids, taille) #L'utilisation de super ne nécéssite pas de rappeler le self. ce serait nécessaire avec le nom de la classe
        self.altitude_max = altitude_max

    def se_deplacer(self):
        return "je vole"