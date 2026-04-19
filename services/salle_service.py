from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        if not all([salle.code, salle.description, salle.categorie, salle.capacite]):
            return False, "Tous les champs sont obligatoires"
#UPDATE