class Solution:
    def select(self, arr, i):
        for i in range(0, len(arr) - 1):
            curMin = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[curMin]:
                    curMin = j
            if curMin != i:
                arr[i], arr[curMin] = arr[curMin], arr[i]
        return arr
    
    def selectionSort(self, arr, n):
        return self.select(arr, 0)
