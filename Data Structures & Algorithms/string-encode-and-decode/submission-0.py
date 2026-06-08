from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            word_length = len(word)
            encoded_string += str(word_length) + "#" + word

        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_words = []
        index = 0

        while index < len(s):
            # Find where the length number ends.
            delimiter_index = index

            while s[delimiter_index] != "#":
                delimiter_index += 1

            # Extract the length number and convert it to an integer.
            word_length = int(s[index:delimiter_index])

            # The word starts right after the "#".
            word_start = delimiter_index + 1

            # The word ends after reading exactly word_length characters.
            word_end = word_start + word_length

            # Extract the original word.
            word = s[word_start:word_end]
            decoded_words.append(word)

            # Move index to the start of the next encoded word.
            index = word_end

        return decoded_words