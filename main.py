#main
#Programme principal

from animal import *
from zoo import *
from serpent import *
from oiseau import *

ours = Animal("Teddy l'ours",150,2)
print ("Cet ours mesure", ours.taille_animal, "m.")
print ("Cet ours pèse", ours.poids_animal, "kg.","\n")

cobra = Serpent("SSsssssss le cobra",1.5,1)
print ("Ce cobra mesure", cobra.taille_animal, "m.")
print ("Ce cobra pèse", cobra.poids_animal, "kg.")
print ("Le cobra dit : pour me déplacer",cobra.se_deplacer(),".","\n")

condor = Oiseau("Chupakabra le condor",30,1.5,2000)
print ("Ce condor mesure", condor.taille_animal, "m.")
print ("Ce condor pèse", condor.poids_animal, "kg.")
print ("Le condor dit : pour me déplacer",condor.se_deplacer(),".")
print ("Le condor peut voler jusqu'à une altitude maximum de",condor.altitude_max,"mètres.","\n")

liste_animaux_dans_le_zoo = [ours, cobra, condor]
zoo_grenoble = Zoo(liste_animaux_dans_le_zoo)

#print (zoo_grenoble.liste_animaux)
#zoo_grenoble.ajouter_animal(panda)
#print (zoo_grenoble.liste_animaux)

ani = Animal("TanTan",2,6)
print(ani)
print ([str(animal) for animal in zoo_grenoble.liste_animaux], "\n")

panda = Animal("Cocojingo le panda",100,1.5)
chat = Animal("Chat potté",5,0.3)
Khan = Animal("Khan", 150, 1)
liste_des_animaux_nouveau_zoo = [chat,Khan, panda]
nouveau_zoo = Zoo(liste_des_animaux_nouveau_zoo)
print ([str(animal) for animal in nouveau_zoo.liste_animaux], "\n")

grand_zoo = zoo_grenoble + nouveau_zoo
print ([str(animal) for animal in grand_zoo.liste_animaux], "\n")

print (grand_zoo.liste_animaux)


