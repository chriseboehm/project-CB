import sys

sum = 0
n = 0

# Modifying Chris' program

# Sum input values
for num in open('data.txt'):
	sum += float(num)
	n += 1

print "The mean is: " 
print sum / n
