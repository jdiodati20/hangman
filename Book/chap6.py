s = "Camus"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])


r1 = str(input())
r2 = str(input())
s = "Yesterday I wrote a " + r1 + ". I sent it to " + r2 + "."
print(s)


s = "aldous Huxley was born in 1894."
s = s[0].upper() + s[1:]
print(s)


s = "Where now? Who now? When now?"
l = []
l.append(s[:s.index("?") + 1])
s = s[s.index("?") + 1:]
l.append(s[1:s.index("?") + 1])
s = s[s.index("?") + 2:]
l.append(s)
print(l)


l = ["The", "fox", "jumped", "over", "the", "fence", "."]
s = " ".join(l)
print(s)

s = "A screaming comes across the sky"
s = s.replace("s", "$")
print(s)


s = "Hemingway"
n = s.index("m")
print(s)
print(n)


print("'Inconcievable!' he yelled.")

s = "three " + "three " + "three"
print(s)

s = "three " * 3
print(s)

s = "It was a bright cold day in April, and the clocks were striking thirteen"
s = s[:s.index(",")]
print(s)
