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
else : 
    print("pas grave peut-être une prochaine fois")
    exit ()
# je veux rendre ma question sur le rank plus précise 
# je vais donner des valeurs au rank pour que les gens puissent répondre par leur vrai rank et non par un oui ou non 
copper = 1
bronze = 2
silver = 3
gold = 4
platinum = 5 
Emerald = 6
diamond = 7
champion = 8
score = (input("quel est ton rank ?"))
score = str.split(score)[0]
# utiliser la fonction str.split pour choisir quel mot le système veut comprendre et omettre le reste 
if score == "copper" : 
    score = 1 
if score == "bronze" : 
    score = 2
if score == "silver" : 
    score = 3
if score == "gold" : 
    score = 4
if score == "platinum" : 
    score = 5
if score == "Emerald" : 
    score = 6
if score == "diamond" : 
    score = 7
if score == "champion" :
    score = 8
# faire en sorte que dépendament de la réponse un message s'affiche en réponse a son rank Ex: nul, moyen, bon 
if score <= 3 : 
    print("cool! thq je vais t'aider")
elif 3> score <= 6 : 
    print("parfait je suis du même niveau")
else :
    print("Wow tu est vrm fort!")










    