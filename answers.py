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