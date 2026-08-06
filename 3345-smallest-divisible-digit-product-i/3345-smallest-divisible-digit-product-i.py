class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_product(num: int) -> int:
            prod = 1
            temp = num
            while temp > 0:
                prod *= temp % 10
                temp //= 10
            return prod

        for i in range(n, n + 10):
            if get_product(i) % t == 0:
                return i