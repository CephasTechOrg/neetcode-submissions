class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups is our hash map.
        #
        # It will store:
        # fingerprint -> list of words with that same fingerprint
        #
        # Example idea:
        # fingerprint for "act" and "cat" -> ["act", "cat"]
        # fingerprint for "pots", "tops", "stop" -> ["pots", "tops", "stop"]
        groups = {}

        # Go through each word in the input list one by one.
        #
        # Example:
        # strs = ["act", "pots", "tops", "cat", "stop", "hat"]
        #
        # word will become:
        # "act", then "pots", then "tops", then "cat", etc.
        for word in strs:

            # Create 26 empty counters.
            #
            # Each position represents one lowercase English letter.
            #
            # Important:
            # The list does NOT actually contain the letters "a", "b", "c", etc.
            # It only contains numbers.
            #
            # But we agree that:
            # count[0] represents "a"
            # count[1] represents "b"
            # count[2] represents "c"
            # ...
            # count[25] represents "z"
            #
            # So these zeros are like empty boxes/placeholders for letter counts.
            count = [0] * 26

            # Now we go through every character inside the current word.
            #
            # Example:
            # if word = "act"
            #
            # char will become:
            # "a", then "c", then "t"
            for char in word:

                # This line connects the character to the correct position in count.
                #
                # ord(char) gives the hidden number/code of the character.
                #
                # Examples:
                # ord("a") - ord("a") = 0
                # ord("b") - ord("a") = 1
                # ord("c") - ord("a") = 2
                # ord("t") - ord("a") = 19
                #
                # So:
                # "a" is linked to count[0]
                # "b" is linked to count[1]
                # "c" is linked to count[2]
                # "t" is linked to count[19]
                #
                # Again, the letter is not physically stored in count.
                # The formula gives us the index where that letter's count lives.
                index = ord(char) - ord("a")

                # This is where we build the word's fingerprint.
                #
                # We go to the box for this character and increase it by 1.
                #
                # Example with word = "act":
                #
                # char = "a"
                # index = 0
                # count[0] += 1
                # This means "a" appeared once.
                #
                # char = "c"
                # index = 2
                # count[2] += 1
                # This means "c" appeared once.
                #
                # char = "t"
                # index = 19
                # count[19] += 1
                # This means "t" appeared once.
                #
                # After the whole word is counted, the count list becomes
                # the fingerprint of that word.
                count[index] += 1

            # At this point, we have finished counting all characters in the word.
            #
            # So count is now the fingerprint of the whole word.
            #
            # Example:
            # word = "act"
            #
            # fingerprint means:
            # a appeared 1 time
            # b appeared 0 times
            # c appeared 1 time
            # d appeared 0 times
            # ...
            # t appeared 1 time
            # ...
            # z appeared 0 times
            #
            # "cat" will create the exact same fingerprint because it also has:
            # a: 1, c: 1, t: 1
            #
            # We convert count to a tuple because lists cannot be dictionary keys.
            # Lists can change, so Python does not allow them as keys.
            #
            # Tuples cannot change, so they are safe to use as dictionary keys.
            #
            # So key is the frozen fingerprint of this word.
            key = tuple(count)

            # Check if this fingerprint already has a group.
            #
            # Meaning:
            # Have we seen another word with this exact same letter-count fingerprint?
            #
            # Example:
            # If word = "act", maybe this fingerprint is new.
            # So we create a new group.
            #
            # If word = "cat", it creates the same fingerprint as "act".
            # So this key already exists, and we do not create a new group.
            if key not in groups:

                # Create a new empty group for this fingerprint.
                #
                # This means:
                # "Any word with this exact fingerprint should be placed in this list."
                groups[key] = []

            # Add the current word into the group for its fingerprint.
            #
            # Example:
            #
            # For "act":
            # groups[fingerprint_for_act].append("act")
            # group becomes ["act"]
            #
            # For "cat":
            # "cat" has the same fingerprint as "act"
            # groups[fingerprint_for_act].append("cat")
            # group becomes ["act", "cat"]
            #
            # That is how anagrams end up in the same group.
            groups[key].append(word)

        # groups is a dictionary like:
        #
        # {
        #   fingerprint_for_act_cat: ["act", "cat"],
        #   fingerprint_for_pots_tops_stop: ["pots", "tops", "stop"],
        #   fingerprint_for_hat: ["hat"]
        # }
        #
        # But the final answer does not need the fingerprints.
        # It only needs the grouped words.
        #
        # groups.values() gives us:
        # ["act", "cat"]
        # ["pots", "tops", "stop"]
        # ["hat"]
        #
        # list(groups.values()) turns that into:
        # [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
        return list(groups.values())