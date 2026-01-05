

# Numerical operations
a = 10
b = 3
sum_result = a + b
product_result = a * b
division_result = a / b

print("Sum:", sum_result)
print("Product:", product_result)
print("Division:", division_result)

# String operations
name = "Pekka"
greeting = "Hello, " + name + "!"
upper_case = greeting.upper()
length = len(greeting)

print("Greeting:", greeting)
print("Uppercase:", upper_case)
print("Length of greeting:", length)

# Conditional statements
if sum_result > 10:
    print("The sum is greater than 10.")
elif sum_result == 10:
    print("The sum is exactly 10.")
else:
    print("The sum is less than 10.")

if "PEKKA" in upper_case:
    print("Your name appears in uppercase greeting.")
else:
    print("Name not found in uppercase greeting.")

def main():
    # Original string
    text = "  Hello, Pekka! Welcome to Python programming.  "

    # 1. Basic cleanup
    stripped = text.strip()  # remove leading/trailing spaces
    print("Stripped:", stripped)

    # 2. Case operations
    print("Uppercase:", stripped.upper())
    print("Lowercase:", stripped.lower())
    print("Title Case:", stripped.title())
    print("Swap Case:", stripped.swapcase())

    # 3. Slicing and indexing
    print("First 5 chars:", stripped[:5])
    print("Last 5 chars:", stripped[-5:])
    print("Character at index 7:", stripped[7])

    # 4. Searching and replacing
    print("Count 'o':", stripped.count("o"))
    print("Find 'Python':", stripped.find("Python"))
    replaced = stripped.replace("Python", "Advanced Python")
    print("Replaced:", replaced)

    # 5. Splitting and joining
    words = stripped.split(" ")
    print("Words list:", words)
    joined = "-".join(words)
    print("Joined with hyphen:", joined)

    # 6. String formatting
    name = "Pekka"
    language = "Python"
    print("Formatted (f-string):", f"Hello {name}, you are learning {language}!")
    print("Formatted (format method):", "Hello {}, welcome to {}!".format(name, language))

    # 7. Checking string properties
    sample = "12345"
    print("Is digit?", sample.isdigit())
    print("Is alpha?", sample.isalpha())
    print("Is alphanumeric?", sample.isalnum())

    # 8. Advanced: reversing and joining characters
    reversed_text = "".join(reversed(stripped))
    print("Reversed:", reversed_text)

    # 9. Encoding and decoding
    encoded = stripped.encode("utf-8")
    print("Encoded (bytes):", encoded)
    decoded = encoded.decode("utf-8")
    print("Decoded back:", decoded)

    # 10. Multiline and raw strings
    multiline = """This is
a multiline
string."""
    print("Multiline:\n", multiline)

    raw_string = r"C:\Users\Pekka\Documents\Python"
    print("Raw string:", raw_string)


if __name__ == "__main__":
    main()


def analyze_text(text: str):
    print("Original text:", text)

    # 1. Normalize whitespace and case
    cleaned = " ".join(text.split())  # collapse multiple spaces
    cleaned = cleaned.strip().lower()
    print("Cleaned text:", cleaned)

    # 2. Tokenization (split into words)
    words = cleaned.split(" ")
    print("Words:", words)

    # 3. Frequency analysis
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    print("Word frequencies:", freq)

    # 4. Detect keywords
    keywords = ["error", "warning", "success", "python"]
    found = [kw for kw in keywords if kw in cleaned]
    print("Detected keywords:", found)

    # 5. Advanced string slicing and pattern checks
    if cleaned.startswith("error"):
        print("This text starts with an error message.")
    if cleaned.endswith("!"):
        print("This text ends with an exclamation mark.")

    # 6. Replace sensitive info (masking emails)
    import re
    masked = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[EMAIL]", cleaned)
    print("Masked text:", masked)

    # 7. Reverse and palindrome check
    reversed_text = cleaned[::-1]
    print("Reversed:", reversed_text)
    if cleaned == reversed_text:
        print("The text is a palindrome!")

    # 8. Encoding/decoding for storage
    encoded = cleaned.encode("utf-8")
    decoded = encoded.decode("utf-8")
    print("Encoded bytes:", encoded)
    print("Decoded back:", decoded)


if __name__ == "__main__":
    sample_input = "   ERROR: User Pekka logged in with email pekka@example.com !!!   "
    analyze_text(sample_input)





    


