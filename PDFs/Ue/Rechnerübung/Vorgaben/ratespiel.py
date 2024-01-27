#!/usr/bin/env python3.7
zahl = 23
weiter = True

while weiter:
	geraten = input("Bitte Zahl eingeben: ")
	if geraten == zahl:
		print("Richtig geraten!")
		weiter = False
	else:
		print("Falsch geraten")
