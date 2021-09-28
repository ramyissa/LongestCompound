The longest compound word that my algorithm produces is now: cyclotrimethylenetrinitramine
I am aware that this is the wrong ouput as my first attempt had the correct output but the algorithm was flawed, it would not work when random letters were in the words. 
But now i believe my code is more complete and correct even though the output is not exact.

Brute Force Method with recursion

Sumarizing code, see code for in line comments in longestCompound.py
-Iterating from 1 to length of the word
-We keep adding a letter to build the substring
-If we are the end of the word, we return True since it is the end of a word
-We then recursively call longestCompound but now we pass one less letter into rhe recursion, 
for example, we if the previously pass word was ramy, now we pass amy.

The space complexity is O(w^2) to create subwords where w is word length.
The time complexity is O(w^2), where w is the word length


STEP FURTHER:

If I were to take this a step further, I know the better approach
would be to use Tries since this involves prefix strings. 
My Intuituin would be to put every word from the file into a trie. 
Since we want to look for the longest compount word, we would want to apply 
a depth first search from the top of the trie. You have to search nodes that were 
the last letter of a word. So we would pronably have some boolean variable to help us with that. 
The node that is found is a word with all the prefixes and we keep doing that and pick the best word.
'''

