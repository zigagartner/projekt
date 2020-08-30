import numpy as np
import random


STEVILO_VRSTIC = 6
STEVILO_STOLPCEV = 7


class Igra:

    def __init__(self, stevilo_igre):
        self.stevilo_igre = stevilo_igre
        self.polje = np.zeros([6, 7], dtype = int)
        self.zacetna_poteza = int(random.choice([0, 1]))
    
    def vnos_izbire_v_vrstico(self, stolpec):
        proste_vrstice = []
        for vrstica in range(STEVILO_VRSTIC):
            if self.polje[vrstica][stolpec] == 0:
                proste_vrstice.append(vrstica)
        return max(proste_vrstice)
    
    def ali_je_prostor(self, stolpec):
        return self.polje[0][stolpec] == 0
           
    def dodaj_v_polje(self, vrstica, stolpec, kos):
        self.polje[vrstica][stolpec] = kos
    
    def mozne_poteze(self):
        poteze = []
        for stolpec in self.polje[0]:
            if stolpec == 0:
                poteze.append(stolpec)
        return poteze

    def zmagovalna_poteza(self, kos):
        #Vodoravno
        for s in range(STEVILO_STOLPCEV - 3): 
            for v in range(STEVILO_VRSTIC):
                if self.polje[v][s] == kos and self.polje[v][s + 1] == kos and self.polje[v][s + 2] == kos and self.polje[v][s + 3] == kos:
                    return True
        #Navpicno
        for s in range(STEVILO_STOLPCEV): 
            for v in range(STEVILO_VRSTIC - 3):
                if self.polje[v][s] == kos and self.polje[v + 1][s] == kos and self.polje[v + 2][s] == kos and self.polje[v + 3][s] == kos:
                    return True
        #Posevno navzgor
        for s in range(STEVILO_STOLPCEV - 3):
            for v in range(3, STEVILO_VRSTIC):
                if self.polje[v][s] == kos and self.polje[v - 1][s + 1] == kos and self.polje[v - 2][s + 2] == kos and self.polje[v - 3][s + 3] == kos:
                    return True
        #Posevno navzdol
        for s in range(STEVILO_STOLPCEV - 3):
            for v in range(STEVILO_VRSTIC - 3):
                if self.polje[v][s] == kos and self.polje[v + 1][s + 1] == kos and self.polje[v + 2][s + 2] == kos and self.polje[v + 3][s + 3] == kos:
                    return True    

    def celotna_poteza(self, stolpec, kos):
        if self.ali_je_prostor(stolpec):
            v = self.vnos_izbire_v_vrstico(stolpec)
            self.dodaj_v_polje(v, stolpec, kos)

    def stevilo_poteze(self):
        stevilo_poteze  = self.zacetna_poteza
        for vrstica in self.polje:
            for element in vrstica:
                if element != 0:
                    stevilo_poteze += 1
        return int(stevilo_poteze)

    def igralec_na_vrsti(self):
        if self.stevilo_poteze() % 2 != 0:
            return 1
        else:
            return 2


def prosti_stolpci(polje):
    stolpci = []
    for stolpec in polje[0]:
        if stolpec == 0:
            stolpci.append(stolpec)
    return stolpci
        

def nova_igra():
    stevilo_igre = random.choice(range(1001))
    return Igra(stevilo_igre)


class Shramba:

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = igra, igra.polje
        return id_igre

    





            






    
    

        






    



    





