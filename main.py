#main
#Programme principal

from animaux import *

ours = Animal(150,2)
print ("Cet ours mesure", ours.get_taille_animal(), "m.")
print ("Cet ours pèse", ours.get_poids_animal(), "kg.","\n")

cobra = Serpent(1,1.5)
print ("Ce cobra mesure", cobra.get_taille_animal(), "m.")
print ("Ce cobra pèse", cobra.get_poids_animal(), "kg.")
print ("Le cobra dit : pour me déplacer",cobra.se_deplacer(),".","\n")

condor = Oiseau(30,1.5,2000)
print ("Ce condor mesure", condor.get_taille_animal(), "m.")
print ("Ce condor pèse", condor.get_poids_animal(), "kg.")
print ("Le condor dit : pour me déplacer",condor.se_deplacer(),".")
print ("Le condor peut voler jusqu'à une altitude maximum de",condor.altitude_max,"mètres.","\n")