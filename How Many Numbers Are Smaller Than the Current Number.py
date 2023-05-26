class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #finding the number of elements that are smaller than the given element in the array.
        bucket = []
        #iterates through nums array
        for i in range(len(nums)):
            #appends 0 for each elements in the list
            bucket.append(0)
        
        # the outer loop is to select specific elements in the array nums
        for i in range(len(nums)):
            #to compare the current element with every other elements
            for j in range(len(nums)):
                #compare the current element nums[j] with current element nums[i]
                if nums[j] < nums[i]:
                    #increment it when we find smaller element than nums[i]
                    bucket[i] += 1
        
        return bucket
