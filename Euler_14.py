b=range(1,1000000)
ko=[]
k=[]
for a in b:
    while a!=1:
        if a%2==0:
            a=a/2
        else:
            a=3*a+1
        ko.append(a)   
        if a==1:
            k.append(int(len(ko)+1))
            ko.clear()    
#print(max(k)) 
