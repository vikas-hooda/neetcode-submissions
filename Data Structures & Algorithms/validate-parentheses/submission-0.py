class Solution:
    def isValid(self, s: str) -> bool:
        m={
            ')': '(',
            '}': '{',
            ']': '['
        }
        st=[]
        for c in s:
            if c in '({[':
                st.append(c)
            else:
                if not st or not st[-1]==m[c]:
                    return False
                st.pop()
        return True if not st else False