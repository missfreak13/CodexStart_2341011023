#diasha kar
#2341011023
#missing number
#https://cses.fi/problemset/task/1083

n=int(input())
x=(n*(n+1))//2 - sum(int(i) for i in input().split())
print(x)
