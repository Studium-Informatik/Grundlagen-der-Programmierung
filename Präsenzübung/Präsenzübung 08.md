## 3. Die Türme von Hanoi
1. **Basisfall**: Wenn nur eine Scheibe zu bewegen ist, bewege diese direkt vom Startstab zum Ziel stab. Dies ist der einfachste Fall.
    
2. **Rekursiver Schritt**: Um n Scheiben von einem Startstab zu einem Ziel stab unter Verwendung eines Hilfsstabs zu bewegen:
    
    - Bewege die obersten n-1 Scheiben rekursiv vom Startstab zum Hilfsstab unter Verwendung des Zielstabs als Hilfsstab.
        
    - Bewege dann die größte, unterste Scheibe vom Startstab zum Zielstab.
        
    - Bewege schließlich die n-1 Scheiben vom Hilfsstab zum Ziel stab unter Verwendung des Startstabs als Hilfsstab.