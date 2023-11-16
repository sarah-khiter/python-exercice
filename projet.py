import tkinter as tk
from ttkthemes import ThemedTk
import json

# Fonction pour ajouter une tâche
def add_task():
    description = description_entry.get()
    due_date = due_date_entry.get()
    task = {"description": description, "due_date": due_date, "done": False, "notes": ""}
    tasks.append(task)
    update_task_list()
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

# Fonction pour afficher les tâches
def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        task_text = f"{task['description']} (Due: {task['due_date']})"
        if task['done']:
            task_text = "✓ " + task_text
        task_list.insert(tk.END, task_text)

# Fonction pour marquer une tâche comme terminée
def mark_done():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        tasks[index]['done'] = True
        update_task_list()

# Fonction pour supprimer une tâche
def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        del tasks[index]
        update_task_list()

# Enregistrement des tâches dans un fichier JSON
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Chargement des tâches à partir d'un fichier JSON
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        update_task_list()
    except FileNotFoundError:
        tasks = []

# Créez la fenêtre principale
app = tk.Tk()
app.title("Gestion avancée de tâches")
app.geometry("400x500")

# Personnalisation des styles
button_style = {
    "bg": "lightblue",   # Couleur de fond du bouton
    "font": ("Helvetica", 12)  # Police et taille du texte
}

description_entry = {
    "bg": "lightgray",  # Couleur de fond de la zone de description
    "fg": "black",      # Couleur du texte
    "font": ("Helvetica", 12)  # Police et taille du texte
}



# Créez les composants de l'interface utilisateur avec les styles personnalisés
description_label = tk.Label(app, text="Description:")
description_entry = tk.Entry(app)
due_date_label = tk.Label(app, text="Date d'échéance:")
due_date_entry = tk.Entry(app)
add_button = tk.Button(app, text="Ajouter", command=add_task, **button_style)
task_list = tk.Listbox(app, selectmode=tk.SINGLE)
mark_done_button = tk.Button(app, text="Marquer comme terminée", command=mark_done, **button_style)
delete_button = tk.Button(app, text="Supprimer", command=delete_task, **button_style)
save_button = tk.Button(app, text="Enregistrer", command=save_tasks, **button_style)
load_button = tk.Button(app, text="Charger", command=load_tasks, **button_style)

# Utilisez le gestionnaire de mise en page pack pour espacer les boutons
description_label.pack()
description_entry.pack()
due_date_label.pack()
due_date_entry.pack()
add_button.pack(pady=5)
task_list.pack()
mark_done_button.pack(pady=5)
delete_button.pack(pady=5)
save_button.pack(pady=5)
load_button.pack(pady=5)

# Chargez les tâches existantes
load_tasks()

# Lancez l'application
app.mainloop()
