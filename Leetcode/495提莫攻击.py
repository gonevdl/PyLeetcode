class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        ret = 0
        if not timeSeries:
            return 0
        for i in range(0, len(timeSeries) - 1):
            if timeSeries[i] + duration - 1 <= timeSeries[i + 1]:
                ret += duration
            else:
                ret += timeSeries[i + 1] - timeSeries[i]
        ret += duration
        return ret

print(Solution().findPoisonedDuration([1, 2], 2))