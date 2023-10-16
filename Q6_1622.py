#diasha kar
#2341011023
#creating strings
#https://cses.fi/problemset/task/1622

string= input()
letters= list(string)
words= set()
def ways(word, letters):
    if len(letters)==1:
        words.add(word + letters[0])
    else:
        for i in range(len(letters)):
            ways(word + letters[i], letters[0:i] + letters[i+1:])
ways("", letters)

print(len(words))
print("\n".join(sorted(words)))
