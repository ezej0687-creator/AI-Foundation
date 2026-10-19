prompts = "Summarize this document for an AI engineer"
label = "ENGINEER"
prompt = prompts[0:9]
reversed_prompt = prompts[::-1]
len_prompts = len(prompts)
check_prompts = "AI" in prompts
full_label ='AI'

print(prompts[0:1])
print(prompts)
print(prompt)
print(reversed_prompt)
print(len_prompts)
print(check_prompts)
print(f" {full_label} {label.lower()}")
