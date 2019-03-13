import os
import csv
"""
"r" is for readsing only
"w" is for writing only
"w+" is for reading and writing
'open' function returns an object, called file object, which you can use to read and/or write in your file
"""
str1 = "chap9F/test.txt"
with open(str1, "w") as g:
    g.write("Hello from Python1")

l = list()

with open(str1, "r") as g:
    l.append(g.read())

print(l)

n = "chap9F/st.csv"
with open (n, "w", newline='') as f:
    w = csv.writer(f, delimiter = ',')
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

with open (n, "r") as t:
    print(t.read())

with open (n, "r") as y:
    r = csv.reader(y, delimiter = ",")
    for row in r:
        print(", ".join(row))

with open("chap9F/test1.txt", "r") as f:
    print(f.read())


answer = input("What is your name?  ")
f = open("chap9F/newFile.txt", "w")
f.write(answer)
f.close()

with open("chap9F/newFile.txt", "r") as g:
    print(g.read())


l = [["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
final = "chap9F/final.csv"
with open (final, "w", newline = "") as f:
    w = csv.writer(f, delimiter = ",")
    w.writerow(l[0])
    w.writerow(l[1])
    w.writerow(l[2])

with open (final, "r") as f:
    print(f.read())
