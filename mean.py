# Print the mean of numbers in file data.txt

import sys

sum = 0
n = 0

# Modifying Chris' program

# Sum input values
for numb in open('data.txt'):
	sum += float(numb)
	n += 1

print "The mean is: " 
print sum / n
