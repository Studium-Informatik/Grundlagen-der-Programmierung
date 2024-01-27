---
tags:
  - WiSe_23-24
  - GDP
  - Übung
  - Präsenz
---
## 1.
### a)

```python
def inc(x):
	x = x + 1

a = 10
inc(a)
print(a)
```

es wird `10` ausgegeben, da die Funktion die Variable aus ihrem Stackframe nicht zurück gibt.

### b)

```python
def inc(x):
	x = x + 1
	return x

a = 10
a = inc(a)
print(a)
```

## 2.

## 3.
```python
def decToBin (n):
	binRep = "" 
	while n > 0:
		binRep = str(n % 2) + binRep
		n = n // 2 
	return binRep
```
Die Funktion wird solange ausgeführt wie n größer als 0 ist. Bei jeder Iteration wird der Rest der Division von `n` durch 2 wird dann vor den bisherigen Wert von `binRep` als String gesetzt. Danach wird n auf die Ganzzahlige Division mit 2 gesetzt.

## 4.
```python
def binToDec(n):
    decimal = 0
    binary_str = str(n)

    # Überprüfe, ob die Eingabe eine Binärzahl ist
    if not all(bit in '01' for bit in binary_str):
        raise ValueError("Ungültige Eingabe. Bitte geben Sie eine Binärzahl ein.")

    # Konvertiere die Binärzahl in Dezimal
    for i in range(len(binary_str)):
        decimal += int(binary_str[i]) * (2 ** (len(binary_str) - 1 - i))

    return decimal

def main():
    # Benutzer zur Eingabe einer Binärzahl auffordern
    binary_input = input("Geben Sie eine Binärzahl ein: ")

    try:
        # Dezimaldarstellung berechnen
        decimal_result = binToDec(binary_input)
        # Ausgabe der Dezimaldarstellung
        print(f"Die Dezimaldarstellung von {binary_input} ist {decimal_result}.")
    except ValueError as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()
```