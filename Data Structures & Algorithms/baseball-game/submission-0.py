class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for p in operations:
            if p=='+':
                st.append(st[-1]+st[-2])
            elif p=='C':
                st.pop()
            elif p=='D':
                st.append(2*st[-1])
            else:
                st.append(int(p))
        return sum(st)