a=int(input("dati prima nota "))
b=int(input("dati a doua nota "))
c=int(input("dati a treia nota "))
if c and b and a <=10 and c and b and a >=0:
    if c>=8:
        print(a,b,c)
    if c<8:
        if a>b:
            print(a)
        if b>a:
            print(b)
        if a==b:
            print(a)
else:
    print("noi avem sistema de 10 puncte!!!")     