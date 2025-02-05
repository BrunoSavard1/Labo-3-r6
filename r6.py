# 3 blocs de condition complets (if)
# 3 entrées utilisateurs
# 1 opérateurs logique
# imprimier un résultat 
jeu = input("as tu r6?")
if jeu != "oui":
    print("une vrai déception")
    exit ()
else :
    print("nice")
    # crée une question qui se répond par oui ou non 
    # ensuite afficher le texte de ton choix pour chaque cas ( oui ou non)
temps = input("as tu le temps de jouer a soir ?")
heure = input (" 7h cv ?")
if temps == "oui" and heure == "oui" :
    print("parfait vient me rejoindre sur discord")
    # question espace prof
else : 
    print("pas grave peut-être une prochaine fois")
    exit ()
rank = input ("est tu gold ou plus ??")
if rank != "oui" : 
    print("ha ha t'inquiète je vais te carry")
else :
    print ("Yes on va grind à soir ")
    exit ()
    