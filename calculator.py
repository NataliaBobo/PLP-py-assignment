# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator(+,-,/,*)")

if operator == '+':
    result = num1+num2
    print(result)

elif operator == '-':
    result = num1-num2
    print(result)

elif operator == '*':
    result = num1*num2
    print(result)    

elif operator == '/':
    result = num1/num2
    print(result)

else: print("Invalid operator! Please enter +,-,*,/")    