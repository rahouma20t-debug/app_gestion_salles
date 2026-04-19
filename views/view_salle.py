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