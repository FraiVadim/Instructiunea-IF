n1=(input("introduceti nr elevului: "))
n2=(input("introduceti nr elevului: "))
n3=(input("introduceti nr elevului: "))
p1=(input("introduceti nr de puncte a elevului 1 "))
p2=(input("introduceti nr de puncte a elevului 2 "))
p3=(input("introduceti nr de puncte a elevului 3 "))
if p1>p2 and p1>p3:
    print ("punctaj maxim are elevul cu nr","crt",n1)
if p2>p1 and p2>p3:
    print ("punctaj maxim are elevul cu nr","crt",n2)
if p3>p1 and p3>p2:
    print ("punctaj maxim are elevul cu nr","crt",n3)
if p1==p2 and p1>p3:
    print ("punctaj maxim au elevii cu nr crt",n1,"si",n2)
if p1==p3 and p1>p2:
    print ("punctaj maxim au elevii cu nr crt",n1,"si",n3)
if p2==p3 and p2>p1:
    print ("punctaj maxim au elevii cu nr crt",n2,"si",n3)    