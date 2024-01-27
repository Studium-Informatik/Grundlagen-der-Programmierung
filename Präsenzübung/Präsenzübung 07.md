## 1
### 1.1
```python
def rec(x, n):  
    if n <= 1:  
        return x  
    return rec(2 * x, n - 1)  
  
  
position = 10  
start = 5  
  
print(rec(start, position))
```

### 1.2
#### a)
Für n = 1
$$\displaylines{
n^2=1^2=\underline{1}\\
\sum^{n}_{i=1}(2i-1)=(2\cdot 1 - 1)=\underline{1}
}$$

Für n = 2
$$\displaylines{
n^2=2^2=\underline{4}\\
\sum^{n}_{i=1}(2i-1)=(2\cdot 1 - 1)+(2\cdot 2 - 1)=\underline{4}
}$$

Für n = 3
$$\displaylines{
n^2=3^2=\underline{9}\\
\sum^{n}_{i=1}(2i-1)=(2\cdot 1 - 1)+(2\cdot 2 - 1)+(2\cdot 3 - 1)=\underline{9}
}$$
#### b)
Vorschrift:
$S(n)=S(n-1)+(2n-1)$

Basisfall:
$S(1)=1$

#### c)
**IV**:
für $n=1$
$S(1)=1$
gilt, da $1^2=1$

**IA**:
$S(k)=k^2$

**IS**:
$n=k+1$
$$\displaylines{
S(k+1)&=&S(k+1-1)+(2(k+1)-1)\\
&=&S(k)+(2k+1)\\
&=&k^2+2k+1\\
&=&(k+1)^2&&\square
}$$
