t=int(input())
for i in range(t):
    l=input()
    ll=list(l)
    r=set(ll)
    if len(ll)>len(r):
        print("Yes")
    else:
        print("No")