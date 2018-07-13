n=int(input())
dig=str(n)
k=[]
for i in dig:
    k.append(i+" ")
p=""
for z in k:
    p+=z
print(p[:(len(p)-1)])
