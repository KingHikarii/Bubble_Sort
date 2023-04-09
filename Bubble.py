max_num = int(input("Enter the array's max: "))

numbers = []

for i in range(max_num):
    num = int(input("Enter a number: "))
    numbers.append(num)

for i in range(max_num):
    for j in range(max_num-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("This is the sorted array!")

print(numbers)
