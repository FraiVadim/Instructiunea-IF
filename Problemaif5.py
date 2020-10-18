ac=int(input ("dati anul curent "))
lc=int(input ("dati luna curent "))
zc=int(input ("dati ziua curent "))
an=int(input ("dati anul nasterii "))
ln=int(input ("dati luna nasterii "))
zn=int(input ("dati ziua nasterii "))
if lc>ln or ( ln==lc and zc>zn):
    print((ac-an),"ani")
if lc<ln or (ln==lc and zc<zn):
    print((ac-an)-1,"ani")   