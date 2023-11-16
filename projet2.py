import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk  # Importez ThemedTk de ttkthemes
import json

# Fonction pour ajouter un contact
def ajouter_contact():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    num = num_entry.get()
    contact = {"nom": nom, "prenom": prenom, "num": num}
    contacts.append(contact)
    sauvegarder_contacts()
    update_listbox()

# Fonction pour enregistrer les contacts dans un fichier JSON
def sauvegarder_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Fonction pour afficher les détails d'un contact sélectionné
def afficher_details():
    selected_index = listbox.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        details_label.config(text=f"Nom: {contact['nom']}, Prénom: {contact['prenom']}, Numéro: {contact['num']}")

# Fonction pour supprimer un contact sélectionné
def supprimer_contact():
    selected_index = listbox.curselection()
    if selected_index:
        del contacts[selected_index[0]]
        sauvegarder_contacts()
        update_listbox()
        details_label.config(text="")

# Fonction pour modifier un contact sélectionné
def modifier_contact():
    selected_index = listbox.curselection()
    if selected_index:
        new_nom = nom_entry.get()
        new_prenom = prenom_entry.get()
        new_num = num_entry.get()
        contact = {"nom": new_nom, "prenom": new_prenom, "num": new_num}
        contacts[selected_index[0]] = contact
        sauvegarder_contacts()
        update_listbox()
        details_label.config(text="")

# Fonction pour mettre à jour la liste des contacts
def update_listbox():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['nom']} {contact['prenom']}")

# Créer une fenêtre ThemedTk à la place de tk.Tk()
window = ThemedTk(theme="plastik")  # Vous pouvez choisir un thème différent ici

window.title("Gestionnaire de Contacts")

# Liste des contacts
contacts = []

# Charger les contacts depuis un fichier JSON s'ils existent
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    pass

# Entrées pour le nom, le prénom et le numéro
nom_label = ttk.Label(window, text="Nom:")  # Utilisez ttk.Label
nom_label.pack()
nom_entry = ttk.Entry(window)  # Utilisez ttk.Entry
nom_entry.pack()

prenom_label = ttk.Label(window, text="Prénom:")  # Utilisez ttk.Label
prenom_label.pack()
prenom_entry = ttk.Entry(window)  # Utilisez ttk.Entry
prenom_entry.pack()

num_label = ttk.Label(window, text="Numéro:")  # Utilisez ttk.Label
num_label.pack()
num_entry = ttk.Entry(window)  # Utilisez ttk.Entry
num_entry.pack()

# Boutons pour ajouter, supprimer et modifier les contacts
ajouter_button = ttk.Button(window, text="Ajouter", command=ajouter_contact)  # Utilisez ttk.Button
ajouter_button.pack()

supprimer_button = ttk.Button(window, text="Supprimer", command=supprimer_contact)  # Utilisez ttk.Button
supprimer_button.pack()

modifier_button = ttk.Button(window, text="Modifier", command=modifier_contact)  # Utilisez ttk.Button
modifier_button.pack()

# Liste des contacts
listbox = tk.Listbox(window)
listbox.pack()
listbox.bind('<<ListboxSelect>>', lambda event: afficher_details())

# Détails du contact sélectionné
details_label = ttk.Label(window, text="")  # Utilisez ttk.Label
details_label.pack()

# Mettre à jour la liste des contacts au démarrage de l'application
update_listbox()

window.mainloop()
