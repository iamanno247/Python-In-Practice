def is_palindrome(text):
    # Return True if text is a palindrome (case-insensitive, ignoring spaces)
    forward = "".join(text.split()).lower()
    
    return forward == forward[::-1]

text = input().strip()
# Print 'yes' or 'no' based on is_palindrome(text)

if is_palindrome(text):
    print("yes")
else:
    print("no")