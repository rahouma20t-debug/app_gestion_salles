import customtkinter as ctk
from services.salle_service import ServiceSalle
from models.salle import Salle
from tkinter import ttk
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service = ServiceSalle()
        self.title("Gestion des salles")
        self.geometry("500x500")


        self.tree = ttk.Treeview(self, columns=("code", "desc", "cat", "cap"), show="headings")

        self.tree.heading("code", text="Code")
        self.tree.heading("desc", text="Description")
        self.tree.heading("cat", text="Categorie")
        self.tree.heading("cap", text="Capacite")

        self.tree.pack(pady=20)
        self.lister_salles()
        self.entry_code = ctk.CTkEntry(self, placeholder_text="Code")
        self.entry_code.pack()

        self.entry_desc = ctk.CTkEntry(self, placeholder_text="Description")
        self.entry_desc.pack()

        self.entry_cat = ctk.CTkEntry(self, placeholder_text="Categorie")
        self.entry_cat.pack()

        self.entry_cap = ctk.CTkEntry(self, placeholder_text="Capacite")
        self.entry_cap.pack()

        btn = ctk.CTkButton(self, text="Afficher les salles", command=self.lister_salles)
        btn.pack(pady=10)

        btn_add = ctk.CTkButton(self, text="Ajouter salle", command=self.ajouter_salle)
        btn_add.pack(pady=10)

        btn_delete = ctk.CTkButton(self, text="Supprimer salle", command=self.supprimer_salle)
        btn_delete.pack(pady=10)

    def lister_salles(self):
        self.tree.delete(*self.tree.get_children())

        liste = self.service.recuperer_salles()

        for s in liste:
            self.tree.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))

    def supprimer_salle(self):
        selected = self.tree.selection()

        if not selected:
            print("Aucune salle sélectionnée")
            return

        for item in selected:
            values = self.tree.item(item, "values")
            code = values[0]
            success, msg = self.service.supprimer_salle(code)
            print(msg)
        self.lister_salles()

        print("Salle supprimée")

    def ajouter_salle(self):
        code = self.entry_code.get()
        desc = self.entry_desc.get()
        cat = self.entry_cat.get()
        cap = self.entry_cap.get()
        salle = Salle(code, desc, cat, cap)
        success, msg = self.service.ajouter_salle(salle)

        print(msg)
        self.lister_salles()

        try:
            cap = int(cap)
        except ValueError:
            print("Capacité invalide")
            return

        salle = Salle(code, desc, cat, cap)

        success, msg = self.service.ajouter_salle(salle)
        print(msg)

        self.lister_salles()