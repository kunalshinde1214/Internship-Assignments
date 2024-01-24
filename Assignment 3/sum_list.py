def sum_list(numbers):
    return sum(numbers)

list = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    element = int(input())
    list.append(element)
result = sum_list(list)
print("Sum of the list:", result)
