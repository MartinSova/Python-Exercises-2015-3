from anagram import make_anagram_dict, read_words


def anaquery(d):

	"""This function repeatedly asks the user for a word and prints its
	anagrams (if any) that were found 'd' (the argument), which
	is a dictionary constructed from a certain number of words
	where the key is a value of the letters of the word sorted into
	an alphabetical order and where the key's values are the anagrams."""

	while True:
		word = input("Write a word for which you wish to find anagrams: ")
# do not have to assert to check if word is a string, as else statement will simply state "was not found in the provided dictionary"
		alph = ''.join(sorted(word))
		if alph in d:
			if d[alph] == [word]:
			# if word has no anagrams
				print(word, "has no anagrams")
			else:
				for value in d[alph]:
					if value != word:
					# an 'if' statement to not print the word itself, only anagrams
						print(value) 
		else:
			print(word, 'was not found in the provided dictionary.')
	
if __name__ == "__main__":
	anaquery(make_anagram_dict(read_words()))


