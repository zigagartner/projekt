import numpy as np
import json
import random


STEVILO_VRSTIC = 6
STEVILO_STOLPCEV = 7


class Igra:

    def __init__(self, polje):
        self.polje = np.zeros([6, 7], dtype = int)
    
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


class Shranjevanje_iger:
    def __init__(self, datoteka_s_stanjem):
       self.datoteka_s_stanjem = datoteka_s_stanjem
       self.nalozi_igre_iz_datoteke()
       
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        nov_id = self.prost_id_igre()
        igra = nova_igra()
        self.igre[nov_id] = igra
        return nov_id

    def nova_izbira(self, id_igre, vrstica,  stolpec, kos):
        igra = self.igre[id_igre]
        novo_stanje = igra.dodaj_v_polje(vrstica, stolpec, kos)
        self.igre[id_igre] = novo_stanje

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
            igre = json.load(f)
            self.igre = {int(id_igre): (Igra(polje)) for id_igre, (polje) in igre.items()}

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            igre = {id_igre: (polje) for id_igre, (polje) in self.igre.items()}
            json.dump(igre, f, ensure_ascii=False)



  