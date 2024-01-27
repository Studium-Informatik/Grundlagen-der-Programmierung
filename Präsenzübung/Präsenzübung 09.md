## 1.
```python
def fakReduce(n):
    f = lambda x, y: x*y
    seq = range(1, n + 1)
    a = 1

    return reduce(f,seq,a)

print(fakReduce(8))
```

## 2.
```python
def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    numbers = list(range(2, n + 1))

    for prime in range(2, int(n**0.5) + 1):
        numbers = list(filter(lambda x: x == prime or x % prime, numbers))

    return numbers

print(sieve_of_eratosthenes(30))
```

## 3.
```python
def convert_to_right_sequence(seq):
    if seq is None:
        return None

    first, rest = seq
    converted_rest = convert_to_right_sequence(rest)
    return (converted_rest, first)

left_sequence = (1, (2, (3, None)))
print(convert_to_right_sequence(left_sequence))
```

## 4.
#### a)
1. **Funktion h**: Berechnet den Durchschnitt von drei ganzen Zahlen.
    - **Definitionsbereich**: $(a,b,c)$ mit $a,b,c\in \mathbb{Z}$. $(\mathbb{Z}^3)$
    - **Wertebereich**: $\mathbb{R}$
    - **Ordnung**: 1.
2. **Funktion g**: Rundet eine reelle Zahl auf die nächste Ganzzahl ab.
    - **Definitionsbereich**: $\mathbb{R}$
    - **Wertebereich**: $\mathbb{Z}$
    - **Ordnung**: 1.
3. **Funktion f**: Kombiniert h und g.
    - **Definitionsbereich**: $(a,b,c)$ mit $a,b,c\in\mathbb{Z}$
    - **Wertebereich**: $\mathbb{Z}$
    - **Ordnung**: 2.

#### b)




## Zusatzaufgabe
```python
def insert(x, sorted_xs):
    if sorted_xs is None:
        return (x, None)
    else:
        first, rest = sorted_xs
        if x <= first:
            return (x, sorted_xs)
        else:
            return (first, insert(x, rest))

def isort(xs):
    if xs is None:
        return None
    else:
        first, rest = xs
        sorted_rest = isort(rest)
        return insert(first, sorted_rest)


unsorted_sequence = (3, (1, (4, (2, None))))
sorted_sequence = isort(unsorted_sequence)
print(sorted_sequence)
```

