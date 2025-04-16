import os
########################################
#
#########################################

# Listes fournies
liste_initiale = [
1,2,3



]

###########################################################################################
# todo :rajouter  une methode pour recupere tout les nom des fichiers enforme de text 
###########################################################################################
print(os.path.basename('C:\Users\Gabriel.Charib\Desktop\temp\isabel'))
StringDir = os.path.dirname(os.path.abspath(__file__))






liste_trouvee = [
2


]


set_initiale = set(liste_initiale)
set_trouve = set(liste_trouvee)




factures_manquantes = (set_initiale - set_trouve)
print("Factures manquantes :",factures_manquantes)


