b=1
summa=0
for k in range(1,101):
    b*=k
b=str(b)
q=[int(item) for item in b]
print(q)
for i in q:
    summa+=i
print(summa)

