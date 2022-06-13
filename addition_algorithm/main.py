def get_max(num1, num2):

	"""Return the largest number in size."""
	return max(len(str(num1)), len(str(num2)))

def to_string(num1, num2, size):

	"""Transform int to string in order to apply leading zeroes."""
	num1 = str(num1).zfill(size)
	num2 = str(num2).zfill(size)

	# string to list:
	num1 = list(num1)
	num2 = list(num2)

	return num1, num2

def add(num1, num2):

	"""Apply paper/pen method."""

	# initializing list, will contain the final result
	result = []

	# initializing carrier 
	carrier = 0

	for i in range(size - 1, -1, -1):

		# sum current column (backwards)
		temp = int(num1[i]) + int(num2[i]) + carrier

		# store the units (and carrier if needed)
		if temp // 10 > 0:
			column_digit = temp % 10
			carrier = temp // 10 
		else:
			column_digit = temp % 10
			carrier = 0

		# adding digit (backwards)
		result.insert(0, column_digit)

	# in the end, add remaning carrier
	if i == 0 and carrier != 0:
		result.insert(0, carrier)

	# to string
	result = [str(n) for n in result]

	return result

def print_result(num1, num2, result):

	result = ' '.join(result)
	line = '-' * len(result)

	# if result has more digits than the numbers, add leading spaces to align everything
	num1 = ' '.join(num1)
	num2 = ' '.join(num2) + ' +'

	diff1 = len(result) - len(num1)
	diff2 = len(result) - len(num2)
	diff = max(diff1, diff2)

	# applying leading spaces
	num1 = ' ' * diff + num1
	num2 = ' ' * diff + num2	

	print(num1)
	print(num2)
	print(line)
	print(result)

# input
num1 = int(input('Write a number: '))
num2 = int(input('Write another number: '))

# operations
size = get_max(num1, num2)
num1, num2 = to_string(num1, num2, size)
result = add(num1, num2)

# print
print_result(num1, num2, result)