# mpis_approximations
Niech f : [a, b] → R+ bedzie funkcja ciagła na przedziale [a, b] przyjmujaca wartosci nieujemne
dla której chcemy wyznaczyc przyblizona wartosc całki oznaczonej a b

 f(x) dx. Rozwazmy
prosta probabilistyczna metode aproksymacji takich całek.

1. Generujemy niezaleznie i jednostajnie losowo  n punktów z prostokata [a, b] × [0, M] dla
ustalonego M ­ sup{f(x): x ∈ [a, b]}.

2. Zliczamy, ile sposród wylosowanych punktów lezy „pod wykresem” funkcji f (punkt
(x, y) lezy „pod wykresem” f, jesli y <= f(x)) – oznaczmy ta liczbe przez C.

3. Jako aproksymacje całki przyjmujemy wartosc (C/n)*


(b − a)M 
(gdzie (b − a)M to pole powierzchni rozwazanego prostokata). 
