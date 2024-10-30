def getMaxEquals(arr1, arr2) -> int:
    neg_arr = []
    pos_arr = []

    for i in range(len(arr1)):
        curr = arr1[i] - arr2[i]
        if curr < 0:
            neg_arr.append(i)
        if curr > 0:
            pos_arr.append(i)
    if len(neg_arr) == 0 or len(pos_arr) == 0:
        return 0
    neg_abs = abs(sum(arr1[i]-arr2[i] for i in neg_arr))
    pos_abs = sum(arr1[i]-arr2[i] for i in pos_arr)
    res = min(pos_abs, neg_abs)
    for i in neg_arr:
        for j in pos_arr:
            curr_abs = abs(arr1[i]-arr2[i]) + arr1[j]-arr2[j]
            if abs(arr1[i]-arr2[j]) + abs(arr1[j]-arr2[i]) < curr_abs:
                arr1[i], arr1[j] = arr1[j], arr1[i]
                res = min(res, 1 + getMaxEquals(arr1, arr2))
                arr1[i], arr1[j] = arr1[j], arr1[i]
    return res



assert getMaxEquals([2,4,1], [1,2,3]) == 2

assert getMaxEquals([100, 10, 100], [99,  9,  99]) == 0
   
assert getMaxEquals([10,100, 100], [99,  9,  99]) == 1

assert getMaxEquals([1, 1, 1], [1,  1,  1]) == 0

assert getMaxEquals([1, 100, 80], [1,  1,  100]) == 1

