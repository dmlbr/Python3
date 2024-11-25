# Arithmetic operators in Python
# Python 3.7.9
# https://docs.python.org/3.7/reference/expressions.html#operator-precedence

print("Test arithmetic operators in Python")
print()

print("Give me first number")
numberOne = int(input())
print("Give me first number")
numberTwo = int(input())


print()
resultAddition = str(numberOne + numberTwo)
print("\"+\" result operation is " + resultAddition)
print()


print()
resultSubtraction = str(numberOne - numberTwo)
print("\"-\" result operation is " + resultSubtraction)
print()

print()
resultMultiplication = str(numberOne * numberTwo)
print("\"*\" result operation is " + resultMultiplication)
print()

print()
resultDivision = str(numberOne / numberTwo)
print("\"/\" result operation is " + resultDivision)
print()

print()
resultExponention = str(numberOne ** numberTwo)
print("\"**\" -  exponentiation")
print("numberOne ** numberTwo")
print("result operation is ")
print(resultExponention)
print()

# 6.16. Operator precedence¶
# *, @, /, //, %
# Multiplication, matrix multiplication, division, floor division, remainder 5

"""
print()
resultMatrix = str(numberOne @ numberTwo)
print("\"@\" -  matrix")
print("numberOne @ numberTwo")
print("result operation is ")
print(resultMatrix)
print()
"""

print()
resultFloorDivision = str(numberOne // numberTwo)
print("\"//\" -  floor division")
print("numberOne // numberTwo")
print("result operation is ")
print(resultFloorDivision)
print()

print()
resultRemainder = str(numberOne % numberTwo)
print("\"%\" -  remainder")
print("numberOne // numberTwo")
print("result operation is ")
print(resultRemainder)
print()



