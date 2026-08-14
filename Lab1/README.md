## Lab 1 – Python Programs
## 1. Variable and Identifier Practice

Aim:
To declare variables for name, age, height, and student status, and display their values along with their data types.

Logic:
Declare variables with appropriate values and data types. Use type() to determine and display the data type of each variable.

Sample Input / Output:

Harshil Soni     <class 'str'> 
 20      <class 'int'> 
 178     <class 'int'> 
 True    <class 'bool'>

## 2. Greeting Program

Aim:
To take the user's name, age, and city as input and display them together using an f-string.

Logic:
Take the name, age, and city from the user using input(). Convert the age to an integer and use an f-string to combine all three values into a single sentence.

Sample Input / Output:

Enter your name: Harshil
Enter your age: 20
Enter your city: Indore
Hello Harshil from Indore and of age 20!

## 3. Arithmetic Operations

Aim:
To perform basic arithmetic operations on two numbers entered by the user.

Logic:
Take two numbers as input and convert them to numeric values. Calculate their sum, difference, product, quotient, and remainder using Python arithmetic operators.

Sample Input / Output:

Enter first number: 2
Enter Second number: 3
Addition = 5
Subtraction = -1
Multiplication = 6
Division = 0.6666666666666666 

## 4. Celsius to Fahrenheit

Aim:
To convert a temperature given in Celsius to Fahrenheit.

Logic:
Take the temperature in Celsius as input and convert it to a float. Apply the Celsius-to-Fahrenheit formula and display the resulting temperature.

Sample Input / Output:

Enter current temperature (in C): 32
Temperature in fahrenheit = 89.6

## 5. String Manipulation

Aim:
To perform different string operations on a user's full name.

Logic:
Take the user's full name as input. Use string methods to display the name in uppercase and lowercase, use slicing to reverse it, and use len() to find its length.

Sample Input / Output:

Enter your full name: Harshil Soni
upper = HARSHIL SONI
lower = harshil soni
reversed = inoS lihsraH
reversed by word = Soni Harshil
length = 12

## 6. Escape Sequence Practice

Aim:
To create a simple receipt using \t and \n escape sequences for neat formatting.

Logic:
Use \t to create spacing between item names and prices. Use \n to place each item on a separate line and format the output like a small receipt.

Sample Input / Output:

Item            Price
Milk            ₹60
Bread           ₹40
Eggs            ₹70
Rice            ₹120
Apples          ₹150

## 7. Menu-Driven Calculator

Aim:
To create a menu-driven calculator that performs addition, subtraction, multiplication, and division, and continues running until the user chooses to exit.

Logic:
Display a menu with four arithmetic operations and an exit option. Use a while loop to repeatedly accept the user's choice and perform the selected operation. Handle invalid numeric input using try-except and prevent division by zero.

Sample Input / Output:

Menu:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit


Enter choice: 1
Enter first number: 20
Enter second number: 5
Result: 20.0 + 5.0 = 25.0


Enter choice: 3
Enter first number: 7
Enter second number: 6
Result: 7.0 * 6.0 = 42.0


Enter choice: 4
Enter first number: 20
Enter second number: 4
Result: 20.0 / 4.0 = 5.0


Enter choice: 5