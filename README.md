# Linearne struktury
Naprogramoval som par zakladnych pomocnych funkcii potrebnych pri praci so zoznamom.

## Obsah
1. [Pridanie prvku na koniec zoznamu](#pridanie-prvku-na-koniec-zoznamu)
1. [Odstranenie posledneho prvku zoznamu](#odstranenie-posledneho-prvku-zoznamu)
1. [Odstranenie prveho prvku zoznamu](#odstranenie-prveho-prvku-zoznamu)
1. [Pridanie prvku na zaciatok zoznamu](#pridanie-prvku-na-zaciatok-zoznamu)
1. [Odstranenie prvku na lubovolnom indexe zoznamu](#odstranenie-prvku-na-lubovolnom-indexe-zoznamu)
1. [Pridanie prvku na lubovolny index zoznamu](#pridanie-prvku-na-lubovolny-index-zoznamu)
1. [Stack (LIFO princip)](#stack-(lifo-princip))
1. [Queue (FIFO princip)](#queue-(fifo-princip))
1. Zoznam (Linearna datova struktura)

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
Najprv sa musime uistit, ze index, na ktory chce uzivatel umiestnit novy prvok existuje v nasom zozname:
```py
if idx < 0 or idx > len(zoznam) - 1:
    print("nespravny index")
    return
```
Ked uz vieme, ze index je spravny, tak si posunieme prvky v zozname od indexu (vratane) po predposledny prvok o 1 poziciu dolava:
```py
# Cyklus zacina pri zvolenom indexe a konci pri predposlednom prvku
for i in range(idx, len(zoznam) - 1):
    zoznam[i] = zoznam[i + 1]
```
Zoznam `[2, 4, 6]` pri vybratom indexe `1` sa nam zmeni na: `[2, 6, 6]`. Potom mozeme jednoducho odstranit posledny prvok:
```py
zoznam.pop()
```

### Pridanie prvku na lubovolny index zoznamu
Uistime sa, ze index existuje podobne ako pri predoslej operacii:
```py
if idx < 0 or idx > len(zoznam) - 1:
    print("nespravny index")
    return
```
Nasledne zduplikujeme posledny prvok zoznamu:
```
zoznam.append(zoznam[-1])
```
Zoznam `[2, 4, 6]` sa nam zmeni na `[2, 4, 6, 6]`.
Teraz si posunieme prvky zoznamu od predposledneho (vratane) po zvoleny index o 1 doprava. Cyklus postupuje od vacsich indexov po mensie (opacne ako normalne):
```py
# Cyklus zacina pri predposlednom indexe a konci pri zvolenom indexe
# Cyklus postupuje od vacsich indexov po mensie
for i in range(len(zoznam) - 2, idx, -1):
    zoznam[i] = zoznam[i - 1]
```
Takto sa nam zoznam `[2, 4, 6, 6]` pri zvolenom indexe `1` zmeni na: `[2, 4, 4, 6]`. Nasledne mozeme jednoducho nastavit hodnotu prvku na zvolenom indexe na lubovolnu hodnotu, kedze tuto hodnotu mame momentalne duplikovanu:
```py
zoznam[idx] = nova_hodnota
```

### Stack (LIFO princip)
Datova struktura stack (zasobnik) funguje na takzvanom principe **LIFO** (_Last in First out_).
Tento princip vyjadruje postupnost vkladanie a mazania udajov v strukture.
Podla nazvu zistime, ze <ins>**prvok, ktory bol naposledy ulozeny do zasobnika je prvy pri mazani**</ins> udajov zo zasobnika.
Pri pochopeni principu nam pomoze nasledujuci obrazok:

![graf zasobnika](./assets/stack.svg "Graf zasobnika")

### Queue (FIFO princip)
Datova struktura queue (fronta) funguje na principe **FIFO** (_First in First out_).
Toto znamena, ze <ins>**prvok, ktory bol prvy vlozeny do fronty je prvy pri mazani**</ins> hodnot z fronty.
Obrazok na pomoc s pochopenim:

![graf fronty](./assets/queue.svg "Graf fronty")
