class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

 # input =  two strings, s & t
 # lowercase means only 26 characters allowed, hash table works better than hash maps
 # hash maps works for dynamic dataset

       if len(s) != len(t):     # anagrams means lenght should be the same   
           return False

# hash table (array) method:
       count = [0] * 26 # create the array

       for chars in range(len(s)):
           count[ord(s[chars]) - ord('a')] += 1 # access the array location by count[], and then convert s[chars] to ASCII using ord() and, 
           count[ord(t[chars]) - ord('a')] -= 1 # then subtract the reference point 'a' ASCII from each of s[chars] and t[chars] to create unique index value and keep a count

       for val in count:
            if val != 0:
                return False
       return True