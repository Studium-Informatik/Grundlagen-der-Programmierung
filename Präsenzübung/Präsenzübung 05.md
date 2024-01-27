---
tags:
  - WiSe_23-24
  - GDP
  - Übung
  - Präsenz
---
# 1.
## 1.
### 1.
$f(n)=255n^3-19n^2+0,003n-1000$
#### a)
$f(n)\in O(n^3)$

#### b)
$f(n)\in \Omega(n^3)$
$f(n)\geq n^3$ für $n\geq 1$

### 2.

### 3.
$3n^2+30n+300=f(n)$
$4^n=g(n)$
$5+0,001n^3+0,0025n=h(n)$
$n^2+3n-3=j(n)$

## 2.
### Adjazenzliste:

Angenommen, der Graph hat |V| = n Knoten und |E| = m Kanten.

**Best Case (Leerer Graph):**

- Zeitkomplexität O(1), da der Ausgangsgrad jedes Knotens gleich null ist.

**Worst Case:**
- durchschnittliche Zeitkomplexität O(n)

### Adjazenzmatrix:

Angenommen, der Graph hat |V| = n Knoten.

**Best Case (Leerer Graph):**

- Zeitkomplexität O(1), da der Ausgangsgrad jedes Knotens gleich null ist.

**Worst Case:**
- durchschnittliche Zeitkomplexität $O(n^2)$.
## 3.
### 1.
#### ggt_1
##### Zeitkomplexität im worst Case
$O(max(x,y))$

##### Zeitkomplexität bezüglich der Bitlänge
$O(log_{2}(x) + log_{2}(y))$

#### ggt_2
##### Zeitkomplexität im worst Case
$O(x+y)$

##### Zeitkomplexität bezüglich der Bitlänge
$O(log_{2}(x) + log_{2}(y))$

-> 2^(n-1)
## 4.
Wenn $\mid xs\mid=n$
$O(n^2)$

Die Funktion findet das kleinste Element einer Liste
eine Bessere Darstellung der Funktion wäre:

```python
def findMin(xs):
	if(len(xs) == 0):
		return None
	min = xs[0]
	for i in xs:
		if(i < min):
			min = i
	return min
```

$O(n)$
