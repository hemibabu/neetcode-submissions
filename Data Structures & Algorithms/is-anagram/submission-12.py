class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


 # input =  two strings, s & t
 # lowercase means only 26 characters allowed, hash table works better than hash maps
 # hash maps works for dynamic dataset

       if len(s) != len(t):     # anagrams means lenght should be the same   
           return False

# hash map method:
       hashmap_s = {}
       hashmap_t = {}
       # create dict for s
       for chars in s:
            if chars in hashmap_s:
                hashmap_s[chars] += 1
            else:
                hashmap_s[chars] = 0

        # create dict for t
       for chars in t:
            if chars in hashmap_t:
               hashmap_t[chars] += 1
            else:
               hashmap_t[chars] = 0
        
        # compare the dicts
       if hashmap_s == hashmap_t:
            return True
       else:
            return False
