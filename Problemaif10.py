a=int(input ("Numarul de gaini: ")) 
b=int(input ("Numarul de boabe: ")) 
fg=b//a
c=b-(a*fg) 
if fg>c: 
    print("Gaina primeste cu ",fg-c," boabe mai mult") 
if c>fg: 
    print("Curcanul primeste cu ",c-fg," boabe mai mult") 
if c==fg: 
    print("Primesc acelasi numar de boabe",fg)