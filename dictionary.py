def poorhash(x):
	"""
	This function simulates hashing where collisions
	are very likely.
	"""
	return hash(x)%10

def search(L, query):
	"""
	I chose to have 'search' as a seperate function so it can be
	used throughout the module.
	The function returns the index of the first item in L equal to query or 
	the next largest item.
	"""
	low, high = 0, len(L)
	while low < high:
		mid = (low + high)//2
		if query <= L[mid][0]:
# if query is less than one at current index
			high = mid
		else:
			low = mid +1
	return low

def insert(key, value, D, hasher=hash):
	
	"""
	This function inserts the tuple (h, key, value),
	where h = hash(key), into the list D. D is constructed
	so it has the same behavior as a dictionary; thus,
	if a key is already in D and it's being inserted again,
	the tuple is then overwritten with the new value. In order
	to allow rapid look up of the key-value pair, the list is
	ordered by the hash values, so that binary search can be
	used to rapidly locate the relevant tuple. The function is
	also constructed as to prevent hash collisions, by checking
	if there are more keys with the same hash value with a counter.
	"""

	index = search(D, hasher(key))

	while True:
		counter = 0
		for item in D[index:]:
			if item[0] == hasher(key):
				counter += 1
# if more of the same hash values, counter adds one
			else:
				break
		break
# this while loop gives the count of number of keys with same hash value in D
# fault-tolerance for hash collisions by using counter later in program

	if D == [] or index == len(D):	
		D.append((hasher(key), key, value))
		return D

	elif key not in [item[1] for item in D[index:index+counter+1]]:
# checking that key is not in yet in D for any place of it's hash value
		D.insert(index, (hasher(key), key, value))
		return D

	else: # if key is already in D
		for place, item in enumerate(D[index:index+counter+1]):
# have to iterate as key exists, and it is, possibly, amongst other keys with same hash value
			if item[1] == key:
				D[place+index] = (hasher(key), key, value)
# overwrite with new value if keys are equal; same behavior as normal dictionary
				return D
	
	
def get(key, D, hasher=hash):

	"""
	This function returns the value in dictionary D,
	corresponding to the given key. A KeyError is raised if
	the key is not in D.
	"""

	index = search(D, hasher(key))

	while True:
		counter = 0
		for item in D[index:]:
			if item[0] == hasher(key):
				counter += 1
# if more of the same hash values, counter adds one
			else:
				break
		break

	if key in [item[1] for item in D[index:index+counter+1]]:
# checking if key exists indexes with (possibly many) same hash values
			for item in D[index:index+counter+1]: # iterating over possible keys
# iterating to find key in its hash value(s) (if more keys have same hash value)
				if item[1] == key: # found desired key
					return item[2]
	raise KeyError('key is not in D')


def pop(key, D, hasher=hash):
	
	"""
	This function returns the value in list dictionary D
	corresponding to the given key and removes the key-value
	pair from D. A KeyError is raised if the key is not in D.
	"""

	index = search(D, hasher(key))

	while True:
		counter = 0
		for item in D[index:]:
			if item[0] == hasher(key):
				counter += 1
# if more of the same hash values, counter adds one
			else:
				break
		break

	if key in [item[1] for item in D[index:index+counter+1]]:
# checking if key exists indexes with (possibly many) same hash values
			for place, item in enumerate(D[index:index+counter+1]):
# iterating to find key in its hash value(s) (if more keys have same hash value)
				if item[1] == key: # found desired key
					value = item[2]
					D.pop(index+place)
# popping the key-value pair at index of chosen key
					return value

	raise KeyError('key is not in D')


def keys(D):
	"""
	This functions returns a list of the keys in D.
	"""

	return [t[1] for t in D]

def values(D):
	"""
	This functions returns a list of the values in D.
	"""

	return [t[2] for t in D]

def items(D):
	"""
	This functions returns a list of tuples of key-value pairs in D.
	"""

	return [(t[1],t[2]) for t in D]



"""
I used the same generated list D by test_insert for all
test functions because lists are mutable, which is very
convenient for the test functions.
"""

def test_insert(D=[], hasher=poorhash):
	"""This function tests whether 'insert' function can
	correctly construct a dictionary of the list of words
	'words' by inserting each word into D."""

	words = ['DRACULA', 'A', 'Mystery', 'Story', 'a', 'A', 9 , 'a dog', 'a cat', 'sheep']
	# only one 'A' should appear in D

	for index, word in enumerate(words):
		insert(word, index, D, hasher)
		# index used in 'for loop' as an easy method to have different values for each key for testing purposes
	
	return D

def test_get(D=test_insert(), hasher=poorhash):
	
	"""
	This function tests whether 'get' function can
	correctly return the value from dictionary D correpsonding
	to a given key; in this test functions, the key is 'a',
	which should indeed be in D, a dictionary that was contructed
	by the test_insert function, and should have the value of 4.
	"""

	return get('a', D, hasher)
	# should be 4 as it is index value of 'a' in 'words' list in test_insert()

def test_pop(D=test_insert(), hasher=poorhash):
	"""
	This function tests whether 'pop' function can
	correctly return a value from dictionary D correpsonding
	to a given key and remove the key-value pair from D;
	in this test functions, the value of key 'A' should be returned,
	which should be 5, as seen in D that was contructed by
	the test_insert function.
	"""

	return pop('A', D, hasher)
	# should give value of 5, the index value of the last 'A' in 'words' list in test_insert() because last called value replaces

def test_keys(D=test_insert()):
	"""
	This function tests whether 'keys' function
	indeed returns all keys in D.
	"""
	return keys(D)
	# notice, 'A' no longer in D as it was popped

def test_values(D=test_insert()):
	"""
	This function tests whether 'values' function
	indeed returns all values in D.
	"""
	return values(D)

def test_items(D=test_insert()):
	"""
	This function tests whether 'items' function
	indeed returns all tuples of key-value pairs in D.
	"""
	return items(D)

def test_all():
	print("Test functions using poorhash:")
	print('Dictionary D constructed by test_insert:', test_insert())
	print('Value for the key "a":', test_get())
	print('Value of pooping off "A":', test_pop())
	print('All keys in D ("A" is popped off):', test_keys())
	print('All values in D:', test_values())
	print('All tuples of key-value pairs in D:', test_items())
	print("\n""Test functions using hash:")
	print('Dictionary D constructed by test_insert:', test_insert(hasher=hash))
	print('Value for the key "a":', test_get(hasher=hash))
	print('Value of pooping off "A":', test_pop(hasher=hash))
	print('All keys in D ("A" is popped off):', test_keys())
	print('All values in D:', test_values())
	print('All tuples of key-value pairs in D:', test_items())


if __name__ == "__main__":
	test_all()






