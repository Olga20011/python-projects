num1 = int(input("enter first number;" ))
operator = input("enter operator;")
num2 = int(input("enter second number;"))
# if operator is (*|+|-|/|) then perform num1 (*|+|-|/|) num2
if operator == "*":
    print(num1*num2)
elif operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
else:
    print("invalid input")