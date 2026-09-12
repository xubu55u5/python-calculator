num1 = float(input("Первое число "))
operator = input("Операция (+, -, *, /): ")
num2 = float(input("Второе число "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Неизвестная операция"

print("Результат", result)
