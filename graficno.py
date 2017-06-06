from iscem_idejo import Ideje
import tkinter as tk
import random

class Izgled:
    def __init__(self):
        self.i = Ideje()
        self.zacetno_okno()    

    def zacetno_okno(self):
        okno1 = tk.Tk()
        oznaka = tk.Label(okno1, text='Kam na izlet?'.upper())
        oznaka.grid(row=0)
        gumb1 = tk.Button(okno1, text='Iščem idejo', command = self.iscemo_idejo)
        gumb1.grid(row=1, column=2)
        gumb2 = tk.Button(okno1, text='Dodal/-a bi nov kraj')
        gumb2.grid(row=2, column=2)

    def iscemo_idejo(self):
        okno2 = tk.Tk()
        oznaka = tk.Label(okno2, text='Kako bi želel začeti iskanje?')
        oznaka.pack()
        gumb21 = tk.Button(okno2, text='Glede na regijo in oznake', command = self.iskanje_po_regijah_in_oznakah)
        gumb21.pack()
        gumb22 = tk.Button(okno2, text='Preseneti me z naključno izbiro', command = self.nakljucno_iskanje)
        gumb22.pack()
        gumb23 = tk.Button(okno2, text='Priljubljeno')
        gumb23.config(state='disabled')
        gumb23.pack()

    def nakljucno_iskanje(self):
        self.i.nakljucna_izbira()
        # odpremo novo okno in jo prikažemo, zraven lohk že kr ta kraj prikaže
        okno = tk.Tk()
        nalepka_o_izbiri = tk.Label(okno, text=self.i.izbira)
        nalepka_o_izbiri.pack()
        
    def iskanje_po_regijah_in_oznakah(self):
        self.okno_za_izbiro_regije = tk.Tk()

        vprasanje = tk.Label(self.okno_za_izbiro_regije, text='Imaš v mislih določeno regijo? Da/ne?')
        vprasanje.pack()
        gumb_da = tk.Button(self.okno_za_izbiro_regije, text='DA', command = self.regijsko_iskanje)
        gumb_da.pack()
        gumb_ne = tk.Button(self.okno_za_izbiro_regije, text='NE', command = self.z_oznakami)
        gumb_ne.pack()

    def regijsko_iskanje(self):
        self.okno_za_izbiro_regije.destroy()
        okno = tk.Tk()
        for regija in self.i.mozne_regije:
            def nastavi_regijo(r=regija):
                self.i.regija = r
                self.i.nalozi_slovar_idej()
                okno.destroy()
                self.nadaljuj_iskanje()
            gumb = tk.Button(okno, text=regija, command=nastavi_regijo)
            gumb.pack()

    def nadaljuj_iskanje(self):
        self.okno_za_nadaljne_iskanje = tk.Tk()

        vprasanje = tk.Label(self.okno_za_nadaljne_iskanje, text='Želiš nadaljevati iskanje glede na oznake/ ključne besede? Da/ne?')
        vprasanje.pack()
        gumb_da = tk.Button(self.okno_za_nadaljne_iskanje, text='DA', command = self.z_oznakami)
        gumb_da.pack()
        gumb_ne = tk.Button(self.okno_za_nadaljne_iskanje, text='NE', command = self.predstavi)
        gumb_ne.pack()

    def predstavi(self):
        print(self.i.regija)
        for kraj in self.i.slovar.keys():
            if self.i.slovar[kraj][0] == self.i.regija:
                self.i.primerni_cilji.append(kraj)
        print('Ideje: {}'.format(self.i.primerni_cilji))
        self.okno_za_nadaljne_iskanje.destroy()
        okno = tk.Tk()
        ustrezni_cilji = tk.Label(okno, text ='' )

    def z_oznakami(self):
        self.okno_za_nadaljne_iskanje.destroy()
        okno = tk.Tk()
        povemo = tk.Label(okno, text='Torej nadaljujemo iskanje glede na oznake/ ključne besede in iščemo kraje iz cele Slovenije.')
        povemo.pack()
        for oznaka in self.i.mozne_oznake:
            def nastavi_oznako(o=oznaka):
                self.i.oznaka = o
            gumb = tk.Button(okno, text=oznaka, command=nastavi_oznako)
            gumb.pack()
        self.i.vprasaj_po_oznakah()
        

Izgled()



#lohk tud .grid(row= , column= )
#vnosno_polje.get() kar je v tk.Entry()
#button.config(state='disabled' or 'normal')

##
##
##okno3 = tk.Tk()
##vnos = tk.Entry(okno3)
##vnos.pack()

#http://www.python-course.eu/tkinter_text_widget.php

