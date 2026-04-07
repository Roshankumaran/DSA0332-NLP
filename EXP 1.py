import re

text = "Contact me at roshan@gmail.com"

# Find email
pattern = r"\S+@\S+"
result = re.search(pattern, text)

if result:
    print("Email found:", result.group())
else:
    print("No email found")
