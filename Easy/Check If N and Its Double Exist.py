# Check If N and Its Double Exist
# O(n^2), O(n)
def checkIfExist(self, arr: List[int]) -> bool:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j] * 2:
                return True
    return False
