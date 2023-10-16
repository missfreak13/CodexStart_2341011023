#diasha kar
#2341011023
#apple division
#https://cses.fi/problemset/task/1623

n= int(input())
w= list(map(int, input().split()))
def md(index, a, b):
    if index >= len(w):
        return abs(a - b)
    return min(md(index + 1, a + w[index], b), md(index + 1, a, b + w[index]))
print(md(0, 0, 0))










