def ends_with_ab(s):
    if len(s) >= 2 and s[-2:] == "ab":
        return True
    return False

# Test
words = ["ab", "aab", "aba", "babab"]
for w in words:
    print(w, "->", "Accepted" if ends_with_ab(w) else "Rejected")
