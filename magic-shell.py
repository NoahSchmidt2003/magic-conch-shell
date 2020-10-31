from tkinter import *
import random
import time
import os


#definieren
gibab = ""
zahlen = (0,1,2,3,4,5,6,7,8,9,10)

#funktionen
def mach_es():
	computer = zahlen[random.randint(0,10)]
	if computer == 0:
		gibab = ("Ja auf jeden Fall.");
	if computer == 1:
		gibab = ("Nein eher nicht.");
	if computer == 2:
		gibab = ("Was ist das für eine Frage.");
	if computer == 3:
		gibab = ("Error Code 404 KI überlastet.");
	if computer == 4:
		gibab = ("Wieso nicht.");
	if computer == 5:
		gibab = ("Nein ganz sicher nicht.");
	if computer == 6:
		gibab = ("Warum das denn.");
	if computer == 7:
		gibab = ("Diese Frage kann ich nicht beantworten.")
	if computer == 8:
		gibab = ("Definitiv NEIN!");
	if computer == 9:
		gibab = ("Ein Fehler ist mit unterlaufen.");
	if computer == 10:
		gibab = ("Stelle deine Frage bitte nochmal :D")


	schreibrein.config(text=gibab)
	schreibrein.destroy
	schreibrein.grid(row=4, column=2)









root = Tk()
root.title("Magische Miesmuschel")
eingabe = Entry(root, width=20)
work = Button(root, text="Enter", command=mach_es)
titel=Label(root, text="Magische Miesmuschel", fg="black", bg="red", font="Arial")
schreibrein=Label(root, text="...")
#widgets platzieren


eingabe.grid(row=2, column=2)
work.grid(row=3, column=2)
titel.grid(row=0, column=2)


root.mainloop()






















	#Spiel
	#while spielen:
		#liste = "";
		#liste = (0,1,2,3,4,5,6,7,8,9,10);
		#computer = "";
		#antwort = "";
		#antwort = input("Wie lautet deine Frage?\n");
		#if (antwort == "stop"):
		#	spielen = False;
		#computer = liste[random.randint(0,10)]
		#answers()

