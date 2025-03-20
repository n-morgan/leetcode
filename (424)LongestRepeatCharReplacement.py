'''


You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.



'''


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        def most_freq(mappings):

            freq = -float('inf')

            for key,value in mappings.items():
                if value > freq:
                    freq = value 

            return freq
        
        mapping = {}
        longest = -float('inf')



        window_size = 1
        i = 0 

        if s[i] not in mapping:
            mapping[s[i]] = 0 
        mapping[s[i]] += 1

        while i + window_size < len(s):

            print("********")
            print(i, window_size) 
            print(mapping, most_freq(mapping))
            print(s[i:i+window_size])
            if window_size - most_freq(mapping) <= k:
                print("hereA")

                if window_size  > longest:
                    longest = window_size

                if s[i+window_size] not in mapping:
                    mapping[s[i+window_size]] = 0 
                mapping[s[i+window_size]] += 1 

                window_size += 1
            else:   
                print("here")

                mapping[s[i]] -= 1

                window_size -= 1
                i += 1

                if s[i+window_size] not in mapping:
                    mapping[s[i+window_size]] = 0
                mapping[s[i+window_size]] += 1 

                
        return window_size 


            
    

if __name__ == "__main__":
     
    solver = Solution()
    print(solver.characterReplacement("AABABBA", 0))


