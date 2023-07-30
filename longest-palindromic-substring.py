def longestPalindrome(s: str) -> str:
        longest = ''
        l = 0
        r = 0
        while r < len(s):
            curString = s[l:r]
            if sorted(curString) == curString:
                longest = curString if (len(curString) > len(longest)) else longest
            r += 1
        
        return longest

print(longestPalindrome('abbda'), " answer")

print(longestPalindrome('babab'))

print(longestPalindrome('absdfgda'))