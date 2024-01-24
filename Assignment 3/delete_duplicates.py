def delete_duplicates(numbers):
    return list(set(numbers))

list1 = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    element = int(input())
    list1.append(element)
result_no_duplicates = delete_duplicates(list1)
print("List with duplicates removed:", result_no_duplicates)
