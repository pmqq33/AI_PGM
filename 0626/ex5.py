#1
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f"You entered: {a} and {b}")

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")

#2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))

numlist = [num1, num2, num3, num4, num5]

print(f"합: {sum(numlist)}")
print(f"평균: {sum(numlist)/len(numlist)}")
print(f"최대값: {max(numlist)}")
print(f"최소값: {min(numlist)}")

#3
b = []
list1 = input("Enter first fruit: ")
b.append(list1)
list2 = input("Enter second fruit: ") 
b.append(list2)
list3 = input("Enter third fruit: ")
b.append(list3)

print(f"첫 번째 과일: {b[0]}")
print(f"마지막 과일: {b[-1]}")