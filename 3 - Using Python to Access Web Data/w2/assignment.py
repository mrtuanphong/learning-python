import re

# Open file and read the content:
#file = open('regex_sum_42.txt')
file = open('regex_sum_628636.txt')
text = file.read()

total = 0

# Get all the numbers:
numbers = re.findall('[0-9]+', text)

# Calculate for the total:
for num in numbers:
  total = total + int(num)

# Print the result:
print(total)