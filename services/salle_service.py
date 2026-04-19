from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        if not all([salle.code, salle.description, salle.categorie, salle.capacite]):
            return False, "Tous les champs sont obligatoires"
#UPDATE
        if salle.capacite < 1:
            return False, "Capacité invalide"

        self.dao.insert_salle(salle)
        return True, "Salle ajoutée"

    def modifier_salle(self, salle):
        if salle.capacite < 1:
            return False, "Capacité invalide"

        self.dao.update_salle(salle)
        return True, "Salle modifiée"