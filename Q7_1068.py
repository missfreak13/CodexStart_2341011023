#diasha kar
#2341011023
#Weird Algorithm
#https://cses.fi/problemset/task/1068

n = int(input("Enter a number till which the program will run: "))
print(n, end=" ")
while n!=1:
    if n%2==0:
        n= n//2
    else:
        n=(n*3)+1

    print(n, end=" ")