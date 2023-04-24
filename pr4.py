s = "dvdf"

class Solution:
    
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        max_len, start = 0, 0
        for i, c in enumerate(s):
            print('In for Loop')
            while c in char_set:
                print('In While Loop')
                print('s[start]: ',s[start])
                char_set.remove(s[start])
                start += 1
            char_set.add(c)
            print('char_set:',char_set)
            max_len = max(max_len, i - start + 1)
            print('max_len: ',max_len)
        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
            