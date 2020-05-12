def compare(array1, array2):
    array1.sort()
    array2.sort()
    return "YES" if array1 == array2 else "NO"


array1 = []
array2 = []

for i in range(11):
    array1.append(input())

for i in range(11):
    array2.append(input())

print(compare(array1, array2))
