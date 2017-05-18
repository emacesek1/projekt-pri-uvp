from slovar_idej import ideje

#iskanje glede na kriterije:
def določimo_regijo():
    odločitev = input('Imaš v mislih določeno regijo? Da/Ne')
    if odločitev == 'Da':
        # izbere gumb z eno od regij: Gorenjska, Dolenjska, Primorska, Koroška,
        # Štajerska, Notranjska, Prekmurje
        iskana_regija = input() #dobim s pritiskom gumba
        primerni_cilji = []
        for kraj in ideje.keys():
            if ideje[kraj][0] == iskana_regija:
                primerni_cilji.append(kraj)

        print('Ideje: {}'.format(primerni_cilji))
        # funkcija kjer izberemo kraj iz tega seznama
        # ali dodamo dodatne kriterije
        # če je več idej od npr... ti ponudi ali želi da izpiše vse, koliko,
        # ali naključno, po vrstnem redu ali prve ali tiste, ki majo komentarje       

    elif odločitev == 'Ne':
        pass      
    else:
        print('Odgovoriš lahko samo z Da ali Ne.')
        določimo_regijo()

#če že izberejo regijo se more narediti nov slovar samo s kraji iz tiste regije
def glede_na_oznake(izbira=[]):
    kategorija = input('Katero kategorijo oz. katero ključno besedo naj iščemo?')
    if kategorija in vse_oznake():
        shranjena_izbira = izbira
        nova_izbira = []
        for kraj in ideje.keys():
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
    oznake = []
    for kraj in ideje.keys():
        za_en_kraj = list(ideje[kraj][1:])
        for oznaka in za_en_kraj:
            if oznaka not in oznake:
                oznake.append(oznaka)
    return oznake

def oznake_kraja(kraj):
    '''Seznam oznak enega kraja'''
    return list(ideje[kraj][1:])
        

def naštejemo_vse_kraje():
    '''Seznam krajev'''
    seznam_krajev = []
    for kraj in ideje.keys():
        seznam_krajev.append(kraj)
    return seznam_krajev

import random
def naključna_izbira():
    seznam_krajev = naštejemo_vse_kraje()
    return random.choice(seznam_krajev)

def priljubljeno(iskanja=0, iskane_oznake=[]):
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
    

        
        
#def način_prevoza()
#ker če izbere javni prevoz najdem še najbližjo avtobusno ali železniško postajo



# spreminjam slovar samo lokalno: del ideje['Ljubljana']
