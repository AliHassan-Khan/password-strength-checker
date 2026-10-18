# Author: Ali Hassan Khan   
# password strength checker: check length, uppercase, lowercase, digits and symbols, then print Weak, Medium or Strong
def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    digit_error = not any(char.isdigit() for char in password)
    symbol_error = not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)

    if length_error or uppercase_error or lowercase_error or digit_error or symbol_error:
        return "Weak"
    elif len(password) >= 12 and not (length_error or uppercase_error or lowercase_error or digit_error or symbol_error):
        return "Strong"
    else:
        return "Medium"
    
password = input("Enter a password: ")
result = check_password_strength(password)
print("Password strength:", result)
