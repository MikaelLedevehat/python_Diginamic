import random
import string

class Etudiant():

    def __init__(self,nom,prenom,notes):
        self.notes = notes
        self.nom = nom
        self.prenom = prenom

    def moyenne_generale(self):
        moy = 0
        for i in self.notes:
            moy += i

        moy /= len(self.notes)
        return moy

    def __repr__(self):
        return f"({self.nom},{self.prenom},{self.notes})\n"


class Promotion():

    matieres = ["Math", "Francais", "Anglais", "SVT", "EPS"]

    def __init__(self):
        self.etudiants = []

    def generer_tab_notes(self):
        t = []
        for i in Promotion.matieres:
            t.append(random.randrange(0,20))
        return t

    def generer_random_string(self):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(8))
        return result_str

    def moyenne_promo(self):
        moy = 0
        for i in self.etudiants:
            moy += i.moyenne_generale()

        moy /= len(self.etudiants)
        return moy

    def trouver_etudiant_meilleur_note(self,matiere):
        if not matiere in Promotion.matieres:
            return None

        i = Promotion.matieres.index(matiere)
        bestEtudiant = None
        for e in self.etudiants:
            if bestEtudiant == None:
                bestEtudiant = e
            elif bestEtudiant.notes[i] < e.notes[i]:
                bestEtudiant = e

        return bestEtudiant

    def replir_etudiants(self, nb):
        for i in range(0,nb):
            self.etudiants.append(Etudiant(self.generer_random_string(),self.generer_random_string(),self.generer_tab_notes()))

p = Promotion()
p.replir_etudiants(10)
print(p.etudiants)
print(p.moyenne_promo())
print(p.trouver_etudiant_meilleur_note("Math"))
