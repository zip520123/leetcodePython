# Top K Frequent Elements
# O(n log n), O(n) space
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    dict = collections.defaultdict(int)
    for n in nums:
        dict[n] += 1
    arr = [key for _,key in enumerate(dict)]
    return sorted(arr, key=lambda key: dict[key], reverse = True)[0:k]