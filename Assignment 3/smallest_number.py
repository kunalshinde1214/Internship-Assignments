def smallest_number(numbers):
    return min(numbers)

list = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    element = int(input())
    list.append(element)
result_min = smallest_number(list)
print("Smallest number in the list:", result_min)
