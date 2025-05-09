from collections import Counter

def check_freq(x):
    return {c: x.count(c) for c in set(x)}

# Using check_freq function
sample_text = input('Input text: ')
freq_dict = check_freq(sample_text)
print(f"Character frequencies using check_freq: {freq_dict}")

# Using Counter from collections
sample_text = input('Input text: ')
count = Counter(sample_text)
print(f"Character frequencies using Counter: {dict(count)}")

def check_freq(x):
    return {c: x.count(c) for c in set(x)}

sample_text = str(input ('Input text: '))
check_freq(sample_text)

print(f"{input}: {check_freq}")
print()