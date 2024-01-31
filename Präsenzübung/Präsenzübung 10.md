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
3. STORE r4 [r1]    ; Store the value of r4 into 
```


