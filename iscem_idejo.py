import random
class Ideje:
    def __init__(self):
        self.regija = None
        self.mozne_regije = ['Gorenjska', 'Dolenjska', 'Primorska', 'Koroška', 'Štajerska', 'Notranjska', 'Prekmurje']
        self.slovar = {}
        self.nalozi_slovar_idej()
        self.izbira = None
        self.primerni_cilji = []
        self.mozne_oznake = self.vse_oznake()
#        self.preberemo_seznam_iskanih_oznak()
#        self.datoteka_z_oznakami()
        
    def nalozi_slovar_idej(self):
        if self.regija != None:
            nov_slovar = {}
            for kraj in self.slovar.keys():
                if self.slovar[kraj][0] == self.regija:
                       nov_slovar[kraj] = self.slovar[kraj]
            self.slovar = nov_slovar
        else:
            with open('ideje.txt') as f:
                vse_ideje = f.read()
                posebej = vse_ideje.split(';')
                for vse_za_kraj in posebej:
                    loceno = vse_za_kraj.split(':')
                    seznam = loceno[1].strip().split(',')
                    self.slovar[loceno[0].strip()] = tuple(seznam)
                
    def poisci_ideje(self):
        self.primerni_cilji = []
        self.vprasaj_po_regiji()
        if self.regija is None:
            self.vprasaj_po_oznakah()
        else: 
            self.nalozi_slovar_idej()
            self.nadaljujemo_iskanje()

    def vprasaj_po_regiji(self):
        self.odlocitev = input('Imaš v mislih določeno regijo? Da/Ne')
        if self.odlocitev == 'Da':
            # izbere gumb z eno od regij: Gorenjska, Dolenjska, Primorska, Koroška,
            # Štajerska, Notranjska, Prekmurje
            self.regija = input() #dobim s pritiskom gumba
            for kraj in self.slovar.keys():
                if self.slovar[kraj][0] == self.regija:
                    self.primerni_cilji.append(kraj)
            print('Ideje: {}'.format(self.primerni_cilji))
           
        elif self.odlocitev == 'Ne':
            print('Iščemo torej kraje iz cele Slovenije.')

        else:
            print('Odgovoriš lahko samo z Da ali Ne.')
            self.vprasaj_po_regiji()


    def nadaljujemo_iskanje(self):
        print('Želite nadaljevati iskanje glede na oznake/ ključne besede?')
        nadaljujemo = input('Da/Ne')
        if nadaljujemo == 'Da':
            self.vprasaj_po_oznakah()
        else:
            self.izbira = self.primerni_cilji
            print('Ideje: {}'.format(self.izbira))

    def vprasaj_po_oznakah(self):
##      self.oznaka = input('Katero kategorijo oz. katero ključno besedo naj iščemo?')
        nova_izbira = []
        for kraj in self.slovar.keys():
            if self.oznaka in self.oznake_kraja(kraj):
                if kraj not in nova_izbira:
                    nova_izbira.append(kraj)
                    
        if self.izbira != None:
            izbira = list(set(nova_izbira) & set(self.izbira))
            self.izbira = izbira
            print('Na podlagi oznak: {}'.format(self.izbira))
            if self.izbira == []:
                print('Vašim kriterijem ne ustreza noben vnešen kraj.')
                print('Poskusite znova z drugačnimi.')
                self.izbira = None
                self.vprasaj_po_oznakah()
            self.dodamo_vec_oznak()
        else:
            self.izbira = nova_izbira
            print('Na podlagi oznak: {}'.format(self.izbira))
            self.dodamo_vec_oznak()


    def dodamo_vec_oznak(self):
        dodamo_oznako = input('Razširimo iskanje s še kakšno kategorijo? Da/Ne')
        if dodamo_oznako == 'Da':
            self.vprasaj_po_oznakah()
        elif dodamo_oznako == 'Ne':
            print('Na podlagi oznak: {}'.format(self.izbira))
        else:
            print('Možna odgovora le Da ali Ne.')
            self.vprasaj_po_oznakah()
      
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
        return list(self.slovar[kraj][1:])


    def nakljucna_izbira(self):
        self.izbira = random.choice(self.nastejemo_vse_kraje())
            
    def nastejemo_vse_kraje(self):
        '''Seznam krajev'''
        seznam_krajev = []
        for kraj in self.slovar.keys():
            seznam_krajev.append(kraj)
        return seznam_krajev

    def datoteka_z_oznakami(self):
        if self.iskane_oznake == []:
            with open('iskane_oznake.txt', 'w') as f:
                None

    def osvezimo_seznam_iskanih_oznak(self):
        with open('iskane_oznake.txt', 'a') as f:
            if self.iskane_oznake == []:
                print('{}'.format(self.oznaka), file = f)
            else:
                print(',{}'.format(self.oznaka), file = f)

##    def preberemo_seznam_iskanih_oznak(self):
##        with open('iskane_oznake.txt') as f:
##            if f.read() == '':
##                self.iskane_oznake = []
##            else:
##                self.iskane_oznake = []
##                seznam_oznak = f.read().split(',')
##                for beseda in seznam_oznak:
##                    self.iskane_oznake.append(beseda.strip())

    def priljubljeno(self):
        if len(self.iskane_oznake) > 10:
            brez_ponovitev = []
            for oznaka in self.iskane_oznake:
                if oznaka not in brez_ponovitev:
                    brez_ponovitev.append(oznaka)
            pari = []
            for oznaka in brez_ponovitev:
                kolikokrat = self.iskane_oznake.count(oznaka)
                pari.append((-kolikokrat, oznaka))
                pari.sort()
            self.oznaka = pari[0][1]
            self.izbira = []
            for kraj in self.slovar.keys():
                if self.oznaka in self.oznake_kraja(kraj):
                    self.izbira.append(kraj)

def dodamo_kraj():
    with open('ideje.txt', 'a') as dat:
        ime = input('Ime kraja:') #preveri naj če že obstaja kraj v slovarju
        regija = input('Regija tvojega kraja?') #gumbki
        oznake = input() #gumbki
        print(';', file = dat)
        print('{}:{},{}'.format(ime, regija, oznake), file = dat)

class Kraj:
    def __init__(self, ime):
        self.ime = ime
        self.vsebina_v_slovarju()
        self.regija = self.vsebina[0]
        self.oznake = self.vsebina[1:]
        self.opis_kraja()

    def vsebina_v_slovarju(self):
        with open('ideje.txt') as f:
            vse_ideje = f.read()
            posebej = vse_ideje.split(';')
            for vse_za_kraj in posebej:
                if self.ime in vse_za_kraj:
                    loceno = vse_za_kraj.split(':')
                    self.vsebina = tuple(loceno[1].split(','))

    def opis_kraja(self):
        ime_datoteke = self.ime + '.txt'
        with open(ime_datoteke) as f:
            self.opis = f.read()


def dodati_opis(kraj):
    ime_datoteke = kraj + 'txt'
    with open(ime_datoteke, 'w') as f:
        besedilo = input('Opis:')
        print(besedilo, file = f)

def pocisti_iskanja():
    pass
           
#za nov kraj samo da se vpiše v datoteko
#za prikaz kraja bo on vpisal Entry
#za vsakega ime, regija, oznake, prebran opis, prebrani komentarji, ogleda sliko
#kraj bo vnos.get ker to vrne niz

#gumb počisti iskanje da začne od začetka, lahko gumb ki pove koliko krajev v bazi
# spreminjam slovar samo lokalno: del ideje['Ljubljana']
#za sliko:import os
#         os.system('start slika.jpeg')

##i = Ideje()
##i.poisci_ideje()


