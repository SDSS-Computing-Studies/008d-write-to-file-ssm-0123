import json

filer = open('database.txt')
Read = filer.read()
sub = json.loads(Read)


def subname():
    x = 1
    for i in sub:
        print(x,end=". ")
        for a in i:
            print(a)
        x = x+1
    ask = input("Choose the number to change name of the subject: ")
    now = int(ask)
    askname = input("Enter new name of subject")
    sub[now-1][0] = askname

def subgrade():
    x = 1
    for i in sub:
        print(x,end=". ")
        for a in i:
            print(a)
        x = x+1
    ask = input("Choose the number to change grade of the subject: ")
    now = int(ask)
    askname = input("Enter new grade of subject")
    sub[now-1][1] = askname
    
def savedata():
    filew = open('database.txt','w')
    filew.write(json.dumps(sub))


def main():
    while True:
        print("1. Change subject name")
        print("2. Change subject grade")
        print("3. Save & Exit")
        Main = input("")
        if Main == "1":
            subname()
        elif Main == "2":
            subgrade()
        elif Main == "3":
            savedata()
            break


main()