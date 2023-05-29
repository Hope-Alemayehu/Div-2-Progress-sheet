class Solution:
    def frequencySort(self, s: str) -> str:
        # frequency dictionary
        freq_dict = collections.Counter(s)

        #Sort characters based on frequency
        sorted_chars = sorted(freq_dict, key=freq_dict.get, reverse=True)

        # the sorted string
        sorted_string = ""
       
        for char in sorted_chars:
            sorted_string += char * freq_dict[char]

        return sorted_string
