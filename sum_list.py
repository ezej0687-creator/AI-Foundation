def sum_list(nums: list[int]) -> int:
    total = 0
    for num in nums:
        total += num
    return total
        

print(sum_list(nums = [1, 2, 3, 4, 5]))
print(sum_list(nums = [-1, 10, -5, 20]))

def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(n = 4))
print(is_even(n = 7))

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count+= 1
    return count
print(count_vowels(s = "Hello World"))
print(count_vowels(s = "PYTHON programming"))  

def reverse_string(s: str) -> str:
    return s[::-1]
    
print(reverse_string(s = "python"))
print(reverse_string(s = "Data Science"))