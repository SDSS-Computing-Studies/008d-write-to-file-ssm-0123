filer = open('database.csv')

Read = filer.read()

AA = Read.split('\n')
subgrade = []
subgrade.append(AA)

def subname():
    for i in subgrade:
        print(subgrade[i])

subname()