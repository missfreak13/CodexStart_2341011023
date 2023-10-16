#diasha kar
#2341011023
#coin piles
#https://cses.fi/problemset/task/1754

t= int(input("Enter the number of tests:"))
for i in range(t):
    r,c = map(int, input().split())
    if r<c:
        r,c= c,r
    if r>2*c:
        print("NO")
    elif (r+c)%3== 0:
        print("YES")
    else:
        print("NO")