I implemented a brute force method for the longest-compound problem

Brute Force Method:

- We check if all prefixes word[:x] are present for each word.
- I Used sets to store all the words.
- Whenever we find a better word, we check for all the prefixes. 
- Then we would replace our result.

The algorithm goes as follows:
- For every word in the text file we check if the length of the word is greater than the length of the current best. 
- If this condition were to be met, we iterate through every substring possible to find the new best long compound word. 

The space complexity is O(w^2) to create subwords where w is word length
The time complexity is O(w^2), where w is the word length


STEP FURTHER:

If I were to take this a step further, I know the better approach
would be to use Tries since this involves prefix strings. 
My Intuituin would be to put every word from the file into a trie. 
Since we want to look for the longest compount word, we would want to apply 
a depth first search from the top of the trie. You have to search nodes that were 
the last letter of a word.So we would pronably have some boolean variable to help us with that. 
The node that is found is a word with all the prefixes and we keep doing that and pick the best word.
'''