# Slovar naj bo v datoteki, ki jo preberemo

class Ideje:
    def __init__(self):
        self.slovar = {}
        self.nalozi_slovar_idej()

    def nalozi_slovar_idej(self):
        with open('ideje.txt') as f:
            vse_ideje = f.read()
            posebej = vse_ideje.split(';')
            for vse_za_kraj in posebej:
                ločeno = vse_za_kraj.split(':')
                nabor = ločeno[1].split(',')
                self.slovar[ločeno[0]] = tuple(nabor)


    def pozeni(self):
        self.vprasaj_po_regiji()
        if self.regija is None: # regije nismo nastavili
            pass

    def vprasaj_po_regiji(self):
        self.regija = None
        odlocitev = input('Imaš v mislih določeno regijo? Da/Ne')

        if odločitev == 'Da':
            # izbere gumb z eno od regij: Gorenjska, Dolenjska, Primorska, Koroška,
            # Štajerska, Notranjska, Prekmurje
            self.regija = input() #dobim s pritiskom gumba
            
            primerni_cilji = []
            for kraj in self.slovar.keys():
                if self.slovar[kraj][0] == iskana_regija:
                    primerni_cilji.append(kraj)
            print('Ideje: {}'.format(primerni_cilji))
           
        elif odločitev == 'Ne':
            print('Iščemo torej kraje iz cele Slovenije.')

        else:
            print('Odgovoriš lahko samo z Da ali Ne.')
            self.vprasaj_po_regiji()




            print('Želite nadaljevati iskanje glede na kategorije/ ključne besede?')
            nadaljujemo = input('Da/Ne')
            if nadaljujemo.strip() == 'Da':
                
                glede_na_oznake()
            else:
                print('Ideje: {}'.format(primerni_cilji))



    def prikaži(self):
        pass


        
i = Ideje()
i.pozeni()

#iskanje glede na kriterije:
def glede_na_regijo(slovar):
    odločitev = input('Imaš v mislih določeno regijo? Da/Ne')
    if odločitev == 'Da':
        # izbere gumb z eno od regij: Gorenjska, Dolenjska, Primorska, Koroška,
        # Štajerska, Notranjska, Prekmurje
        iskana_regija = input() #dobim s pritiskom gumba
        primerni_cilji = []
        for kraj in slovar.keys():
            if slovar[kraj][0] == iskana_regija:
                primerni_cilji.append(kraj)
        print('Ideje: {}'.format(primerni_cilji))
        
        print('Želite nadaljevati iskanje glede na kategorije/ ključne besede?')
        nadaljujemo = input('Da/Ne')
        if nadaljujemo.strip() == 'Da':
            
            glede_na_oznake()
        else:
            print('Ideje: {}'.format(primerni_cilji))
                  
    elif odločitev == 'Ne':
        print('Iščemo torej kraje iz cele Slovenije.')
        glede_na_oznake()
    else:
        print('Odgovoriš lahko samo z Da ali Ne.')
        glede_na_regijo(slovar)

#če že izberejo regijo se more narediti nov slovar samo s kraji iz tiste regije
def glede_na_oznake(izbira=[]):
    kategorija = input('Katero kategorijo oz. katero ključno besedo naj iščemo?')
    if kategorija in vse_oznake():
        shranjena_izbira = izbira
        nova_izbira = []
        for kraj in slovar.keys():
            if kategorija in oznake_kraja(kraj):
                if kraj not in nova_izbira:
                    nova_izbira.append(kraj)
        if shranjena_izbira != []:
            izbira = list(set(nova_izbira) & set(shranjena_izbira))
            print('Na podlagi kategorij: {}'.format(izbira))
            nova_izbira = izbira
            if izbira == []:
                print('Vašim kriterijem ne ustreza noben vnešen kraj.')
                print('Poskusite z drugačnimi.')
                glede_na_oznake()
        else:
            print('Na podlagi kategorij: {}'.format(nova_izbira))
            # v okvircku se izpisujejo beležijo kategorije

        dodamo_kategorijo = input('Razširimo iskanje s še kakšno kategorijo? Da/Ne')
        dodamo = dodamo_kategorijo.strip()
        if dodamo == 'Da':
            glede_na_oznake(nova_izbira)
        elif dodamo == 'Ne':
            print('Na podlagi kategorij: {}'.format(nova_izbira))
            pass
        else:
            print('Možna odgovora le Da ali Ne.')
            glede_na_oznake()
    #malo drugače

    else:
        oznake = vse_oznake()
        print('Se opravičujemo, vendar ta ključna beseda/kategorija ne obstaja.')
        print('Poskusite znova. Na voljo so vam naslednje kategorije:{}'.format(oznake))
        glede_na_oznake()

def vse_oznake():
    '''Seznam oznak brez ponavljanja'''
    slovar = naloži_slovar_idej()
    oznake = []
    for kraj in slovar.keys():
        za_en_kraj = list(slovar[kraj][1:])
        for oznaka in za_en_kraj:
            if oznaka not in oznake:
                oznake.append(oznaka)
    return oznake

def oznake_kraja(kraj):
    '''Seznam oznak enega kraja'''
    return list(slovar[kraj][1:])
        

def naštejemo_vse_kraje():
    '''Seznam krajev'''
    seznam_krajev = []
    for kraj in slovar.keys():
        seznam_krajev.append(kraj)
    return seznam_krajev

import random
def naključna_izbira():
    seznam_krajev = naštejemo_vse_kraje()
    return random.choice(seznam_krajev)

def priljubljeno(iskanja=0, iskane_oznake=[]):
#za iskanja se bo s klikom delal neviden števec do 20 pol pa kot da zmer vela
#ko odpreš kraj se v datoteko shranijo oznake
    if iskanja > 20:
        print('Ok')
        brez_ponovitev = []
        for oznaka in iskane_oznake:
            if oznaka not in brez_ponovitev:
                brez_ponovitev.append(oznaka)
        print(brez_ponovitev)
        pari = []
        for oznaka in brez_ponovitev:
            kolikokrat = iskane_oznake.count(oznaka)
            pari.append((-kolikokrat, oznaka))
            pari.sort()
        return pari[0][1]

#za prikaz kraja bo on vpisal Entry
#za vsakega ime, regija, oznake, prebran opis, prebrani komentarji, ogleda sliko
#kraj bo vnos.get ker to vrne niz
def prikaži_kraj(kraj):
    #v Label z velikimi ime kraja
    regija = ideje[kraj][0]
    oznake = oznake_kraja(kraj)

def prebrati_opis(kraj):
    ime_datoteke = kraj + 'txt'
    with open(ime_datoteke) as f:
        print(f.read())

def dodati_opis(kraj):
    ime_datoteke = kraj + 'txt'
    with open(ime_datoteke, 'w') as f:
        besedilo = input('Opis:')
        print(besedilo, file = f)
    
#komentarji, kaj če jih še ni!
def prebrati_komentar(kraj):
    ime_datoteke = kraj + 'kom.txt'
    with open(ime_datoteke) as f:
        print(f.read())

def dodati_komentar(kraj):
    ime_datoteke = kraj + 'kom.txt'
    with open(ime_datoteke, 'a') as f:
        komentar = input('Vaš komentar:')
        print('\n{} \n'.format(komentar), file=f)

def počisti_iskanje():
    pass

#gumb počisti iskanje da začne od začetka, lahko gumb ki pove koliko krajev v bazi
# spreminjam slovar samo lokalno: del ideje['Ljubljana']
#za sliko:import os
#         os.system('start slika.jpeg')
