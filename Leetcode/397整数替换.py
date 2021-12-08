class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0

        k = 0
        while n != 1:
            n_s = bin(n)
            if n_s.count("1") == 1:
                return k + len(n_s) - 3
            if (n % 2) == 0:
                n //= 2
            else:
                n += 1
            k += 1
        return k


print(Solution().integerReplacement(1234))
