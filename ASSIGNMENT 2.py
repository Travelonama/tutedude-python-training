'''
num=int(input('Enter a number:'))

if num % 2 == 0:
    print(f"{num} is an even number.")

else:
    print(f"{num} is an odd number")
'''

# Initialize a variable to store the sum
total_sum = 0

# Iterate over numbers from 1 to 50 (inclusive)
for number in range(1, 51):
    total_sum += number  # Add the current number to the total sum

# Display the final sum
print("The sum of numbers from 1 to 50 is:", total_sum)

