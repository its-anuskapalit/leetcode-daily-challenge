class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t=s.split()
        return [*map(pattern.index,pattern)]== [*map(t.index,t)]