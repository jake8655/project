# Linearne struktury
Naprogramoval som par zakladnych pomocnych funkcii potrebnych pri praci so zoznamom.

## Obsah
1. [Pridanie prvku na koniec zoznamu](#pridanie-prvku-na-koniec-zoznamu)
1. [Odstranenie posledneho prvku zoznamu](#odstranenie-posledneho-prvku-zoznamu)
1. [Odstranenie prveho prvku zoznamu](#odstranenie-prveho-prvku-zoznamu)
1. [Pridanie prvku na zaciatok zoznamu](#pridanie-prvku-na-zaciatok-zoznamu)
1. [Odstranenie prvku na lubovolnom indexe zoznamu]()
1. Pridanie prvku na lubovolny index zoznamu
1. Stack (LIFO semantika)
1. Queue (FIFO semantika)
1. Zoznam (Mudry datovy typ)

### Pridanie prvku na koniec zoznamu
Na tuto operaciu som vyuzil vstavanu metodu `.append(val)`.

### Odstranenie posledneho prvku zoznamu
Na odstranenie posledneho prvku som pouzil vstavanu metodu `.pop()`.

### Odstranenie prveho prvku zoznamu
Najprv sa musime uistit, ze nas zoznam obsahuje prvky, co osetrime takymto sposobom:
```py
if len(zoznam) == 0:
    print("zoznam je prazdny")
    return
```
Teraz si postupne posunieme prvky zoznamu dolava o 1 poziciu:
```py
# Cyklus zacina pri druhom prvku zoznamu (1. index) a konci pri poslednom prvku
for i in range(1, len(zoznam)):
    # Prvok na predoslej pozicii nastavime na hodnotu prvku na aktualnej pozicii
    zoznam[i - 1] = zoznam[i]
```
Ked mame dany zoznam: `[2, 4, 6]`, tak po tejto operacii sa nam zoznam zmeni na: `[4, 6, 6]`.
Ako posledny krok, odstranime posledny nepotrebny prvok zoznamu:
```py
zoznam.pop()
```

### Pridanie prvku na zaciatok zoznamu
Na zaciatku si duplikujeme posledny prvok zoznamu:
```py
zoznam.append(zoznam[-1])
```
Takto sa nam zoznam `[2, 4, 6]` zmeni na `[2, 4, 6, 6]`
Dalej spustime cyklus od predposledneho prvku zoznamu az po prvy (0. index):
```py
# Cyklus zacina pri predposlednom prvku zoznamu a konci pri prvom (0. index)
# Cyklus tiez postupuje v opacnom smere (od vacsich cisel po mensie)
for i in range(len(zoznam) - 2, 0, -1):
    # Nastavenie prvku na aktualnej pozicii na hodnotu prvku na predoslej pozicii
    zoznam[i] = zoznam[i - 1]
```
Tymto cyklom sa nam zoznam `[2, 4, 6, 6]` zmeni na `[2, 2, 4, 6]`.
Teraz mozeme jednoduch nastavit hodotu prveho prvku zoznamu (0. index) na novu hodnotu:
```py
zoznam[0] = nova_hodnota
```

### Odstranenie prvku na lubovolnom indexe zoznamu