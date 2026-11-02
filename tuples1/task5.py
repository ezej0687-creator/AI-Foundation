person = {
    "name": "Sam",
    "age": 99,
    "country": "Nigeria",
}

person.update({"email": "sam@gmail.com"})
person.update({"name": "Jay", "age": 100})
print(person)
person["name"] = "Jay"
print(person["name"])
person.pop("name")
print(person)

del person["email"]
print(person)