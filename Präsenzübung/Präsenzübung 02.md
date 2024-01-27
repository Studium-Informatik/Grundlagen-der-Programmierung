---
tags:
  - WiSe_23-24
  - GDP
  - Übung
  - Präsenz
---
## 1.
```pseudo
\begin{algorithm}
\caption{Rest einer Ganzzahligen Division}
\begin{algorithmic}
  \Function{Remainder}{$dividend, divisor$}
    \If{$divisor = 0$}
      \State \textbf{return} "Nicht mögliche Division"
    \EndIf
    \State $quotient \gets \lfloor \frac{dividend}{divisor} \rfloor$  \Comment{Ganzzahl Division}
    \State $remainder \gets dividend - (quotient \times divisor)$
    \State \textbf{return} $remainder$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```


## 2.
```pseudo
\begin{algorithm}
\caption{ggT}
\begin{algorithmic}
  \Procedure{ggT}{$a, b$}
    \If{$a < b$}
      \State \Call{Swap}{$a, b$} \Comment{Vertausche a und b, falls a < b}
    \EndIf

    \While{$b > 0$}
      \State $q \gets \lfloor a / b \rfloor$ \Comment{Berechne den ganzzahligen Quotienten}
      \State $r \gets a \mod b$ \Comment{Berechne den Rest}
      \State $a \gets b$ \Comment{Ersetze a durch b}
      \State $b \gets r$ \Comment{Ersetze b durch r}
    \EndWhile

    \State \Return $a$ \Comment{Der ggT ist in a gespeichert}
  \EndProcedure
\end{algorithmic}
\end{algorithm}
```


## 3.
Karo < Herz < Pik < Kreuz
### 1.
Da beide Stapel sortiert sind, können wir jeweils die oberste Karte vergleichen. Hierbei suchen wir uns die kleinere Karte aus und legen sie mit dem Bild nach unten auf den Tisch. Danach wiederholen wir diesen Schritt bis keine Karten mehr übrig sind.
danach können wir den Stapel umdrehen und haben einen von oben nach unten sortierten Stapel.
### 2.
#### a)
```pseudo
\begin{algorithm}
\caption{WertSort}
\begin{algorithmic}
\Input  s1 Liste von Sortierten Karten, s2 Liste von Sortierten Karten, S leere Ausgabeliste
\Output none
  \Procedure{WertSort}{$s1, s2, S$}
    \If{\Call{Wert}{$s1$} $<$ \Call{Wert}{$s2$}}
		\State \Call{Lege}{$s1[1], S$}
	\Else
		\State \Call{Lege}{$s2[1], S$}
	\EndIf
  \EndProcedure
\end{algorithmic}
\end{algorithm}
```

#### b)
```pseudo
\begin{algorithm}
\caption{FarbSort}
\begin{algorithmic}
\Input  s1 Liste von Sortierten Karten, s2 Liste von Sortierten Karten, S leere Ausgabeliste
\Output none 
  \Procedure{FarbSort}{$s1, s2, S$}
    \If{\Call{Farbe}{$s1$[1]} $<$ \Call{Farbe}{$s2$[1]}}
	    \State \Call{Lege}{$s1[1], S$}
    \ElsIf{\Call{Farbe}{$s1$[1]} $>$ \Call{Farbe}{$s2$[1]}}
	    \State \Call{Lege}{$s2[1], S$}
    \Else
	    \State \Call{WertSort}{$s1, s2, S$}
	\EndIf
  \EndProcedure
\end{algorithmic}
\end{algorithm}
```

#### c)
```pseudo
\begin{algorithm}
\caption{Mischen}
\begin{algorithmic}
\Input  s1 Liste von Sortierten Karten, s2 Liste von Sortierten Karten
\Output Sortierte Zusammengefügte Liste 
  \Procedure{Mischen}{$s1, s2$}
	\State $S \gets Leere Liste$
    \While{$s1$ nicht leer und $s2$ nicht leer}
      \State \Call{FarbSort}{$s1$, $s2$, $S$}
    \EndWhile
    \While{$s1$ nicht leer}
      \State \Call{Lege}{$s1[1], S$}
    \EndWhile
    \While{$s2$ nicht leer}
      \State \Call{Lege}{$s2[1], S$}
    \EndWhile
    \Return $S$
  \EndProcedure
\end{algorithmic}
\end{algorithm}
```
