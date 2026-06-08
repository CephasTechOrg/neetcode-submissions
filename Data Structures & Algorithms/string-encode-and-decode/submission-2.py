from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            # Store each string as: length + "#" + string
            # Example: "light" becomes "5#light"
            res.append(str(len(s)))
            res.append("#")
            res.append(s)

        # Join all parts into one encoded string.
        # Example: ["light", "book"] becomes "5#light4#book"
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # Keep decoding while i is still inside the encoded string.
        # When i reaches len(s), there is nothing left to decode.
        while i < len(s):
            # j starts where i starts.
            # i points to the beginning of the length number.
            j = i

            # Move j until it finds "#".
            # The number between i and j is the length of the next string.
            while s[j] != "#":
                j += 1

            # Extract the length number.
            # Example: in "5#light", s[i:j] is "5".
            length = int(s[i:j])

            # Move i to the first character after "#".
            # This is where the actual string starts.
            i = j + 1

            # Move j to the end of the actual string.
            # Example: if i points to "l" in "light" and length is 5,
            # then j moves 5 steps ahead, right after "light".
            j = i + length

            # Extract the actual string from i up to, but not including, j.
            res.append(s[i:j])

            # Move i to the start of the next encoded string.
            i = j

        return res