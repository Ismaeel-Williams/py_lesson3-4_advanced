#Question 1
a = 5
b = 10
c = 22

a += 3
b *= 2
c %= 4

d = a**2 + b**2 + c**2

print(round(d, 2))

#question 2 
integer1 = int(input("Enter first whole number: "))
integer2 = int(input("Enter second whole number: "))
integer3 = int(input("Enter third whole number: "))

is_even = integer1 % 2 == 0
is_positive = integer2 > 0
is_greater_than_ten = integer3 > 10

print("Is the first number even?", is_even)
print("Is the second number positive?", is_positive)
print("Is the third number greater than ten?", is_greater_than_ten)

final_condition = is_even and is_positive and is_greater_than_ten
print("Final condition", final_condition)

#question 3
base_score = int(input("Enter your base score: "))
bonus_points = 5
late_penalty = -10

final_score = base_score + bonus_points + late_penalty
final_score = max(0, min(final_score, 100))
print("Final score:", final_score)

if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "B"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"
elif final_score >= 50:
    grade = "E"
else:
    grade = "F"
print("Grade:", grade)

#Question 4
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = n1 + n2
elif operation == "-":
    result = n1 - n2
elif operation == "*":
    result = n1 * n2
elif operation == "/":
    if n2 != 0:
        result = n1 / n2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print("Result:", result)