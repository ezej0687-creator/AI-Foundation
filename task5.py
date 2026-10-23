model = "gpt-4.1-mini"
temperature = 0.3
max_tokens = 512

raw_user_text = "  EXPLAIN lists vs strings for AI engineers  "
docs = "intro.txt,api.md,faq.md"
messages = []

user_text = raw_user_text.strip().lower()
print(user_text)

doc_list = docs.split(",")
print(doc_list)

messages.append("system: You are a helpful AI engineering tutor.")
messages.append("context: " + ", ".join(doc_list))
messages.append("user: " + user_text)
print(messages)

print(f"Model: {model} {type(model)}")
print(f"Temperature: {temperature} {type(temperature)}")
print(f"Max_tokens: {max_tokens} {type(max_tokens)}")

print(len(messages))
for message in messages:
    print(message)

user = "lists" in user_text
print(user)
#print("lists" in user_text)   

