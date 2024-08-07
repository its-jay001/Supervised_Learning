def print_multiples():
    num = int(input("Enter the number: "))
    limit = int(input("Enter the limit: "))
    print(*range(num, limit + 1, num))

# Call the function to execute
print_multiples()
