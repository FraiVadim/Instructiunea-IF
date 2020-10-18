n=int(input("Ionel a sosit al : "))
if n>0:
    if n%4==0:
        print("Casuta",n//4)
    if n%4!=0:
        print("Casuta",((n//4)+1))
if n<=0:
    print("eroare")