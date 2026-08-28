from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        odd = [c for c, cnt in counts.items() if cnt % 2 == 1]
        if len(odd) > 1:
            return ""
        mid = odd[0] if odd else ""
        half_counts = {c: cnt // 2 for c, cnt in counts.items() if cnt // 2 > 0}
        half_len = len(s) // 2
        res = []
        def dfs(idx, is_greater, counts_map):
            if idx == half_len:
                full = "".join(res) + mid + "".join(reversed(res))
                return full if (is_greater or full > target) else None
            chars = sorted(counts_map.keys())
            for c in chars:
                if counts_map[c] == 0:
                    continue
                if not is_greater and idx < len(target) and c < target[idx]:
                    continue
                next_greater = is_greater or (idx < len(target) and c > target[idx])
                counts_map[c] -= 1
                res.append(c)
                val = dfs(idx + 1, next_greater, counts_map)
                if val:
                    return val
                res.pop()
                counts_map[c] += 1
            return None
        ans = dfs(0, False, half_counts)
        return ans if ans else ""
