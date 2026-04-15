class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_list = list(s)
        t_list = list(t)

        s_list = sorted(s_list)
        t_list = sorted(t_list)

        for i in range(0, len(s)):
            if s_list[i] != t_list[i]:
                return False

        return True

        return False
        
