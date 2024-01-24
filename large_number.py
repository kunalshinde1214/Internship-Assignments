def large_number(numbers):
    return max(numbers)

list = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    element = int(input())
    list.append(element)
resultmax = large_number(list)
print("Largest number in the list:", resultmax)
