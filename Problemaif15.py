x=int(input("Radu este pe locul: "))
if x>0 and x<=125:
    if x<=25:
        print("A")
    if x>25 and x<=50:
        print("B")
    if x>50 and x<=75:
        print("C")
    if x>75 and x<=100:
        print("D")
    if x>100 and x<=125:
        print("E")
else:
    print ("eroare!!!")