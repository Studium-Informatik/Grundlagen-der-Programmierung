# Lernziele GdP: Was sollte ich für die Klausur können? (Repetitorium)
## 4) Algorithmisches Denken, Pseudocode

- Ich kann in Pseudocode gegebene Algorithmen implementieren ("verfeinern").

- Ich kann zu einer gegebenen Problemstellung einen Algorithmus entwerfen und in Pseudocode beschreiben.

- Ich kann algorithmische Grundkonzepte (Variable, Bedingung, Zuweisung, Sequenz, Fallunterscheidung, Wiederholung) erläutern.

- Ich kann den Programmablauf von in Pseudocode gegebenen Algorithmen beschreiben.

  

## 5) Modelle, Graphen, Brute-Force

- Eigenschaften von Graphen erläutern (Adjazenz, Zusammenhängend, Gewichtet, Gerichtet, Zyklus, Kreis, Schlingenfrei, Grad, etc)

- Repräsentation von Graphen zeichnen und überführen (Graph <-> Matrix <-> Liste)

- Pseudocode zu Graphen erstellen: Abstand von Knoten ...

- Idee des Brute Force Algorithmus erklären können

  

## 6) Imperative Programmierung

- Pseudocode in Python implementieren.

- Grundverständnis von Pythoncode (Schleifen,Fallunterscheidungen,Sequenzen,Ausdrücke,Operationen: Mathematisch und Listen und Logische) unterscheiden und erläutern können.

- Mit verschiedenen Datentypen(Listen, Boolsche Ausdrücke,Tupel, Integer, Strings) arbeiten, beschreiben, identifizieren können.

- einfache algorithmische Konzepte erläutern und entwickeln können.

  

## 7) Prozedurale Programmierung

- Imperative Programmierung: Pseudocode in Pythoncode schreiben (GGT, Liste aller Teiler sowohl in Pseudocode und als auch in Python schreiben)

- Prozeduren und Funktionen schreiben und anwenden können 

- Prozeduren verwalten können

- Wie kann der Interpreter die Variablen der Funktion von den sonstigen Programmvariablen unterscheiden?

- Aufrufstack(vereinfacht) 

- Wann kann eine Funktion berechnbar sein?

- formalle Parameter Vs. aktuelle Parameter

- Referenzen(Wertzuweisung, Änderungen der Variablenwerte)

- Wie treten Seiteneffekte auf?

- Module und import-Anweisungen

  

## 8) Ressourcen/Effizienz

- ich kann die drei möglichen Szenarien abschätzen: best case, worst case, average case 

- Interpretation der Effizienz eines Algorithmus in Pseudocode( Zeitkomplexität)

- Ich kann das Wachstum von Funktionen einordnen und vergleichen

- obere und untere Schranke einer gegebenen Funktion bestimmen oder zeigen

  

## 9) BFS, DFS

- Ich kann die Konzepte von Queue und Stack erklären und verstehe die zusammenhängenden Operationen.

- Ich kann das kleine-Welt Problem/Freundschaftsprobelm erklären und kann es auf andere Themengebiete anwenden.

- Ich verstehe Breadth-First-Search / Breitensuche (BFS) und Depth-First-Search / Tiefensuche (DFS), kenne die Unterschiede und weiß, wann ich welche Suche anwende

- Ich kann eine Aussage zur Laufzeitkomplexität von BFS und DFS geben.

- Ich kann Graphen zeichnen und als Adjazenzlisten und Adjazenzmatrix repräsentieren.

  

## 10) OO-Programmierung

- Ich verstehe die Grundbegriffe des Themenbereiches (Objekte, Klassen, Attribute, Methoden, self)

- Ich verstehe den Grundgedanken der Objektorientierten Programmierung

- ~~Ich kann die Vorteile und Nachteile Objektorienterter Programmierung für ein gegebenes Programm erkennen und erklären~~

- Ich kann eine Klasse mithilfe eines Konstruktors definieren

- Ich kann mit Objeten und Klassen umgehen (Verändern, erstellen, auslesen, vergleichen)

-   
    

## 11) Objekte & Referenzen, funktionale Programmierung

- Ich verstehe den Unterschied zwischen Identität und Gleichheit (Definition und im Code)

- Ich kenne die Operatormethoden der funktionalen Programmierung.

- Ich kann eine Klasse erstellen und neue Objekte erzeugen.

- Ich kann die Grundidee der funktionalen Programmierung wiedergeben.

- Ich kann verschiedene Definitions- und Wertebereiche bestimmen sowie deren Datentypen (OOP)

- Ich kann Funktionen definieren und aufrufen. 

- Ich kann iteration von Rekursion unterscheiden und anwenden 

- Ich kann Funktionen höherer Ordnung erkennen und ihren Grad angeben. 

- Ich kann Funktionen höherer Ordnung implementieren. 

- Ich kann Definitions- und Wertebereich höherer Funktionen benennen. 

- Ich kann Funktionen als anonyme Funktionen angeben.

- Ich kann lambda und def unterscheiden. 

  

## 12) Sequenzen, Currying, Stile

- Ich verstehe wie ich Funktionen höherer Ordnung (map, filter, reduce) benutze.

- Ich kann zwischen den verschiedenen Programmierstilen unterscheiden.

- Ich verstehe die Funktionsweise von Links- und Rechtssequenzen.

- Ich kann mehrstellige in einstellige Funktionen überführen.

  

## 13) Assembler, Interpreter, Compiler

- Ich kann Programme in AASS formulieren.

- Ich kann die Funktion eines gegebenen AASS-Programms interpretieren.

- Ich kann den Unterschied zwischen Interpreter und Compiler erkennen und beschreiben.

- Ich kann den Unterschied zwischen Syntax und Semantik erkennen und beschreiben.

- ~~Ich kann Fehlerarten in einem Programm erkennen.~~

  

## 14) Berechenbarkeit & Abzählbarkeit 

- Ich kann abzählbar unendlich und überabzählbar unendlich voneinander unterscheiden

- Ich kann beweisen, dass zwei Mengen gleichmächtig sind

- Ich kann mit der Diagonalisierung zeigen, dass eine Menge überabzählbar unendlich ist

## 15) Unentscheidbarkeit

- Ich kann jeweils ein Beispiel für ein Entscheidbares und Unentscheidbares Problem nennen 

- Ich kann erklären warum das Halteproblem unentscheidbar ist

- Ich kann erkennen ob ein Problem Entscheidbar ist oder nicht, und erklären warum

# 2
## 2

## 3
### 1
```pseudo
\begin{algorithm}
\caption{Counting Bidirectional Edges}
\begin{algorithmic}
\Input Vertex list $V$ and edge matrix $E$
\Output Count of bidirectional edges in the graph represented by $V$ and $E$
  \Function{CountBidirectionalEdges}{$V, E$}
    \State $count \gets 0$
    \For{$x \gets 0$ \textbf{to} \textbf{length of} $V$}
      \For{$y \gets x+1$ \textbf{to} \textbf{length of} $V$}
        \If{$V[x][y]$ \textbf{and} $V[y][x]$}
          \State $count \gets count + 1$
        \EndIf
      \EndFor
    \EndFor
    \State \textbf{return} $count$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```
```python
def uniCount(V, E):
	count = 0
	for x in range(len(V)):
		for y in range(1 + x, len(V)):
			if V[x][y] and not 
			
			V[y][x]:
				count += 1			
```

## 4
### 1
```tikz
\begin{document}
\begin{tikzpicture}[node distance={15mm}, main/.style = {draw, circle}] 
\node[main] (a) {$a$}; 
\node[main] (b) [above right of=a] {$b$};
\node[main] (c) [right of=a] {$c$};
\node[main] (d) [right of=b] {$d$};
\node[main] (e) [below of=c] {$e$};
\node[main] (f) [right of=d] {$f$};

\draw (a) -- (b);
\draw (a) -- (c);
\draw (a) -- (e);
\draw (b) -- (a);
\draw (b) -- (c);
\draw (b) -- (d);
\draw (c) -- (a);
\draw (c) -- (b);
\draw (d) -- (b);
\draw (d) -- (e);
\draw (d) -- (f);
\draw (e) -- (a);
\draw (e) -- (d);
\draw (f) -- (d);
\end{tikzpicture}
\end{document}
```
### 2
Ja
z.B. $f\to d\to c\to a\to c\to b$
### 3
$a\to b\to d\to e\to a$
### 4
3
### 5
$b\to a\to c\to d\to e\to f$
### 6
$b\to a\to c\to e\to d\to f$
## 5
### 1
$O(n²)$
### 2
$44n^5-40n^4-2n^2-30\leq n^5$
$44n^5-40n^4-2n^2\leq c\cdot n^5+30$
