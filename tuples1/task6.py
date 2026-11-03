config = {
    "model": "gpt-4.1-mini",
    "temperature": 0.7,
    "max_tokens": 1024,
}

print(list(config.keys()))
print(list(config.values()))
#print(f"{config.keys()}={config.values()}")
for key, value in config.items():
    print(f"{key}={value}")

for key in config:
    if key == "temperature":
            print(key)

    if key == "max_tokens":
         print(key)


#     items = ["apple", "banana", "cherry"]

# # index gets the number, item gets the value
# for index, item in enumerate(items, start=1):
#     print(f"Index: {index}, Item: {item}")

# for item in items:
#      print(f"item: {item}")


# tasks = ["Clean room", "Cook dinner", "Study Python"]

# index = 0
# for task in tasks:
#     print(f"{index}: {task}")
#     index += 1  # Easy to forget this line!

safe = {k: config.get(k) for k in ["model", "stream"]}
print(safe)
# safes = config.items()
# print(safes)


# safe = {key: config.get}
# for key in ["model", "stream"]:
#     print(safe)

safes = {}

for key in ["model", "stream"]:
    #  safes[key] = config.get(key)
    if key == "stream":
         safes[key] = config.get(key, False)

    elif key == "model":
         safes[key] = config.get(key)

print(safes)