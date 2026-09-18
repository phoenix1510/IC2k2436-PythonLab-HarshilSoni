"""Take a full name as input. Print it in uppercase, in lowercase, reversed, and print its length. Use at least three different string methods."""
Name=input("Enter your full name: ")
print(f"upper = {Name.upper()}")
print(f"lower = {Name.lower()}")
print(f"reversed = {Name[-1::-1]}")
words = Name.split()
reversedL = words[::-1]
print(f"reversed by word = {" ".join(reversedL)}")
print(f"length = {len(Name)}")