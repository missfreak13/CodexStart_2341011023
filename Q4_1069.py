#diasha kar
#2341011023
#repetitions
#https://cses.fi/problemset/task/1069

string=input()
concur=""
count=0
maxcount=0
for char in string:
    if char== concur:
        count+=1
    else:
        maxcount=max(count, maxcount)
        count=1
        concur=char
maxcount=max(count, maxcount)
print (maxcount)
