class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # Initialize a variable to count the pairs
        pair_count = 0

        # Iterate through each word in the list
        for i, source_word in enumerate(words):
            # Compare with every other word in the list that comes after the current word
            for target_word in words[i + 1:]:
                # Increase the count if target_word starts and ends with source_word
                pair_count += target_word.endswith(source_word) and target_word.startswith(source_word)

        # Return the total count of pairs
        return pair_count