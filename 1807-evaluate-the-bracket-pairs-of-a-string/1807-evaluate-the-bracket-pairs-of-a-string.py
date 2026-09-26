class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = {key: value for key, value in knowledge}
        res = []
        i = n = len(s)
        j = 0
        while j < n:
            if s[j] == '(':
                end = s.find(')', j)
                key = s[j + 1:end]
                res.append(mapping.get(key, '?'))
                j = end + 1
            else:
                res.append(s[j])
                j += 1
                
        return "".join(res)
