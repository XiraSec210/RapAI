# RAPAI 0.0.1
# Made by XiraS3c 
# all right reserved

import string 
import random 

adjectives = ["dangereux", "fou", "ambitieux", "cool", "déterminé", "furtif", "loyal", "cool", "sinistre"] 
adverbs = ["rapidement", "délibérément", "certainement", "direttamente", "frèrek", "génial"]
verbs = ["risqué", "sauter", "débloquant", "voler", "héberger", "déplacer", "déménager"] 
nouns = ["ennemis", "site web", "victimes", "Réseau", "ordinateur", "haie", "clan"] 

lyrics = [random.choice(adjectives), random.choice(adverbs), random.choice(verbs), 
          random.choice(nouns), random.choice(adjectives), random.choice(adverbs),
         random.choice(nouns), random.choice(adjectives), random.choice(adverbs),
         random.choice(verbs), random.choice(nouns)] 

print("Je suis "+lyrics[0]+" "+lyrics[1]+" "+lyrics[2]+" des "+lyrics[3]+ " et "+lyrics[4] +" "+lyrics[5] + " "+lyrics[6] + " et "+lyrics[7]+ " "+lyrics[8] + 
      " "+lyrics[9]+" des "+lyrics[10]+"!")
