f=open('13.txt')
x=f.read()
q=x.replace('\n','')
i=0
summa=0
e=[]
while i<5000:
    a=q[0+i:50+i]
    e.append(a)
    i+=50
for f,p in enumerate(e):
    e[f] = int(p)
"""
for g in e:
    summa+=g
    mo=str(summa)
print(mo[0:11])
"""
koko=sum(e)
qo=str(koko)
print(qo[0:10])


    
