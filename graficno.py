from iscem_idejo import Ideje
from tkinter import *
import tkinter as tk
import random
import os

class Izgled:
    def __init__(self):
        self.i = Ideje()
        self.zacetno_okno()

    def zacetno_okno(self):
        prvo_okno = tk.Tk()
        oznaka = tk.Label(prvo_okno, text='Kam na izlet?'.upper())
        oznaka.grid(row=0)
        gumb1 = tk.Button(prvo_okno, text='Iščem idejo', command = self.iscemo_idejo)
        gumb1.grid(row=1, column=2)
        gumb2 = tk.Button(prvo_okno, text='Dodal/-a bi nov kraj')
        gumb2.grid(row=2, column=2)

    def iscemo_idejo(self):
        self.i.regija = None
        self.i.izbira = None
        self.i.seznam_oznak = []
        self.ustrezni_cilji = None
        self.i.primerni_cilji = []
        
        self.odlocitveno_okno = tk.Tk()
        oznaka = tk.Label(self.odlocitveno_okno, text='Kako bi želel začeti iskanje?')
        oznaka.pack()
        gumb1 = tk.Button(self.odlocitveno_okno, text='Glede na regijo in oznake', command = self.iskanje_po_regijah_in_oznakah)
        gumb1.pack()
        gumb2 = tk.Button(self.odlocitveno_okno, text='Preseneti me z naključno izbiro', command = self.nakljucno_iskanje)
        gumb2.pack()

        gumb3 = tk.Button(self.odlocitveno_okno, text='Priljubljeno', command=self.priljubljeno_iskanje)
        if self.i.stevilo_iskanih_oznak < 20:
            gumb3.config(state='disabled')
        gumb3.pack()

    def nakljucno_iskanje(self):
        self.i.nakljucna_izbira()
        self.odlocitveno_okno.destroy()
        
        self.okno_za_nakljucno = tk.Tk()
        nalepka_o_izbiri = tk.Label(self.okno_za_nakljucno, text=self.i.izbira)
        nalepka_o_izbiri.pack()

        prikaz = tk.Button(self.okno_za_nakljucno, text='Prikaži kraj', command=self.prikazi_kraj)
        prikaz.pack()

        znova_zacni = tk.Button(self.okno_za_nakljucno, text='Znova začnimo iskanje', command=self.zacnimo_znova)
        znova_zacni.pack()
        
    def iskanje_po_regijah_in_oznakah(self):
        self.odlocitveno_okno.destroy()
        self.okno_za_izbiro_regije = tk.Tk()

        vprasanje = tk.Label(self.okno_za_izbiro_regije, text='Imaš v mislih določeno regijo? Da/ne?')
        vprasanje.pack()
        self.gumb_da = tk.Button(self.okno_za_izbiro_regije, text='DA', command = self.regijsko_iskanje)
        self.gumb_da.pack()
        self.gumb_ne = tk.Button(self.okno_za_izbiro_regije, text='NE', command = self.z_oznakami)
        self.gumb_ne.pack()

    def regijsko_iskanje(self):
        for regija in self.i.mozne_regije:
            def nastavi_regijo(r=regija):
                self.i.regija = r
                self.i.nalozi_slovar_idej()
                self.okno_za_izbiro_regije.destroy()
                self.nadaljuj_iskanje()
            gumb = tk.Button(self.okno_za_izbiro_regije, text=regija, command=nastavi_regijo)
            gumb.pack()
            self.gumb_da.config(state='disabled')
            self.gumb_ne.config(state='disabled')

    def nadaljuj_iskanje(self):
        self.okno_za_nadaljne_iskanje = tk.Tk()

        vprasanje = tk.Label(self.okno_za_nadaljne_iskanje, text='Želiš nadaljevati iskanje glede na oznake/ ključne besede? Da/ne?')
        vprasanje.pack()
        gumb_da = tk.Button(self.okno_za_nadaljne_iskanje, text='DA', command = self.z_oznakami)
        gumb_da.pack()
        gumb_ne = tk.Button(self.okno_za_nadaljne_iskanje, text='NE', command = self.predstavi_za_regijo)
        gumb_ne.pack()

    def predstavi_za_regijo(self):
        self.okno_za_nadaljne_iskanje.destroy()
        self.i.poznamo_regijo()

        self.okno_z_oznakami = tk.Tk()
        self.prikaz_izbrane_oznake_in_krajev()
        self.pocisti.config(state='disabled')

    def z_oznakami(self):
        if self.i.stanje == None:
            if self.i.regija != None:
                self.okno_za_nadaljne_iskanje.destroy()
            elif self.i.regija == None:
                self.okno_za_izbiro_regije.destroy()
        
        self.okno_z_oznakami = tk.Tk()
        povemo = tk.Label(self.okno_z_oznakami, text='Torej nadaljujemo iskanje glede na oznake/ ključne besede in iščemo kraje iz cele Slovenije.')
        povemo.grid(column=0)
        for oznaka in self.i.mozne_oznake:
            def nastavi_oznako(o=oznaka):
                self.i.oznaka = o
                self.i.zapis_iskanih_oznak_v_dat()
                self.i.seznam_izbranih_oznak()
                if self.ustrezni_cilji != None:
                    self.ustrezni_cilji.destroy()
                self.prikaz_izbrane_oznake_in_krajev()
            gumb = tk.Button(self.okno_z_oznakami, text=oznaka, command=nastavi_oznako)
            gumb.grid(column=0)

            
    def prikaz_izbrane_oznake_in_krajev(self):
        if self.i.seznam_oznak != []:
            izbrane_oznake = tk.Label(self.okno_z_oznakami, text='Izbrane oznake: {}'.format(self.i.seznam_oznak))
            izbrane_oznake.grid(row=2, column=1)
            self.i.poznamo_oznake()

        if self.i.regija != None:
            izbrana_regija = tk.Label(self.okno_z_oznakami, text='Izbrana regija: {}'.format(self.i.regija))
            izbrana_regija.grid(row=3, column=1)
    
        self.ustrezni_cilji = tk.Label(self.okno_z_oznakami, text='Ideje: {}'.format(self.i.primerni_cilji))
        self.ustrezni_cilji.grid(row=4, column=1)
        self.i.primerni_cilji = []
            
        navodilo = tk.Label(self.okno_z_oznakami, text = 'V vnosno polje vpišite ime kraja, ki Vas zanima.')
        navodilo.grid(row=6, column=1)

        self.vnosno_polje = tk.Entry(self.okno_z_oznakami)
        self.vnosno_polje.grid(row=7, column=1)

        prikaz = tk.Button(self.okno_z_oznakami, text='Prikaži kraj', command=self.prikazi_kraj)
        prikaz.grid(row=8, column=1)

        self.pocisti = tk.Button(self.okno_z_oznakami, text='Počisti oznake', command=self.pocisti_oznake)
        self.pocisti.grid(row=10, column=1)
        if self.i.seznam_oznak == []:
            self.pocisti.config(state='disabled')

        znova_zacni = tk.Button(self.okno_z_oznakami, text='Znova začnimo iskanje', command=self.zacnimo_znova)
        znova_zacni.grid(row=11, column=1)

    def pocisti_oznake(self):
        self.i.pocisti_oznake()
        self.okno_z_oznakami.destroy()
        self.ustrezni_cilji = None
        self.z_oznakami()

    def zacnimo_znova(self):
        if self.i.seznam_oznak != [] or self.i.regija != None:
            self.okno_z_oznakami.destroy()
        else:
            self.okno_za_nakljucno.destroy()
        self.iscemo_idejo()

    def priljubljeno_iskanje(self):
        self.odlocitveno_okno.destroy()
        self.i.najveckrat_iskane()
        self.okno_z_oznakami = tk.Tk()
        self.prikaz_izbrane_oznake_in_krajev()
        self.pocisti.config(state='disabled')

    def prikazi_kraj(self):
        if self.i.izbira == None:
            self.i.izbira = self.vnosno_polje.get()
        self.i.preveri_regijo()
        
        self.okno_za_prikaz = tk.Toplevel()

        text1 = tk.Text(self.okno_za_prikaz)
        photo= PhotoImage(file='Bohinj.gif')
        text1.insert(END, self.i.izbira)
        text1.image_create(END, image=photo)
        text1.pack(side=LEFT)

        text2 = tk.Text(self.okno_za_prikaz)
        text2.insert(END, self.i.regija + '\n')
        text2.insert(END, self.i.oznake_kraja(self.i.izbira))
        text2.insert(END, '\nOpis kraja')
        text2.pack(side=LEFT)

        self.okno_za_prikaz.mainloop()
        




Izgled()




#http://www.python-course.eu/tkinter_text_widget.php

