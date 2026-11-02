user = {
    "name": "Sam",
    "age": 99,
    "country": "Nigeria",
}

print(user["name"])
print(user["age"])

print(user.get("country"))
print(user.get("email"))
print(user.get("email", "not given"))
print("name" in user)
print("sam" in user)

user.update({"email": "ezej0687@gmail.com"})
print(user)

print(type(user))
print(len(user))