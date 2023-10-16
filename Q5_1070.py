#diasha kar
#2341011023
#permutations
#https://cses.fi/problemset/task/1070

n=int(input())
e=[]
o=[]
if n==1:
    print(1)
elif n<=3:
    print("NO SOLUTION")
else:
    for i in range(n, 0,-1):
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
x=(o+e)
print(*(x))
