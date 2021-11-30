#!python3

'''
Ask the user to enter in a list of 5 words.
Convert the word to a string literal JSON object
Write the contents to a file called 'task3.txt'

Example:
Enter a word: frog
Enter a word: french
Enter a word: puppy
Enter a word: escalate
Enter a word: ice

task3.txt contents:
["frog","french","puppy","escalate","ice"]

'''

import json

def test1():
    list1 = []
    file1 = open('task3.txt','w')
    while True:
        a = input("Enter a word: ")
        if a != "":
            list1.append(a)
        if a == "":
            break
    printing = json.dumps(list1)
    file1.write(printing+"\n")
    file1.close()

test1()