#%%
from typing import List

def removeDuplicates(nums:List[int])->int:
    if not nums:
        return 0
    else:
        n=len(nums)
        slow=fast=1
        while fast<n:
            if nums[fast]!=nums[fast-1]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow
removeDuplicates([1,2,3,3,3,4])

