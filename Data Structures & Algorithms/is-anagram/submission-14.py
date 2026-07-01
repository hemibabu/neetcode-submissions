class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


 # input =  two strings, s & t
 # lowercase means only 26 characters allowed, hash table works better than hash maps
 # hash maps works for dynamic dataset

       if len(s) != len(t):     # anagrams means lenght should be the same   
           return False

# hash map method:
       hashmap_s, hashmap_t = {},{}

       for chars in range(len(s)):
            hashmap_s[s[chars]] = 1 + hashmap_s.get(s[chars], 0)
            hashmap_t[t[chars]] = 1 + hashmap_t.get(t[chars], 0)
       return hashmap_s == hashmap_t