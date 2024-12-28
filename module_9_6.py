def all_variants(text):
    for i in range(len(text)):
        yield text[i]
    for length in range(2, len(text) + 1):
        for i in range(len(text) - length + 1):
            yield text[i:i + length]

a = all_variants("abc")
for i in a:
    print(i)