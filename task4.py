docs = ["intro.txt", "api.md", "faq.md"]
messages = ["tell me about ai"]
scores = [72, 91, 65, 88]
docs[1] = "api-guide.md"

documents = docs.append("notes.md")
document = messages.extend(["summarize docs", "rewrite this email"])

last_item = docs.pop()
backup = docs[0:3] = ["Sam, Jack, Fred"]
backup_docs = backup.copy()


print(docs[0])
print(docs[0:3])
print(docs)
print(messages)
print(backup_docs)
print(last_item)
print(scores)
print(max(scores))
print(min(scores))
print(sum(scores))


