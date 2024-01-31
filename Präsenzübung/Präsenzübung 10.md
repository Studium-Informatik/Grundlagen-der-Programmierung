### AASS-Befehle:
| Syntax | Beispiel | Wirkung |
| --- | --- | --- | 
| LOAD Register Mem  | LOAD r1 [4] | *r1 = Mem[4] |
| STORE Register Mem | STORE r1 [8] | Mem[8] = *r1 |
| SET Register Wert | SET r1 4 | *r1 = 4 |
| ADD Ziel Quellen | ADD r3 r1 r2 | *r3 = *r1 + *r2 |
| SUB Ziel Quellen | SUB r3 r1 r2 | *r3 = *r1 - *r2 |
| MUL Ziel Quellen | MUL r3 r1 r2 | *r3 = *r1 x *r2 |
| DIV Ziel Quellen | DIV r3 r1 r2 | *r3 = *r1 / *r2 |
| GOTO Wert | GOTO 7 | Befehlszähler = 7 |
| GOEQ | *r1 == *r2, dann Befehlszähler = 7, sonst um 1 erhöhen | GOEQ r1 r2 7 |
| GOLS | *r1 < *r2, dann Befehlszähler = 7, sonst um 1 erhöhen | GOLS r1 r2 7 |
| GOGR | *r1 > *r2, dann Befehlszähler = 7, sonst um 1 erhöhen | GOGR r1 r2 7 |
| GOLE | *r1 <= *r2, dann Befehlszähler = 7, sonst um 1 erhöhen | GOLE r1 r2 7 |
| GOGE | *r1 >= *r2, dann Befehlszähler = 7, sonst um 1 erhöhen | GOGE r1 r2 7 |
| GONE | *r1 != *r2, dann Befehlszähler = 7, sonst um 1 erhöhen | GONE r1 r2 7 |
| STOP | Programmende |  |
| # Text | Kommentar |  |


## 1.1
### 1.
```python
def f(a,b,c):
	res = a + b
	res = res + c
	res = res / 3
	return res

def f_short(a,b,c):
	return (a+b+c) / 3
```

### 2.
```python
def g(a,b):
	while (a => b){
		a = a - b
	}
	return a
```

## 1.2 Max
| Variable | res | a | b |
| ---- | ---- | ---- | ---- |
| Adresse | 1 | 2 | 3 |
```css
1. LOAD r1 [2]   ; Load the value of 'a' into register r1.
2. LOAD r2 [3]   ; Load the value of 'b' into register r2.
3. GOGR r1 r2 6  ; If a > b, go to line 5.
4. STORE r2 [1]  ; If a <= b, store b in 'res' and stop.
5. STOP          ; End of the program.
6. STORE r1 [1]  ; If a > b, store a in 'res'.
7. STOP          ; End of the program.
```


## 1.3 Swap
| Variable | a | b |
| ---- | ---- | ---- |
| Adresse | 1 | 2 |
```css
1. LOAD r3 [r1]     ; Load the value of Mem[r1] into register r3.
2. LOAD r4 [r2]     ; Load the value of Mem[r2] into register r4.
3. STORE r4 [r1]    ; Store the value of r4 into Mem[r1]
4. STORE r3 [r2]    ; Store the value of r3 into Mem[r2]
```


## 1.4 Fakultät
$fakul(n)=n\cdot(n-1)\cdot\dots\cdot(n-n+1)$

| Variable | res | n |
| ---- | ---- | ---- |
| Adresse | 1 | 2 |
```css
1. LOAD r2 [2]      ; Load the value of 'n' into r2
2. SET r1 1         ; Init r1 with value '1' 
3. GOLE r2 1 7      ; If r2 < 1, go to line 7.
4. MUL r1 r1 r2     ; Multiply r1 with r2 and save in r1
5. SUB r2 r2 1      ; Substract '1' from r2
6. GOTO 3           ; Return to line 3.
7. STORE r1 [1]     ; Save result in Mem[1]
```

## 1.5 Übersetzungsschemata
### 1.
```css
# aass(A)
# ... Code für Block A ...

# Bedingte Verzweigung, überprüft, ob a gleich b ist
LOAD r1 [a]     ; r1 = a
LOAD r2 [b]     ; r2 = b
GOEQ r1 r2 3    ; Wenn a == b, gehe zu Block B (Zeile 3)
GOTO 5          ; Sonst gehe zu Block C (Zeile 5)

# aass(B)
# ... Code für Block B ...
GOTO 6          ; Nach Block B, gehe zu Block D (Zeile 6)

# aass(C)
# ... Code für Block C ...

# aass(D)
# ... Code für Block D ...
```

### 2.
```css
# aass(A)
# ... Code für Block A ...

# Schleifenbeginn
1. LOAD r1 [a]   ; r1 = a
2. LOAD r2 [b]   ; r2 = b
3. GOLE r1 r2 5  ; Wenn a <= b, fahre mit Block B fort (Zeile 5)
4. GOTO 7        ; Sonst gehe zu Block C (Zeile 7)

# aass(B)
# ... Code für Block B ...
GOTO 1           ; Gehe zurück und überprüfe die Schleifenbedingung erneut

# aass(C)
# ... Code für Block C ...
```

### 3.
```css
1. # aass(A)

# Initialisiere den Index i und die Länge l
2. SET r1 0        ; r1 = i = 0 (Index für seq)
3. LOAD r2 [l]     ; r2 = l (Laden der Länge von seq)

# Schleifenbeginn
4. GOEQ r1 r2 10    ; Wenn i == l, beende die Schleife

# Lade das aktuelle Element von seq in r3
5. ADD r3 s r1     ; Berechne die Adresse des aktuellen Elements
6. LOAD r3 [r3]    ; Lade das aktuelle Element von seq in r3

7. # aass(B)

# Erhöhe den Index i und springe zurück zum Schleifenanfang
8. ADD r1 r1 1     ; r1 = i = i + 1
9. GOTO 4          ; Springe zurück zum Schleifenbeginn

10. # aass(C)
```