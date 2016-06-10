def read_words():
	"""
	This function returns a list of words in
	words.txt.
	"""
	return open('words.txt', 'r').read().lower().splitlines()

def make_anagram_dict(words):
	"""
	This function constructs and returns a dictionary whose keys
	are the letters of a word sorted into alphabetical order
	and whose values are lists of all the words with that key.
	All words are imported as a list through the argument 'words'.
	"""

	dic = dict()
	for word in words:
		alph = ''.join(sorted(word))
		if alph not in dic:
# if alph not yet created, word is first value
			dic[alph] = [word]
		elif word not in dic[alph]:
			dic[alph].append(word)
# append word if alph already created
	return dic

def most_variants(d):
	"""
	This function finds and prints the key(s)
	and its corresponding anagrams (values)
	in dictionary 'd' (the argument
	defined by make_anagram_dict function
	using the file 'words.txt')
	that have the largest number of anagram
	variants (values) out of all keys in 'd'.
	"""

	most_values = max(len(v) for v in d.values())
	# number of most values for a key in d

	for key in d: 
	# iterating over d because more keys can have 'most_values' values
		if len(d[key]) == most_values:
			print(key, d[key])

def longest_pair(d):

	"""
	This function finds and prints the key(s)
	and its corresponding anagrams (values)
	in dictionary 'd' (the argument
	defined by make_anagram_dict function
	using the file 'words.txt')
	that have the longest pair of anagrams
	out of all keys and in 'd'.
	"""

	new_dic = dict()

	for k in d:
	# first, make a dictionary with all keys in d that have more values than one
	# hence, all keys in new_dic has at least two values
		if len(d[k]) > 1:
			new_dic[k] = d[k]


	longest = max(len(k) for k in new_dic)
	# the value of longest key in new_dic, since length of key = length of value

	for k in new_dic:
	# iterating over new_dic because more keys can have 'longest' length
		if len(k) == longest:
			print(k, new_dic[k])



if __name__ == "__main__":
	print("anagrams with the greatest number of variants:")
	most_variants(make_anagram_dict(read_words()))
	print("anagrams that have the longest pair of anagrams:")
	longest_pair(make_anagram_dict(read_words()))


