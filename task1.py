


def test1():
    file1 = open('task1.txt','w')
    a = input("What is your name? ")
    file1.write(a+"\n")
    b = input("What is your email? ")
    file1.write(b+"\n")
    file1.close()

test1()