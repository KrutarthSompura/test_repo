def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    word = input("Enter text: ")
    if is_palindrome(word):
        print("✅ It's a palindrome!")
    else:
        print("❌ Not a palindrome.")
