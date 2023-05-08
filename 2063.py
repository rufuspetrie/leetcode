# Questions:
    # For a given word, how many possible substrings are there?
        # n + (n-1) + ... = n**2/2
    # For a for character at index i, how many substrings contain it?
        # choices for start * choices for end = (i + 1) * (n - i)
class Solution:
    def countVowels(self, word: str) -> int:
        vowel = "aeiou"
        n = len(word)
        total = 0
        for i, c in enumerate(word):
            if c in vowel:
                total += (i + 1) * (n - i)

        return total