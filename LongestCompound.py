#Brute Force Method using Recursion
#The space complexity is O(w^2) to create subwords where w is word length
#The time complexity is O(w^2), where w is the word length


def LongestCompound(word, wordList):
	sub=''

	#Iterating from 1 to length of the word
	for index in range(len(word)):
		#We keep adding a letter to build the substring
		sub += word[index]
		#Checking if substrong is in the world list
		if sub in wordList:
			#if we are the end, we return True since it is the end of a word
			if index == len(word)-1:
				return True

			# There is where the magic happens
			# Recursively calling Longest Compound but now we pass one less letter into the recursion
			#for example, if the previously passed word was ramy, now we pass amy.
			return LongestCompound(word[index+1:], wordList)
	return False

def main():
	#Opening text file
	best = ''
	file = open("words.txt")

	#reading the file into the content variable
	content = file.read()

	#Parsing file into an array called words
	words = content.splitlines()

	for index in range(len(words)):
		#Simply checking if the word length at index is greater than the current best
		#if so, we reassign best to the new best
		if len(words[index]) > len(best):
			newWorldList = words.copy()
			newWorldList.pop(index)
			if LongestCompound(words[index], newWorldList):
				best = words[index]

	print("The longest compound word: " + best)

main()

