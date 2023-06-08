#!/usr/bin/python3

a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

sum_result = add(a, b)
diff_result = subtract(a, b)
prod_result = multiply(a, b)
quot_result = divide(a, b)

print("Sum: {}".format(sum_result))
print("Difference: {}".format(diff_result))
print("Product: {}".format(prod_result))
print("Quotient: {}".format(quot_result))
