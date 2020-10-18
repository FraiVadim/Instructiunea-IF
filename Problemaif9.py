ma=int(input("bile albe si mici sunt "))
mr=int(input("bile rosii si mici sunt "))
mv=int(input("bile verzi si mici sunt "))
ga=int(input("bile albe si mari sunt "))
gr=int(input("bile rosii si mari sunt "))
gv=int(input("bile verzi si mari sunt "))
mt=ma+mr+mv
gt=ga+gr+gv
print("in total sunt",mt+gt,"bile")
if mt>gt:
    print("sunt",mt,"bile mici")
if gt>mt:
    print("sunt",gt,"bile mari")
ta=ma+ga
tr=mr+gr
tv=mv+gv
if ta>tr and ta>tv:
    print("sunt",ta,"bile albe")
if tr>ta and tr>tv:
    print("sunt",tr,"bile rosii")
if tv>ta and tv>tr:
    print("sunt",tv,"bile verzi") 
if ta==tr==tv:
    print("nr bilelor este egal")            