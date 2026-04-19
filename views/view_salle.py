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


        btn = ctk.CTkButton(self, text="Afficher les salles", command=self.afficher_salles)
        btn.pack(pady=10)