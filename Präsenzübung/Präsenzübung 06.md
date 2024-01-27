---
tags:
  - WiSe_23-24
  - GDP
  - Übung
  - Präsenz
---
## .1
#### Adjazenzliste:
     - CGN: FRA, PAD
     - FRA: CGN, MUC, STR
     - KEL: STR
     - MUC: KEL
     - PAD: KEL
     - BER: HAM
     - STR: FRA
     - HAM: BER

#### Adjazenzmatrix:
   |    | CGN | FRA | KEL | MUC | PAD | BER | STR | HAM |
   |----|-----|-----|-----|-----|-----|-----|-----|-----|
   | CGN|  0  |  1  |  0  |  0  |  1  |  0  |  0  |  0  |
   | FRA|  1  |  0  |  0  |  1  |  0  |  0  |  1  |  0  |
   | KEL|  0  |  0  |  0  |  0  |  0  |  0  |  1  |  0  |
   | MUC|  0  |  0  |  1  |  0  |  0  |  0  |  0  |  0  |
   | PAD|  0  |  0  |  1  |  0  |  0  |  0  |  0  |  0  |
   | BER|  0  |  0  |  0  |  0  |  0  |  0  |  0  |  1  |
   | STR|  0  |  1  |  0  |  0  |  0  |  0  |  0  |  0  |
   | HAM|  0  |  0  |  0  |  0  |  0  |  1  |  0  |  0  |

## .2
### Breitensuche:
   ```
   BFS(Graph, Start):
      Initialize empty queue Q
      Initialize empty set visited
      Enqueue Start into Q
      Add Start to visited set
      
      while Q is not empty:
         current = Dequeue from Q
         Process current node
         
         for neighbor in neighbors of current:
            if neighbor is not in visited:
               Enqueue neighbor into Q
               Add neighbor to visited set
   ```

### Tiefensuche:
   ```
   DFS(Graph, Start):
      Initialize empty stack S
      Initialize empty set visited
      Push Start onto S
      
      while S is not empty:
         current = Pop from S
         Process current node
         
         for neighbor in neighbors of current:
            if neighbor is not in visited:
               Push neighbor onto S
               Add neighbor to visited set
   ```



```pseudo
\begin{algorithm}
\caption{Depth-first search auf einem gerichteten Graphen}
\begin{algorithmic}
  \Procedure{DFS}{$Graph, Start$}
    \State Initialize empty stack $S$
    \State Initialize empty stack $ALL$
    \State Initialize empty set $visited$
    \State Push $Start$ onto $S$

    \While{$S$ is not empty}
      \State $current \gets$ Pop from $S$

      \For{$neighbor$ in neighbors of $current$}
        \If{$neighbor$ is not in $visited$}
          \State Push $neighbor$ onto $S$
          \State Push $neighbor$ onto $ALL$
          \State Add $neighbor$ to $visited$ set
        \EndIf
      \EndFor
    \EndWhile
  \EndProcedure
\end{algorithmic}
\end{algorithm}
```

## .3
   - *Breitensuche (Start: BER):* BER, HAM
   - *Breitensuche (Start: FRA):* FRA, CGN, MUC, STR, PAD, KEL, BER, HAM
   - *Tiefensuche (Start: BER):* BER, HAM
   - *Tiefensuche (Start: FRA):* FRA, MUC, KEL, STR, PAD, CGN, HAM, BER
   - *Vergleich:*
      a) Reihenfolge der Knoten: Unterschiedlich
      b) Entwicklung von Queue/Stack: Breitensuche nutzt Queue, Tiefensuche nutzt Stack
      c) Nicht erreichte Städte: PAD (von BER aus in Tiefensuche) 