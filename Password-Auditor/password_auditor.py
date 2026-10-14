#built-in module allowing the search for characters, integers and special characters
import re

#user is asked to enter their password and it is stored in a variable
password = input("Enter password: ")

#this variable will track how many security requirements the password will pass
score = 0

#length check
if len(password) >= 12:
  score += 1
  length_check = "PASS"
else:
  length_check = "FAIL"
  
#uppercase check
if re.search(r"[A-Z]", password):
  score += 1
  uppercase_check = "PASS"
else:
  uppercase_check = "FAIL"
  
#lowercase check
if re.search(r"[a-z]", password):
  score += 1
  lowercase_check = "PASS"
else:
  lowercase_check = "FAIL"

#number check
if re.search(r"\d", password):
  score += 1
  number_check = "PASS"
else:
  number_check = "FAIL"

#special character check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
  score += 1
  special_check = "PASS"
else:
  special_check = "FAIL"

#rating of password
if score <= 2:
  rating = "WEAK"
elif score <= 4:
  rating = "MODERATE"
else:
  rating = "STRONG"
  
#generates a security report
print("\nPASSWORD STRENGTH REPORT")
print("-" * 30)

#displays results
print(f"Length: {length_check}")
print(f"Uppercase: {uppercase_check}")
print(f"Lowercase: {lowercase_check}")
print(f"Numbers: {number_check}")
print(f"Special Characters: {special_check}")
print(f"\nStrength Rating: {rating}")
  

