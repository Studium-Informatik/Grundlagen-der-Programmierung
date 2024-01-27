#!/usr/bin/env python3.7
def mischen(a, b):
	c = []
	pass
	return c
		
print("Bewaeltigen Sie alle Tests:\n")

print("Mischen zweier gleich grosser Stapel [1,3,5] und [2,4,6]")
L = mischen([5,3,1], [6,4,2])
print("Richtige Sortierung ist: [1, 2, 3, 4, 5, 6]")
print("Ihr Ergebnis lautet:	", L)
input()
print("Mischen zweier gleich grosser Stapel [7,8,9] und [1,2,6]")
L = mischen([9,8,7], [6,2,1])
print("Richtige Sortierung ist: [1, 2, 6, 7, 8, 9]")
print("Ihr Ergebnis lautet:	", L)
input()
print("Mischen zweier gleich grosser Stapel [2,7,10] und [8,9,10]")
L = mischen([10,7,2], [10,9,8])
print("Richtige Sortierung ist: [2, 7, 8, 9, 10, 10]")
print("Ihr Ergebnis lautet:	", L)
input()
print("Mischen zweier unterschiedlich grosser Stapel [1,1,5,5], [1,2,6]")
L = mischen([5,5,1,1], [6,2,1])
print("Richtige Sortierung ist: [1, 1, 1, 2, 5, 5, 6]")
print("Ihr Ergebnis lautet:	", L)
print()

