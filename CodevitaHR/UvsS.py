n=int(input())
l=list(map(int,input().split()[:n]))
m=int(input())
for i in range(1,m+1):
    s=0
    num=int(input())
    vv=-1
    for j in range(n):
        s+=l[j]
        if s>=num:
            vv=j+1
            break
        else:
            pass
    print(int(vv))