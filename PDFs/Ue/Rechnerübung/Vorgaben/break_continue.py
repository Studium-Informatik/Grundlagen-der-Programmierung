#!/usr/bin/env python
n = 0
while n >= 0:
	print("=== Schleifenblock beginnt ===")
	n = int(input("Ganze Zahl eingeben: n = "))
	if n == 0:
		break
	if n % 2 == 0:
		continue
	print ("Zahl ist ungerade")
	print ("=== Schleifenblock endet ===")
	input()
if n < 0:
	print("Negative Zahl eingegeben.")

print("Skript wird beendet.")
