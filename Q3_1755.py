#diasha kar
#2341011023
#pallindrome reorder
#https://cses.fi/problemset/task/1755

string=input("Enter a string with random alphabets:")
pair=[]
solo=[]
for char in string:
    if char in solo:
        solo.remove(char)
        pair.append(char)
    else:
        solo.append(char)
reorder=''.join(pair)+''.join(solo)+''.join(pair)[::-1]
if reorder==reorder[::-1]:
    print(reorder)
else:
    ("NO SOLUTION")