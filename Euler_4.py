'''
Find the largest palindrome made from the product of two 3-digit numbers

'''

a = []
for x in range(100,1000):
    for y in range(100,1000):
        z = x*y 
        k = str(z)
        q = k[::-1]
        if k == q:
            a.append(z)
a.sort()
print(a[-1])
