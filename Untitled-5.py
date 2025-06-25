num = int(input("Enter a number: "))
odd_numbers = [x for x in range(num) if x % 2 != 0]
print("Odd numbers under", num, ":", odd_numbers)

even_numbers = [x for x in range(num) if x % 2 == 0]
print("Even numbers under", num, ":", even_numbers)

fruits = ["banana", "apple", "cherry", "mango", "grape"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Updated fruit names:", capitalized_fruits)
