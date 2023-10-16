#diasha kar
#2341011023
#missing number
#https://cses.fi/problemset/task/1083

a=[]
n=int(input("Enter the number till where the program will run: "))
for i in range(0,n-1):
    ele=int(input("Enter element:"))
    a.append(ele)
print (a)
min=min(a)
max=max(a)
for j in range(min, max, 1):
    if j not in a:
        print ("Missing number:",j)
        
