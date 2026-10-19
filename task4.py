docs = ["intro.txt", "api.md", "faq.md"]
messages = ["tell me about ai"]
scores = [72, 91, 65, 88]
docs[1] = "api-guide.md"
documents = docs.append("notes.md")
document = messages.extend(["summarize docs", "rewrite this email"])
last_item = docs.pop()


print(docs[0])
print(docs[0:3])
print(docs)
print(messages)
print(last_item)
print(scores)
print(max(scores))
print(min(scores))
print(sum(scores))

