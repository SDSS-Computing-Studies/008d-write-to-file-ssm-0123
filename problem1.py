import json

file1 = open('problem1.txt','r')

a = file1.read()

b = json.loads(a)

print(type(b))
print(b)
