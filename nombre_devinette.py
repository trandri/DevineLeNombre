from random import randint, choice, random

nombre = randint(0, 100)

phrase = ["Ressaye encore!", "Non, n'ambandonner pas!", "Oups, tu peux le faire",
          "Pas bon, ressaye", "Allez encore", "Ressaye", "Tu vas réussir",
          "Ne lâche pas!", "Encore une fois"]
devinette = int(input("Pensez un nombre entre 0 à 100: "))
tentative = 9
derniere_phrase = []
trouve = False
while (tentative > 0 and not trouve ):

    phrases_dispo = [p for p in phrase if p not in derniere_phrase]
    new_phrase = choice(phrases_dispo)
    derniere_phrase.append(new_phrase)
    
    if devinette > nombre:
        print(f"{choice(phrase)} Le nombre est plus petit, encore {tentative}")
    elif devinette < nombre:
        print(f"{choice(phrase)} Le nombre est plus grand, encore {tentative} tentative")
    else:
        print("Bravo avez trouvé le nombre")
        trouve = True
    
    tentative -= 1
    devinette = int(input("Entrez à nouveau: "))

if (trouve):
    print("Vous avez gagner")
else:
    print("Vous avez perdu")