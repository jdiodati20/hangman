l = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index in l:
    print(index)


for i in range (25, 51):
    print(i)


for index in l:
    print(index)
    print(l.index(index))


f = False
a = 15
while f == False:
    print("Guess the number?  Press q to quit")
    g = input()
    if g == "q":
        break
    g = int(g)
    if g == a:
        print("You guessed right")
        f = True
    else:
        print("You did not guess right")


l1 = [8, 19, 148, 4]
l2 = [9, 1, 33, 83]
l3 = []
for i in range(0, 4):
    l3.append(l1[i] * l2[i])
print(l3)
