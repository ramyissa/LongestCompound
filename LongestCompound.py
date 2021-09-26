#Opening text file
file = open("words.txt")

#reading the file into the content variable
content = file.read()

#Parsing file into an array called words
words = content.splitlines()

'''
Brute Force Method:

- We check if all prefixes word[:x] are present for each word.
- I Used sets to store all the words.
- Whenever we find a better word, we check for all the prefixes. 
- Then we would replace our result.
- Further explaination in the README file.
'''

def longestCompoundWord(words):
	#Initializing the result variable
	best = ""

	#Initializing the word set with the word parsed from the text file
	w_set = set(words)

	#Iterating through each word in the set
	for word in words:
		#if the length of the word is greater than the previous we do the follwing:
		if len(word) > len(best):
			#We check if all prefixes word[:x] are present for each word
			for x in range(1, len(word)):
				#If the word is in the set then it is the newest longest word
				if word[:x] in w_set:
					best = word
	return best


def main():
	the_moment_of_truth = longestCompoundWord(words)
	print("The magical word is... " + the_moment_of_truth)


main()

