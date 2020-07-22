import numpy as np
import json
import random

STEVILO_VRSTIC = 6
STEVILO_STOLPCEV = 7


class Igra:

    def __init__(self, polje):
        self.polje = np.zeros((6, 7))
    
    def stevilo_poteze(self):
        poteza = 1
        for vrstica in self.polje:
            for element in vrstica: 
                if element != 0:
                    poteza += 1
        return poteza

    def vnos_izbire_v_vrstico(self, stolpec):
        proste_vrstice = []
        for vrstica in range(STEVILO_VRSTIC):
            if self.polje[vrstica][stolpec] == 0:
                proste_vrstice.append(vrstica)
        return max(proste_vrstice)
    
    def ali_je_prostor(self, stolpec):
        return self.polje[0][stolpec] == 0
           

    def dodaj_v_polje(self, stolpec, vrstica, kos):
        self.polje[vrstica][stolpec] = kos

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
        

def nova_igra():
    stevilo_igre = random.choice(range(1001))
    return Igra(stevilo_igre)



    


    









    
    

                   



    