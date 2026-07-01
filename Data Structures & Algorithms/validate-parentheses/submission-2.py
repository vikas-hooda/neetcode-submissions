class Solution:
    def isValid(self, s: str) -> bool:
        hm={
            '}':'{',
            ')':'(',
            ']':'['
        }
        st=[]
        for c in s:
            if c not in hm:
                st.append(c)
            else:
                if not st or st[-1]!=hm[c]:
                    return False
                st.pop()
        return True if not st else False