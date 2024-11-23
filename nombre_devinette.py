from random import randint, choice, random
import tkinter as tk


def nombre_devinette():
    nombre = randint(0, 100) # Nombre aléatoire

    phrase = ["Ressaye encore", 
              "N'ambandonner pas", 
              "Tu peux le faire",
              "Pas bon ressaye", 
              "Allez encore", 
              "Ressaye", 
              "Tu vas réussir",
              "Ne lâche pas", 
              "Encore une fois",
              "Dommage"
              ]
    
    tentative = 10
    derniere_phrase = []
    trouve = False
    # fonction bouton
    def verifie_nombre():
        nonlocal tentative, trouve, nombre # Pas de variable local
        devinette = input_user.get() # Récupere la saisie
        if int(devinette) == nombre: # Verifie si la saisi est strictement égal au nombre
            bouton.config(state="disabled") # Desactive le bouton

        try:
            devinette = int(devinette) # Convertie nombre en entier
            # Itération dans phrase et récupçre les phrase si elles ne sont pas dans dans la lste denrnière phrase
            phrases_dispo = [p for p in phrase if p not in derniere_phrase]
            new_phrase = choice(phrases_dispo) # Prend une phrase aléatoire dans phrase dispo
            derniere_phrase.append(new_phrase) # Ajoute new phrase dans dernière phrase
                
            if devinette > nombre: #Si la saisi est supérieur au nombre
                label_result.config(text=f"{new_phrase}, le nombre est plus petit!", fg="black")
            elif devinette < nombre: # Si la saisi est inférieur au nombre
                label_result.config(text=f"{new_phrase}, le nombre est plus grand", fg="black")

            else:  # Sinon affiche gagner et arrete la boucle
                label_result.config(text="Bravo vous avez trouvé le nombre", fg="green", font=('Arial', 15))
                prev_value.config(text="") #Affiche rien
                trouve = True 

            tentative -= 1  # Décrementer de -1
            label_tentative.config(text=f"Il vous reste {tentative} tentatives")
            prev_value.config(text=f"Dernière valeur entrée : {devinette}") # Affiche la dernière valeur

            if tentative <= 0 and not trouve: # Si tentative est inférieur ou égal à 0 et pas vrai 
                label_result.config(text=f"Vous avez perdu! Le nombre était {nombre}.", fg="red", font=('Arial', 15))
                input_user.config(state='disabled')  # Desactive le bouton cliquable

        except ValueError: # Erreur 
            label_result.config(text="Veullez entrez un nombre valide", fg="red", font=('Arial', 15))

        input_user.delete(0, tk.END) # Nettoie la saisie
    
    root = tk.Tk()
    root.title("Jeux devinette")
    root.geometry("400x200")

    # Texte tentative
    label_tentative = tk.Label(root, text=f"il vous reste {tentative} tentatives", font=('Arial', 10))
    label_tentative.grid(row=0, column=1, padx=10, pady=10)
    
    # Texte entrez un nombre
    label_texte = tk.Label(root, text="Entrez un nombre")
    label_texte.grid(row=1, column=0, padx=10, pady=10)

    # Entrez saisi de l'utilisateur
    input_user = tk.Entry(root, width=20)
    input_user.grid(row=1, column=1, padx=10, pady=10)

    #Bouton de Deviner
    bouton = tk.Button(root, text="Deviner", command=verifie_nombre)
    bouton.grid(row=1, column=2, padx=10, pady=10)

    # Texte: affiche la valeur précedent
    prev_value = tk.Label(root, text="")
    prev_value.grid(row=2, columnspan=3, padx=10, pady=10)

    #Texte: Affiche le resulat
    label_result = tk.Label(root, text="")
    label_result.grid(row=3, columnspan=3, padx=10, pady=10)

    root.mainloop()
nombre_devinette() # Appel la fonction