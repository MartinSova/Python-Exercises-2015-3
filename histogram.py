from math import log
from anagram import read_words, make_anagram_dict

def histogram(x, y, width):
	"""This function draws a simple histogram of the
	numbers in y versus those in x. The 'width' argument
	controls the width (in stars) of the longest bar
	(of stars)."""

	if len(x) < len(y):
# fault-tolerance for when y is out of range of x
		y = y[:len(x)]
# y is shortened since a y value cannot be printed that doesn't have an x-value

	
	for index, number in enumerate(x):
		if index < len(y):
			print(number,'*'*round((width/max(y))*y[index]), y[index])
		else:
			print(number, 0)
			# when there are no more y-values for x, 0 is printed


def histogram_anagrams(d, width):

	"""Using the histogram() function, this function
	plots a histogram of log (base 10) of the number
	of values there are corresponding to values V
	for V = 2, . . . , 12 (the x-value: the number of
	variants that a key has) in dictionary 'd'. The
	'width' argument controls the width (in stars)
	of the longest bar (of stars)."""


	values_count = [0 for i in range(11)]

	# each item in values_count will be keeping count of a given V (number of variants)
		
	for key in d:

		for index, value in enumerate(list(range(2,13))):

			if value == len(d[key]):

				values_count[index] += 1

# when number of variants (value) equals to number of anagrams in key, 1 is added to respective counter in values_count 

	for index, num in enumerate(values_count):
	# taking a log of all values in values_count
		if num != 0: # log of 0 would be undefined
			values_count[index] = log(num,10)


	histogram(range(2,13), values_count, width)





if __name__ == "__main__":
   
	x = range(6)
	
	H = [12.5, 6.4, 10, 7.6, 8, 13]

	histogram(x, H, 30)

	print('\n')

	histogram_anagrams(make_anagram_dict(read_words()), 30)

