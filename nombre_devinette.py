from random import randint, choice
import tkinter as tk


def nombre_devinette():
    nombre = randint(0, 100) # Nombre aléatoire

    phrases = ["Ressaye encore", 
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
    
    # Fonction: bouton deviner
    def verifie_nombre():
        nonlocal tentative, trouve, nombre # Porté de variable non local
        devinette = input_user.get() # Récupere la saisi

        try:
            if int(devinette) == nombre: # Verifie si la saisi est strictement égal au nombre
                deviner_bouton.config(state="disabled") # Desactive le bouton
            else: # Sinon lever une erreur
                raise ValueError
        except ValueError:
            label_result.config(text="Veullez entrez un nombre valide", fg="red", font=('Arial', 15))

        try:
            devinette = int(devinette) # Convertie nombre en entier

            # Itération dans phrase et récupçre les phrase si elles ne sont pas dans dans la lste denrnière phrase
            phrases_dispo = [phrase for phrase in phrases if phrase not in derniere_phrase]
            new_phrase = choice(phrases_dispo) # Prend une phrase aléatoire dans phrase dispo
            derniere_phrase.append(new_phrase) # Ajoute new phrase dans dernière phrase
                
            if devinette > nombre: # Si la saisi est supérieur au nombre
                label_result.config(text=f"{new_phrase}, le nombre est plus petit!", fg="black")
            elif devinette < nombre: # Si la saisi est inférieur au nombre
                label_result.config(text=f"{new_phrase}, le nombre est plus grand", fg="black")

            else:  # Sinon affiche gagner et arrete la boucle
                label_result.config(text="Bravo vous avez trouvé le nombre", fg="green", font=('Arial', 15))
                prev_value.config(text="") # Affiche rien
                input_user.config(state="disabled") # Desactive la saisi
                trouve = True 

            tentative -= 1  # Décrementer de -1
            label_tentative.config(text=f"Il vous reste {tentative} tentatives")
            prev_value.config(text=f"Dernière valeur entrée : {devinette}") # Affiche la dernière valeur

            if tentative <= 0 and not trouve: # Si tentative est inférieur ou égal à 0 et trouve est pas vrai
                label_result.config(text=f"Vous avez perdu! Le nombre était {nombre}.", fg="red", font=('Arial', 15))
                input_user.config(state="disabled")  # Desactive la saisi
                deviner_bouton.config(state="disabled") # Desactive le bouton deviner
                
        except ValueError: # Erreur 
            label_result.config(text="Veullez entrez un nombre valide", fg="red", font=('Arial', 15))

        # Nettoie la saisie à la fin
        input_user.delete(0, tk.END) 

    # Fonction: Bouuton rejouer   
    def rejouer():
        nonlocal tentative, trouve, nombre, derniere_phrase
        tentative = 10
        trouve = False
        nombre = randint(0, 100)
        label_tentative.config(text=f"Il vous reste {tentative} tentatives")
        label_result.config(text="")
        prev_value.config(text="")
        input_user.config(state="normal")
        deviner_bouton.config(state="normal")
        input_user.delete(0, tk.END)
        derniere_phrase = []
    
    root = tk.Tk()
    root.title("Jeux devinette")
    root.geometry("520x250")
    root.minsize(width=400, height=250)

    # Texte: tentative
    label_tentative = tk.Label(root, text=f"il vous reste {tentative} tentatives", font=("Arial", 12))
    label_tentative.grid(row=0, column=1, padx=10, pady=10)
    
    # Texte: entrez un nombre
    label_texte = tk.Label(root, text="Nombre entre 0 à 100", font=("Arial", 12))
    label_texte.grid(row=1, column=0, padx=10, pady=10)

    # Entrez: Saisi de l'utilisateur
    input_user = tk.Entry(root, width=20)
    input_user.grid(row=1, column=1, padx=10, pady=10)

    # Bouton: Deviner
    deviner_bouton = tk.Button(root, text="Deviner", command=verifie_nombre)
    deviner_bouton.grid(row=1, column=2, padx=10, pady=10)

    # Texte: Rejouer
    label_rejouer = tk.Label(root, text="Tu veux rejouer?", font=("Arial", 12))
    label_rejouer.grid(row=2, column=1, padx=10, pady=10)

    # Bouton: Rejouer
    rejouer_bouton = tk.Button(root, text="Rejouer", command=rejouer)
    rejouer_bouton.grid(row=2, column=2, padx=10, pady=10)

    # Texte: affiche la valeur précedent
    prev_value = tk.Label(root, text="")
    prev_value.grid(row=3, column=1, padx=10, pady=10)

    #Texte: Affiche le resulat
    label_result = tk.Label(root, text="")
    label_result.grid(row=4, columnspan=3, padx=10, pady=10)

    root.mainloop()

nombre_devinette() # Appel la fonction