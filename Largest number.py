class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #changing the array into string
        nums = [str(num) for num in nums]
        #comparison function
        def compare(n1,n2):
            if n1+n2 >n2+n1:
                return -1
            else:
                return 1
# nums,key=cmp_to_key(compare) is used to specify the compare function is used as #a key in sorted function  
        nums = sorted(nums,key=cmp_to_key(compare))
        return str(int("".join(nums)))
    
