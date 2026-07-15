class Solution:
    def isValid(self, s: str) -> bool:

        # understand:
        # input; s= string of characters
        # output; True/ False
        # Check whether every open brackets have a closed one in the order it was opened

        # create a stack to store the open brackets
        stack = []

        # create the library to check against
        lib = {")" : "(", "]" : "[", "}" : "{"}

        # iterate through the string using the index to check for the closing brackets for every open one and check char in the library
        for char in s:
            if char in lib:

                # to check for matches in the stack against library
                if stack and stack[-1] == lib[char]:
                    # remove the pair if match found
                    stack.pop() 

                else:
                    return False

            # append new chars if they not in stack yet
            else:
                stack.append(char)

        # the lenght of the stack will be zero if the string is valid, as all the pairs are removed
        return len(stack) == 0