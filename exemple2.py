import tkinter as tk

def enregistrer():
    pseudo = pseudo_entry.get()
    mdp = mdp_entry.get()
    email = email_entry.get()
    print("Pseudo :", pseudo)
    print("Mot de passe :", mdp)
    print("Email :", email)

fenetre = tk.Tk()
fenetre.title("Inscription")

tk.Label(fenetre, text="Pseudo :").pack()
pseudo_entry = tk.Entry(fenetre)
pseudo_entry.pack()

tk.Label(fenetre, text="Mot de passe :").pack()
mdp_entry = tk.Entry(fenetre, show="*")
mdp_entry.pack()

tk.Label(fenetre, text="Email :").pack()
email_entry = tk.Entry(fenetre)
email_entry.pack()

valider_button = tk.Button(fenetre, text="Valider", command=enregistrer)
valider_button.pack()

fenetre.mainloop()
