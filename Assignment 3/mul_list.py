def mul_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

list = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    element = int(input())
    list.append(element)
result1 = mul_list(list)
print("Product of the list:", result1)
