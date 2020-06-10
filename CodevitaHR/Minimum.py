t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    ll=[]
    for i in range(n):
        x,y=[int(x) for x in input().split()]
        l.append(x)
        ll.append(y)
    r1=max(l)-min(l)
    r2=max(ll)-min(ll)
    z=max(r1,r2)**2
    print(z)