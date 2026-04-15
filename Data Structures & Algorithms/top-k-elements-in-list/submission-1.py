class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        print(buckets)
        freq = {}
        result = []

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        print(freq)

        for num in freq:
            buckets[freq[num]].append(num)
        print(buckets)

        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result