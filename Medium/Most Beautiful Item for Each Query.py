# Most Beautiful Item for Each Query
# O(n log n), O(n)
def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    memo = defaultdict(int)
    for price, beauty in items:
        if price in memo:
            memo[price] = max(memo[price], beauty)
        else:
            memo[price] = beauty
    arr = []
    for price, beauty in memo.items():
        arr.append((price, beauty))
    arr.sort()
    for i in range(len(arr)):
        if i > 0:
            curr_price, curr_beauty = arr[i]
            prev_price, prev_beauty = arr[i-1]
            arr[i] = (curr_price, max(curr_beauty, prev_beauty))
    arr.insert(0, (0,0))

    res = []
    for q in queries:
        l, r = 0, len(arr)-1
        max_b = 0
        while l<=r:
            mid = l+((r-l)>>1)

            if arr[mid][0] <= q:
                max_b = max(max_b, arr[mid][1])
                l = mid+1
            else:
                r = mid-1
        res.append(max_b)
    return res

# O(n log n), O(n)
def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    res = [0] * len(queries)
    queries_with_indices = [(queries[i], i) for i in range(len(queries))]
    items.sort()
    queries_with_indices.sort()

    item_index = 0
    curr_max = 0
    for i in range(len(queries)):
        origin_i = queries_with_indices[i][1]
        q = queries_with_indices[i][0]
        while item_index < len(items) and items[item_index][0] <= q:
            curr_max = max(curr_max, items[item_index][1])
            item_index += 1
        res[origin_i] = curr_max
    return res