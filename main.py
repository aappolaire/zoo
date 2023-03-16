#main
#Programme principal

from animaux import *
from zoo import *

ours = Animal(150,2)
print ("Cet ours mesure", ours.taille_animal, "m.")
print ("Cet ours pèse", ours.poids_animal, "kg.","\n")

cobra = Serpent(1,1.5)
print ("Ce cobra mesure", cobra.taille_animal, "m.")
print ("Ce cobra pèse", cobra.poids_animal, "kg.")
print ("Le cobra dit : pour me déplacer",cobra.se_deplacer(),".","\n")

condor = Oiseau(30,1.5,2000)
print ("Ce condor mesure", condor.taille_animal, "m.")
print ("Ce condor pèse", condor.poids_animal, "kg.")
print ("Le condor dit : pour me déplacer",condor.se_deplacer(),".")
print ("Le condor peut voler jusqu'à une altitude maximum de",condor.altitude_max,"mètres.","\n")

panda = Animal(100,1.5)

liste_animaux_dans_le_zoo = [ours, cobra, condor]

zoo_grenoble = Zoo(liste_animaux_dans_le_zoo)
print (zoo_grenoble.liste_animaux)
zoo_grenoble.ajouter_animal(panda)
print (zoo_grenoble.liste_animaux)