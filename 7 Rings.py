# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    if a*b>=10000 and a*b<100000:
        print("YES")
    else:
        print("NO")
