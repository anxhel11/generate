import random

num_count = int(input("How many numbers would you like to generate? "))
numbers = [random.randint(1, 100) for i in range(num_count)]

print("Generated Numbers:", numbers)
print("Average:", sum(numbers) / len(numbers))

