# Example file for Advanced Python by Joe Marini
# Using the built-in string constants

import string
import secrets


# built-in constants for a variety of needs
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)


# Define a test string
testStr = "The quick brown fox jumps OVER the lazy dog."

# use an iterator to see if a string contains any punctuation 
if any(c in string.punctuation for c in testStr):
    print("The string contains punctuation")
else:
    print("No punctuation found")

# generate a secure random password
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(10))
print(password)

# Check the strength of a password
def check_password_strength(testPass):
    if (any(char in string.punctuation for char in testPass) and
       any(char in string.digits for char in testPass) and
       any(char in string.ascii_lowercase for char in testPass) and
       any(char in string.ascii_uppercase for char in testPass)):
        return f"{testPass} is a strong password"
    else:
        return f"{testPass} is a weak password"

print(check_password_strength("MyTestPa$$123!"))
print(check_password_strength("password"))

# Example file for Advanced Python by Joe Marini
# Formatting output strings

# Basic formatting - center(), ljust(), rjust()
print("center".center(40, '-'))
print("left".ljust(40, '.'))
print("right".rjust(40, '.'))

# Formatting strings with format specification codes
# Format spec is: [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["."precision][type]
val1 = 1234.5678
val2 = 10987.65
val3 = 12.99
val4 = -280.7

print(f"{val1}")
print(f"{val2}")
print(f"{val3}")
print(f"{val4}")

# Specify a precision and type
print(f"{val1:.2f}")
print(f"{val4:.2f}")

# Use alignment and width and leading zeros
# < is left align, > is right align, ^ is centered
print(f"{val1:>10.2f}")
print(f"{val2:>10.2f}")
print(f"{val3:>10.2f}")
print(f"{val4:>10.2f}")

# Use a grouping option and +/- signs
print(f"{val1:>+10,.2f}")
print(f"{val2:>+10,.2f}")
print(f"{val3:>+10,.2f}")
print(f"{val4:>+10,.2f}")

# Insert a fill character
print(f"{val1:_>10.2f}")
print(f"{val2:_>10.2f}")
print(f"{val3:_>10.2f}")
print(f"{val4:_>10.2f}")

# Create format specifiers dynamically
width = 10
precision = 2
format_spec = f"{123.456:{width}.{precision}f}"
print(format_spec)
format_spec = "{val:{width}.{precision}f}".format(
    val=val2, width=10, precision=2)
print(format_spec)

# Example file for Advanced Python by Joe Marini
# Manipulating string content


test_str = "The quick, brown fox jumps over the lazy dog."

# upper, lower, title
print(test_str.upper())
print(test_str.lower())
print(test_str.title())

# strip, lstrip, rstrip
test_str2 = "   This string has whitespace   "
print(test_str2.strip())
print(test_str2.lstrip())
print(test_str2.rstrip())

# split creates a sequence from a single string
words = test_str.split()
print(words)

# join concatenates an iterable into a single string
words = ["Hello", "world", "from", "Python"]
separator = " "
sentence = separator.join(words)
print(sentence)

# Example file for Advanced Python by Joe Marini


sample_text = "The quick brown fox jumps over the lazy dog."

tempstr = sample_text.lower()

# Using find() to find the first occurrence of a substring
print("First occurrence of 'the':", tempstr.find("the"))

# Example with optional start and end parameters
print("First occurrence of 'the' after index 5:", tempstr.find("the", 5, 36))

# Using index() to find the first occurrence of a substring (raises ValueError if not found)
try:
    print("First occurrence of 'fox':", sample_text.index("fax"))
except ValueError:
    print("Not found")

# The 'in' operator can be used for Boolean testing:
print("Is 'fox' present:", "fox" in sample_text)

# Using rfind() to find the last occurrence of a substring
print("Last occurrence of 'a':", sample_text.rfind("the"))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
print("Last occurrence of 'jump':", sample_text.rindex("jump"))

# The replace() function will find content in the string and replace it
result = sample_text.replace("lazy","tired")
print(result)
result = tempstr.replace("the","THE")
print(result)
