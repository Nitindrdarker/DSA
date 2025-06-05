# You are given two strings of the same length s1 and s2 and a string baseStr.

# We say s1[i] and s2[i] are equivalent characters.

# For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:

# Reflexivity: 'a' == 'a'.
# Symmetry: 'a' == 'b' implies 'b' == 'a'.
# Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
# For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        def find(x):
            while(x != parent[x]):
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ap = find(a)
            bp = find(b)


            if ap == bp:
                return 
            if ap > bp:
                parent[ap] = bp
            else:
                parent[bp] = ap

            return


        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        res = []
        for c in baseStr:
            par = find(ord(c) - ord('a'))
            res.append(chr(ord('a') + par))
        return ''.join(res)
            
            
            