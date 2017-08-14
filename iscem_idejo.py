import random
import os.path
import heapq

class Ideje:
    def __init__(self):
        self.regija = None
        self.mozne_regije = ['Gorenjska', 'Dolenjska', 'Primorska', 'Koroška', 'Štajerska', 'Notranjska', 'Prekmurje']
        self.brez_regije = None
        self.slovar = {}
        self.nalozi_slovar_idej()
        self.izbira = None
        self.primerni_cilji = []
        self.mozne_oznake = self.vse_oznake()
        self.seznam_oznak = []
        self.stanje = None
        self.cisti_zacetek_oznak()
        
    def nalozi_slovar_idej(self):
        if self.regija != None:
            nov_slovar = {}
            for kraj in self.slovar.keys():
                if self.slovar[kraj][0] == self.regija:
                       nov_slovar[kraj] = self.slovar[kraj]
            self.slovar = nov_slovar
            #slovar samo za tocno doloceno regijo
        else:
            with open('ideje.txt') as f:
                vse_ideje = f.read()
                posebej_kraji = vse_ideje.split(';')
                for vse_za_kraj in posebej_kraji:
                    loceno_ime_in_atributi = vse_za_kraj.split(':')
                    seznam_atributov = loceno_ime_in_atributi[1].strip().split(',')
                    self.slovar[loceno_ime_in_atributi[0].strip()] = seznam_atributov

    def vse_oznake(self):
        '''Seznam vseh oznak brez ponavljanja'''
        vse_oznake = []
        for kraj in self.slovar.keys():
            za_en_kraj = self.oznake_kraja(kraj)
            for oznaka in za_en_kraj:
                if oznaka not in vse_oznake:
                    vse_oznake.append(oznaka)
        return vse_oznake

    def oznake_kraja(self, kraj):
        '''Seznam oznak enega kraja'''
        return self.slovar[kraj][1:]
    
#odlocimo se za nakljucno izbiro
    def nakljucna_izbira(self):
        self.izbira = random.choice(self.nastejemo_vse_kraje())
       
    def nastejemo_vse_kraje(self):
        '''Seznam krajev'''
        seznam_krajev = []
        for kraj in self.slovar.keys():
            seznam_krajev.append(kraj)
        return seznam_krajev

#dolocimo samo regijo
    def poznamo_regijo(self):
        for kraj in self.slovar.keys():
            self.primerni_cilji.append(kraj)

#dolocimo oznako
    def seznam_izbranih_oznak(self):
        if self.oznaka not in self.seznam_oznak:
            self.seznam_oznak.append(self.oznaka)

    def poznamo_oznake(self):
        for kraj in self.slovar.keys():
            vsota = 0
            for oznaka in self.seznam_oznak:
                if oznaka not in self.oznake_kraja(kraj):
                    vsota += 1
            if vsota == 0:
                self.primerni_cilji.append(kraj)
        if self.stanje == 'priljubljeno':
            if self.primerni_cilji == []:
                najveckrat = self.seznam_oznak[0]
                self.stanje = 'najpogostejsa_oznaka'
                for kraj in self.slovar.keys():
                    if najveckrat in self.oznake_kraja(kraj):
                        self.primerni_cilji.append(kraj)

    def pocisti_oznake(self):
        self.seznam_oznak = []
        self.primerni_cilji = []
        self.stanje = 'pocisti'
                
#za priljubljeno trikrat najveckrat iskane oznake, drugače največkrat iskana
    def cisti_zacetek_oznak(self):
        if os.path.exists('iskane_oznake.txt'):
            self.stetje_iskanih_oznak()
        else:
            with open('iskane_oznake.txt', 'w') as f:
                print(' ', file=f)
            self.stevilo_iskanih_oznak = 0

    def stetje_iskanih_oznak(self):
        with open('iskane_oznake.txt') as f:            
            seznam_oznak = f.read().strip().split(',')
            self.stevilo_iskanih_oznak = len(seznam_oznak) 
        
    def zapis_iskanih_oznak_v_dat(self):
        self.stevilo_iskanih_oznak += 1
        with open('iskane_oznake.txt', 'a') as f:
                print(self.oznaka + ',', file=f)

    def najveckrat_iskane(self):
        with open('iskane_oznake.txt') as f:
            slovar_pojavitev = {}
            seznam_oznak = f.read().strip().split(',')
            for oznaka in seznam_oznak:
                oznaka = oznaka.strip()
                if oznaka in slovar_pojavitev.keys():
                    slovar_pojavitev[oznaka] += 1
                else:
                    slovar_pojavitev[oznaka] = 1
            self.seznam_oznak = heapq.nlargest(3, slovar_pojavitev, key=slovar_pojavitev.get)

#za prikaz
    def preveri_regijo(self):
        if self.regija == None:
            self.regija = self.slovar[self.izbira][0]

#dodajanje kraja
    def zapis_oznak(self):
        if self.oznaka not in self.seznam_oznak:
            self.seznam_oznak.append(self.oznaka) 

    def zapis_kraja(self):
        self.stanje = None
        niz = ''
        for oznaka in self.seznam_oznak:
            if niz == '':
                nov_niz = oznaka
                niz = nov_niz
            else:
                nov_niz = niz + ',' + oznaka
                niz = nov_niz
        self.oznake = niz
            
        with open('ideje.txt', 'a') as f:
            print(';', file=f)
            print(self.izbira + ':' + self.regija + ',' + self.oznake ,file=f)








          
#za vsakega ime, regija, oznake, prebran opis, ogleda sliko

