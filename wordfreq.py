from dictionary import insert, search
from operator import itemgetter

def freq(words):
	"""
	This function uses a dictionary-style list to 
	calculate how many times each
	word in the list of 'words' (the argument) appears,
	with the help of the 'insert' function from the
	dictionary module, and prints the 10 most
	frequently used words in 'words'. This function
	also accounts for possible hash collisions in
	the constructed dictionary D.
	"""

	D = [] # words we've seen


	for word in words:
		index = search(D, hash(word))

		while True:
# while loop used for fault-tolerance against hash collisions
			counter = 0
			for item in D[index:]:
				if item[0] == hash(word):
					counter += 1
# if more of the same hash value, counter adds one
				else:
					break
			break
		
		value = 1
		if word in [item[1] for item in D[index:index+counter+1]]:
# if word is any of the many possible keys with same hash values (as many as counted by 'counter')
			for item in D[index:index+counter+1]: # iterating over possible keys
				if item[1] == word: # if reached the word
					value = item[2]+1 # 1 is added to item value because word is reached
					break
			insert(word, value, D)
		else: # first time that word is seen
			insert(word, value, D)


	sort_freq = sorted(D, key=itemgetter(2), reverse = True)[:10]
# list of all key-value pairs is sorted in reverse based on values, and first ten most frequent as assigned to sort_freq

	for t in sort_freq: # 10 most frequent key-value pairs are printed
		print('%20s %d' % (t[1], t[2]))

if __name__ == "__main__":
	words = open('dracula.txt', 'r').read().lower().splitlines()
	freq(words)
