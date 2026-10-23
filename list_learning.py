names = ["Sam", "Jack", "Joe"]
scores = [50, 90, 45, True, "SAM"]  # mixed types are allowed
empty = []
row = []
empty.append(names)
empty.append(scores)
names.append("Owe")
row.append(empty)
#print(names)
#print(scores)
#print(empty)
#print(row)

names.extend(["paul", "John", "Emmanuel"])
name = names + scores
empty.append(name)

print(empty)


