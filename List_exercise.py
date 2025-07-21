

nums = [1, 2, 3 , 4, 5, 6]
even_num= []
for i in nums:
    if i%2==0:
        even_num.append(i)
print(even_num)

lst = [1, 2, 3, 4, 5]
new_list = []
for i in lst:
    new_list.append(i*i)
print(new_list)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print(common)

num = [1, 2, 3, 4, 5]
odd_sum = 0
even_sum = 0
for i in num:
    if i%2==0:
        even_sum += i
    else:
        odd_sum += i
print(even_sum)
print(odd_sum)

fruits = ["Apple", "banana", "Apple", "cherry", "Apple"]

for i in fruits:
    if i== "Apple":
        fruits.remove(i)
print(fruits)

numbers = [10, 20, 4, 45, 99]
unique_number = list(set(numbers))
unique_number.sort()
second_largest = unique_number[-2]
print(second_largest)

