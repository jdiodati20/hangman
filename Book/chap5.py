listing = []
listing.append("Drake")
listing.append("George Thorogood")
listing.append("Dropkick Murphys")
print(listing)


la = (3.1515926535897932384626433, 832795028841979693)
tuples = []
tuples.append(la)
print(tuples)


dictionary = {"height": "5 foot 8 inches", "weight": "147"}
print(dictionary)

question = str(input("What do you want to know about?  "))
question = question.lower()

if question in dictionary:
    print(dictionary[question])
else:
    print("Not found")


sing = {"Drake": "" "hello" "", "George Thorogood": "", "Dropkick Murphys": ""}
sing["Drake"] = "Hotline Bling"
sing["Drake"] = "Drip Too Hard"
sing.update({"21 Savage": "Bank Account"})
del sing["Drake"]
print(sing)
