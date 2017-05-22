import tkinter as tk
okno1 = tk.Tk()

oznaka = tk.Label(okno1, text='Kam na izlet?'.upper())
oznaka.grid(row=0)

gumb1 = tk.Button(okno1, text='Iščem idejo')
gumb1.grid(row=1, column=2)

gumb2 = tk.Button(okno1, text='Dodal/-a bi nov kraj')
gumb2.grid(row=2, column=2)

gumb3 = tk.Button(okno1, text='Dodal/-a bi komentar')
gumb3.grid(row=3, column=2)

#lohk tud .grid(row= , column= )
#vnosno_polje.get() kar je v tk.Entry()
#button.config(state='disabled' or 'normal')

okno2 = tk.Tk()

oznaka = tk.Label(okno2, text='Kako bi želel začeti iskanje?')
oznaka.pack()

gumb21 = tk.Button(okno2, text='Glede na kriterije')
gumb21.pack()

gumb22 = tk.Button(okno2, text='Preseneti me z naključno izbiro')
gumb22.pack()

gumb23 = tk.Button(okno2, text='Priljubljeno')
gumb23.config(state='disabled')
gumb23.pack()

okno3 = tk.Tk()
vnos = tk.Entry(okno3)
vnos.pack()

#http://www.python-course.eu/tkinter_text_widget.php

