votes = ("yes", "yes", "no", "no", "yes")
points = (3, 4)

print("Yes:", votes.count("yes"))
print("no:", votes.count("no"))
print(len(votes))
vote = votes.index("yes")
print(vote)

#Convert point to a list, set the second value to 5, convert back to a tuple.

list_convert = list(points)
list_convert[1] = 5
tuple_convert = tuple(list_convert)
print(tuple_convert)

print(votes[::-1])
print("maybe" in votes)