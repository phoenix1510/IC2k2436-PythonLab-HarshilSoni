"""Take temperature in Celsius as input. Convert it to a number, then compute and print the Fahrenheit value.
 Formula: F = (C * 9/5) + 32"""
Temp=float(input("Enter current temperature (in C): "))
fahrenheit= (Temp*(9/5)) + 32
print(f"Temperature in fahrenheit = {fahrenheit}")