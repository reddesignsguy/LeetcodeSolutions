class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            largest_pal_around_this_center = ""

            # If chars are the same, then s[i:j+1] is a palindrome
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j + 1 - i > len(largest_pal_around_this_center):
                    largest_pal_around_this_center = s[i:j+1]
                i -= 1
                j += 1

            return largest_pal_around_this_center
            

        # For every character, expand in an odd way or even way
        largest_pal = ""
        for i in range(len(s)):
            largest_odd_pal = expand(i, i)
            largest_even_pal = expand(i, i+1)

            if len(largest_odd_pal) > len(largest_pal):
                largest_pal = largest_odd_pal
            if len(largest_even_pal) > len(largest_pal):
                largest_pal = largest_even_pal

        return largest_pal