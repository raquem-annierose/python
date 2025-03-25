def check_freq(x):
    return {c: x.count(c) for c in set(x)}

sample_text = str(input ('Input text: '))
check_freq(sample_text)

print(f"{input}: {check_freq}")
print()