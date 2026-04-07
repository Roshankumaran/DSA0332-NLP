def plural(word):
    if word.endswith("y"):
        return word[:-1] + "ies"
    else:
        return word + "s"

# Test
nouns = ["cat", "baby", "dog"]
for n in nouns:
    print(n, "->", plural(n))
