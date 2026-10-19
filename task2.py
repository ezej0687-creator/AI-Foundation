model = "gpt-4.1-mini"
temperature = 0.7
max_tokens = 1024
stream = False
api_key = None

token_limit_text = "2048"
token_limit = int(token_limit_text)

temperature = 0.2

daily_request_budget = 1_000_000

print("Types should match this pattern:\n")

print(f"Model: {model} {type(model)}")
print(f"Temperature: {temperature} {type(temperature)}")
print(f"Max_tokens: {max_tokens} {type(max_tokens)}")
print(f"Stream: {stream} {type(stream)}")
print(f"Api_key: {api_key} {type(api_key)}")
print(f"Token_limit: {token_limit} {type(token_limit)}")
print("Temperature:", temperature)
print(f"Model: {model} {daily_request_budget}")
