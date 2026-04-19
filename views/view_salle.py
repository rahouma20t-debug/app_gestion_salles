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
        self.entry_code = ctk.CTkEntry(self, placeholder_text="Code")
        self.entry_code.pack()

        self.entry_desc = ctk.CTkEntry(self, placeholder_text="Description")
        self.entry_desc.pack()

        self.entry_cat = ctk.CTkEntry(self, placeholder_text="Categorie")
        self.entry_cat.pack()

        self.entry_cap = ctk.CTkEntry(self, placeholder_text="Capacite")
        self.entry_cap.pack()




        btn = ctk.CTkButton(self, text="Afficher les salles", command=self.afficher_salles)
        btn.pack(pady=10)

    def afficher_salles(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        salles = self.service.recuperer_salles()

        for s in salles:
            self.tree.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))





