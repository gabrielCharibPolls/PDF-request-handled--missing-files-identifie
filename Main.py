import os
import re
############################################################################################
#BLOCK 1 : variables 
#direname = 'IN' # dossier d'entrée
#############################################################################################
dirName= 'IN'
in_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), dirName)
stringFiles= (os.listdir(in_path))
############################################################################################
#recuperation des numéros de factures qui se trouvent dans le nom des fichiers
#exemple de nom de fichier : 
# INVOIC1543693499_PL5263376320_PL5222574715_5430001208054_5906874381007_925073683.pdf
#extraction du code unique de la facture 925073683
uniqueCode = [re.search(r'_(\d+)\.pdf$', f).group(1) for f in stringFiles]
print (uniqueCode)

# Listes de numero unique  sur le excel
liste_initiale = [
1,2,3



]


liste_trouvee = [
2
]
set_initiale = set(liste_initiale)
set_trouve = set(liste_trouvee)
factures_manquantes = (set_initiale - set_trouve)
print("Factures manquantes :",factures_manquantes)


