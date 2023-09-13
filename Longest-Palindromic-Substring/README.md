# Code
```
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
```

# Intuition
##### 1) The first step to solving this is **defining what a palindrome is in our problem**. That is, a string that has mirrored characters around its center. 

Examples: "a", "bab" "ababa" "abba"

A string's center is determined by if the string is odd or even. This is important because we should generally consider these two cases as different when determining if a string is a palindrome or not.

**If it's odd:**
- a is the center of "a"
- a is the center of "bab"

**If it's even:**
- bb is the center 

##### 2) A string can be checked to be a palindrome by using two pointers o(n^3) 

The intuitive approach would be to compare the string's first character and the string's second character and do the same for every pair of characters towards the center. This approach checks for a palindrome **inwards** For example, to check "babab":

Compare 
* s[0]=b, s[4]=b
* s[1] = a, s[3] = a
* s[2] = b, s[2] = b

This process takes o(n) time. If repeat this for every substring in s, then the final time complexity would be o(n^3). **Is there a way to reduce it to o(n^2)?**


##### 3) Optimizing to O(n^2)

Checking if a string is palindrome will always take o(n), so we should shift our focus on optimizing checking for every substring, which is a costly operation.

**Let's consider a case: "123456aba" where "aba" is the largest palidrome.**

Remember that a palindrome is a string that has mirrored characters around its center. In this case, 4 is the center (123 4 567). **We know this is a palindrome because single characters are always palindromes.** The next logical step would be to check the characters around 4, that is, is 345, which is clearly not a palindrome. Checking 23456 and 1234567 would be redundant because 345 is not a palindrome. Here, we check if a string is a palindrome **outwards**. 

With this "expansion" method, we realize that we're not just checking if 1234567 is a palindrome, but we also derive what the longest palindrome inside it is (in this case 4). We keep expanding outwards until we have reached a substring that isn't a palindrome (in this case 345). This takes o(n).

**Wait! Roll that back.**

We just discovered that this expansion method gives us the longest palindrome, i.e: the problem we're solving, when **we give it a center, not a substring.** In other words, we have found a solution that doesn't require us to look through every substring "12, 123, 1234 ...", but rather every individual character "1, 2, 3, 4, 5, 6, 7, a, b, a". Essentially, we can treat every individual character as a center and perform the expansion method on it, resulting in a time of [o(n^2)].

##### Side Note:
An even more useful fact we have learned is the differences between checking a palindrome from the center vs. the edges.

**Checking from the edges:**
* Determines if string is a palindrome

**Checking from the center:**
* Determines if string is a palindrome 
* Determines the longest palindrome within the string

We can clearly see that checking from the center offers more benefits and may be useful for other algorithmic problems.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Treat each character in s as a center, and perform an expansion on it
2. Define "expansion" as:
a) Initializing 2 pointers, $$i$$ and $$j$$ where $$i=j$$, essentially starting with a single-character palindrome.
b) Evaluating $$s[i] == s[j]$$
c) If above is true, s[i:j+1] is a palindrome, then expanding by performing $$i--$$ and $$j++$$ and repeating the above steps. Otherwise, stop
d) As more palindromes are found, compare this with the longest palindrome found so far.
3. Edge case: We still need to check for even palindromes, and we know that they will always have a center that is 2 characters long. Therefore, for even palindrome, all we need to do is expand around i, i+1. (Use "1xabbay2" to test this theory)

# Complexity
- Time complexity:
o(n^2)

- Space complexity:
o(1)
