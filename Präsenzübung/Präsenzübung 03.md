---
tags:
  - WiSe_23-24
  - GDP
  - Übung
  - Präsenz
---
## 1.
### 1.
#### a)
```run-python
#Input: `graph` (Adjazenzliste repräsentiert als Dictionary), `node` (der vorgegebene Knoten)
#Output: Die Anzahl der ausgehenden Kanten des vorgegebenen Knotens.

def outgoing_degree_adjacency_list(graph, node):
    if node not in graph:
        return "Knoten nicht im Graphen gefunden"
    return len(graph[node])

# Beispielaufruf:
# graph = {'A': ['B', 'C'], 'B': ['C'], 'C': []}
# node = 'A'
# print(outgoing_degree_adjacency_list(graph, node))
```

```pseudo
\begin{algorithm}
\caption{Ausgangsgrad eines Knotens (Adjazenzliste)}
\begin{algorithmic}
\Input Gerichteter Graph in Adjazenzlistenrepräsentation, vorgegebener Knoten im Graphen.
\Output Anzahl der Kanten, die vom gegebenen Knoten ausgehen.

  \Function{OutgoingDegreeAdjacencyList}{$graph, node$}
    \If{$node$ \textbf{not in} $graph$}
      \State \textbf{return} "Knoten nicht im Graphen gefunden"
    \EndIf
    \State \textbf{return} \textbf{length of} $graph[node]$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

#### b)
```run-python
#Input: `matrix` (Adjazenzmatrix repräsentiert als Liste von Listen), `node` (der vorgegebene Knoten)
#Output: Die Anzahl der ausgehenden Kanten des vorgegebenen Knotens.

def outgoing_degree_adjacency_matrix(matrix, node):
    if node >= len(matrix) or node < 0:
        return "Ungültiger Knotenindex"
    return sum(1 for edge in matrix[node] if edge == 1)

# Beispielaufruf:
# matrix = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
# node = 0
# print(outgoing_degree_adjacency_matrix(matrix, node))
```

```pseudo
\begin{algorithm}
\caption{Ausgangsgrad eines Knotens (Adjazenzmatrix)}
\begin{algorithmic}
\Input Gerichteter Graph in Adjazenzmatrixrepräsentation, vorgegebener Knotenindex im Graphen.
\Output Anzahl der Kanten, die vom gegebenen Knoten in der Adjazenzmatrix ausgehen.
  \Function{OutgoingDegreeAdjacencyMatrix}{$matrix, node$}
    \If{$node \geq$ \textbf{length of} $matrix$ \textbf{or} $node < 0$}
      \State \textbf{return} "Ungültiger Knotenindex"
    \EndIf
    \State \textbf{return} \textbf{sum of} $1$ \textbf{for} $edge$ \textbf{in} $matrix[node]$ \textbf{if} $edge = 1$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

#### c)
```run-python
#Input: `graph` (Adjazenzliste repräsentiert als Dictionary)
#Output: Ein Dictionary, das jedem Knoten seinen Eingangsgrad zuordnet.

def incoming_degrees_adjacency_list(graph):
    incoming_degrees = {node: 0 for node in graph}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            incoming_degrees[neighbor] += 1
    return incoming_degrees

# Beispielaufruf:
# graph = {'A': ['B', 'C'], 'B': ['C'], 'C': []}
# print(incoming_degrees_adjacency_list(graph))
```

```pseudo
\begin{algorithm}
\caption{Eingangsgrade aller Knoten (Adjazenzliste)}
\begin{algorithmic}
\Input Gerichteter Graph in Adjazenzlistenrepräsentation.
\Output Dictionary, das jedem Knoten im Graphen den Eingangsgrad zuweist.
  \Function{IncomingDegreesAdjacencyList}{$graph$}
    \State $incoming\_degrees \gets$ \textbf{dictionary} \textbf{with} $node: 0$ \textbf{for} $node$ \textbf{in} $graph$
    \For{$node, neighbors$ \textbf{in} $graph$}
      \For{$neighbor$ \textbf{in} $neighbors$}
        \State $incoming\_degrees[neighbor] \mathrel{+}= 1$
      \EndFor
    \EndFor
    \State \textbf{return} $incoming\_degrees$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

### 2.
#### a)
Der Komplementärgraph eines ungerichteten Graphen ist ein neuer Graph, bei dem jede nicht vorhandene Kante im ursprünglichen Graphen zu einer Kante wird und umgekehrt. Anders ausgedrückt, im Komplementärgraphen sind genau die Kanten vorhanden, die im Originalgraphen fehlen, und umgekehrt.

**Beispiel:** Betrachten wir einen ungerichteten Graphen G mit vier Knoten {A, B, C, D} und den Kanten {{A, B}, {B, C}, {C, D}}. Der Komplementärgraph G' enthält genau die Kanten, die in G fehlen, und keine der vorhandenen Kanten. In diesem Fall wäre G' = {{A, C}, {A, D}, {B, D}}.


```tikz
\begin{document}
\begin{tikzpicture}
% Ungerichteter Graph G
\foreach \pos/\name in {{(0,0)/A}, {(2,0)/B}, {(0,2)/C}, {(2,2)/D}} {
    \node[circle,draw,minimum size=0.6cm] (\name) at \pos {$\name$};
}

\foreach \source/\target in {{A/B}, {B/C}, {C/D}} {
    \draw (\source) -- (\target);
}

% Komplementärgraph G'
\begin{scope}[xshift=7cm]
\foreach \pos/\name in {{(0,0)/A}, {(2,0)/B}, {(0,2)/C}, {(2,2)/D}} {
    \node[circle,draw,minimum size=0.6cm] (\name) at \pos {$\name$};
}

\foreach \source/\target in {{A/C}, {A/D}, {B/D}} {
    \draw (\source) -- (\target);
}
\end{scope}
\end{tikzpicture}
\end{document}
```

#### b)
```run-python
# Input: original_matrix (Adjazenzmatrix)
# Output: complement_matrix (Adjazenzmatrix des Komplementärgraphen)
def complement_adjacency_matrix(original_matrix):
    size = len(original_matrix)
    complement_matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            complement_matrix[i][j] = 1 - original_matrix[i][j]

    return complement_matrix

# Beispielaufruf:
# original_matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
# print(complement_adjacency_matrix(original_matrix))
```

```pseudo
\begin{algorithm}
\caption{Adjazenzmatrix des Komplementärgraphen}
\begin{algorithmic}
\Input Adjazenzmatrix des ursprünglichen ungerichteten Graphen
\Output Adjazenzmatrix des Komplementärgraphen
  \Function{ComplementAdjacencyMatrix}{$original\_matrix$}
    \State $size \gets$ \textbf{length of} $original\_matrix$
    \State $complement\_matrix \gets$ \textbf{create matrix} \textbf{with} $0$ \textbf{rows and} $size$ \textbf{columns}

    \For{$i$ \textbf{in range} $size$}
      \For{$j$ \textbf{in range} $size$}
        \State $complement\_matrix[i][j] \gets 1 - original\_matrix[i][j]$
      \EndFor
    \EndFor

    \State \textbf{return} $complement\_matrix$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

## 2.
### 1.
#### a) Algorithmus zur Überprüfung nicht-trivialer Teiler:
```pseudo
\begin{algorithm}
\caption{Überprüfung nicht-trivialer Teiler}
\begin{algorithmic}
  \Function{HasNonTrivialDivisor}{$i$}
    \If{$i \leq 1$}
      \State \textbf{return} \textbf{false} \Comment{1 ist keine Primzahl}
    \EndIf
    
    \For{$j \gets 2$ \textbf{to} $i$}
      \If{$i$ \textbf{mod} $j = 0$}
        \State \textbf{return} \textbf{true} \Comment{$i$ hat nicht-trivialen Teiler}
      \EndIf
    \EndFor

    \State \textbf{return} \textbf{false} \Comment{$i$ hat keine nicht-trivialen Teiler}
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

#### b) Algorithmus zur Erstellung einer Liste von Primzahlen:
```pseudo
\begin{algorithm}
\caption{Erstellung einer Liste von Primzahlen bis N}
\begin{algorithmic}
  \Function{GeneratePrimeList}{$N$}
    \State $prime\_list \gets$ \textbf{empty list}
    
    \For{$i \gets 2$ \textbf{to} $N$}
      \If{\textbf{not} \Call{HasNonTrivialDivisor}{$i$}}
        \State \Call{Append}{$prime\_list, i$} \Comment{$i$ ist eine Primzahl}
      \EndIf
    \EndFor

    \State \textbf{return} $prime\_list$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```
### 2.
#### a) Sieb des Eratosthenes - Algorithmus in Pseudocode:
```pseudo
\begin{algorithm}
\caption{Sieb des Eratosthenes}
\begin{algorithmic}
  \Function{EratosthenesSieve}{$N$}
    \State $prime\_list \gets$ \textbf{empty list}
    \State $is\_prime \gets$ \textbf{list of size} $N+1$ \textbf{initialized with} \textbf{true}
    
    \For{$i \gets 2$ \textbf{to} $\sqrt{N}$}
      \If{$is\_prime[i]$}
        \For{$k \gets i^2$ \textbf{to} $N$ \textbf{step} $i$}
          \State $is\_prime[k] \gets$ \textbf{false}
        \EndFor
      \EndIf
    \EndFor
    
    \For{$i \gets 2$ \textbf{to} $N$}
      \If{$is\_prime[i]$}
        \State \Call{Append}{$prime\_list, i$}
      \EndIf
    \EndFor

    \State \textbf{return} $prime\_list$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

#### b) Optimierung des Sieb des Eratosthenes:

Um die Anzahl der Berechnungen zu reduzieren, können wir die äußere Schleife (für $i$) bis $\sqrt{N}$ beschränken, da alle nicht markierten zusammengesetzten Zahlen bereits vorher als Vielfache kleinerer Primzahlen gestrichen werden. Zusätzlich können wir die innere Schleife (für $k$) von $i^2$ beginnen lassen, da alle vorherigen Vielfachen bereits von kleineren Primzahlen gestrichen wurden.

```pseudo
\begin{algorithm}
\caption{Optimiertes Sieb des Eratosthenes}
\begin{algorithmic}
  \Function{OptimizedEratosthenesSieve}{$N$}
    \State $prime\_list \gets$ \textbf{empty list}
    \State $is\_prime \gets$ \textbf{list of size} $N+1$ \textbf{initialized with} \textbf{true}
    
    \For{$i \gets 2$ \textbf{to} $\sqrt{N}$}
      \If{$is\_prime[i]$}
        \For{$k \gets i^2$ \textbf{to} $N$ \textbf{step} $i$}
          \State $is\_prime[k] \gets$ \textbf{false}
        \EndFor
      \EndIf
    \EndFor
    
    \For{$i \gets 2$ \textbf{to} $N$}
      \If{$is\_prime[i]$}
        \State \Call{Append}{$prime\_list, i$}
      \EndIf
    \EndFor

    \State \textbf{return} $prime\_list$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

