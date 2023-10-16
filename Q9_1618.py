#diasha kar
#2341011023
#trailing zeros
#https://cses.fi/problemset/task/1618

n= int(input())
count= 0
i= 5
while(n/i>= 1):
    count+= int(n/i)
    i*= 5
print(count)
