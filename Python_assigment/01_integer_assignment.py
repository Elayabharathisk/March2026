# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
import math
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
# Your code here
a=1
for i in range (1,11):
    a=a*i
print(a)

# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
# Your code here
print(156%7)
# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
# Your code here
print(25**2)
# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
# Your code here
print(125**1/3)
# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
# Your code here
a=12345
b=0
while a>0:
    b+=a%10
    a=a//10
print (b)
# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
# Your code here
if((97%2)==0 or (97%3)==0):
    print("97 is not prime number")
else:
    print("97 is prime number")

# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
# Your code here
p=1
for i in range(1,8+1):
    p*=i
print(p)
# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
# Your code here
a=[15, 23, 31, 42, 56]
b=math.prod(a)
print(b/len(a))
# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
# Your code here
a=48
b=36

print(f"the gdc of 48 and 36 is , {math.gcd(a,b)}")
# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
# Your code here 
f=0
c=0
for i in range(1,100,2):
    f+=i
    c+=1
    if(c==20):
        break
print(f)