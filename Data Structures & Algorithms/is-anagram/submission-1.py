class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d={}
        t_d={}
        if len(s) ==  len(t):
            for char in s:
                if char in s_d:
                    s_d[char] = s_d[char]+1
                else:
                    s_d[char] = 1
            for char in t:
                if char in t_d:
                    t_d[char] = t_d[char]+1
                else:
                    t_d[char] = 1
            return (s_d == t_d)
        return False
            
            

            
        