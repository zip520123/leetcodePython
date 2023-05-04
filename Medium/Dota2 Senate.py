#Dota2 Senate
#O(n^2), O(n)
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d=0; r=0
        for char in senate:
            if char == "D":
                d += 1
            if char == "R":
                r += 1
        arr = list(senate)
        while not (d==0 or r==0):
            i=0
            while i<len(arr):
                char = arr[i]
                found = False
                if char == "R":
                    j=i+1
                    while j<len(arr):
                        if arr[j] == "D":
                            arr.pop(j)
                            i += 1
                            d -= 1
                            found = True
                            break 
                        j+=1
                    
                    if found == False:
                        j=0
                        while j<i:
                            if arr[j] == "D":
                                arr.pop(j)
                                d -= 1
                                break
                            j += 1
                else:
                    j=i+1
                    while j<len(arr):
                        if arr[j] == "R":
                            arr.pop(j)
                            i += 1
                            r -= 1
                            found = True
                            break
                        j+=1
                    if found == False:
                        j=0
                        while j<i:
                            if arr[j] == "R":
                                arr.pop(j)
                                r -= 1
                                break
                            j += 1
                if found == False:
                    i += 1
        if d>r:
            return "Dire"
        return "Radiant"