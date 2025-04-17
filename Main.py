import os
import re
################################################################################
# BLOCK 1 : Définition des chemins
################################################################################
input_folder= 'IN'
input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), input_folder)


if not os.path.isdir(input_path):
    raise FileNotFoundError(f"Le dossier spécifié n'existe pas : {input_path}")
file_names= (os.listdir(input_path))
############################################################################################
#recuperation des numéros de factures qui se trouvent dans le nom des fichiers
#exemple de nom de fichier : 
# INVOIC1543693499_PL5263376320_PL5222574715_5430001208054_5906874381007_925073683.pdf
#extraction du code unique de la facture 925073683
liste_trouvee_unique_code= [re.search(r'_(\d+)\.pdf$', f).group(1) for f in file_names]
############################################################################################
#todo: recupere les numéros de factures dans un fichier texte dans le dosser IN.
#eviter de toucher le code et rajouter les vergules a la main
##############################################################################################

# Listes de numero unique  sur le excel
liste_initiale = [

]



set_initiale = set(liste_initiale)
set_trouve = set(liste_trouvee_unique_code)
factures_manquantes = (set_initiale - set_trouve)
#print("Factures manquantes :",factures_manquantes)
print("################################################################################")
print("total des factures manquantes :",len(factures_manquantes))
print("################################################################################")

##############################################################################################
# # TODO: Write the missing invoice numbers to a text file (e.g., 'missing_invoices.txt')
##############################################################################################
