class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1=collections.Counter(ransomNote)
        c2=collections.Counter(magazine)
        return all(c1[c]<=c2[c] for c in string.ascii_lowercase)