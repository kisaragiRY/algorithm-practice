#%%
# 414. 第三大的数
from typing import List
def thirdMax(nums:List[int])->int:
    a,b,c=float('-inf'),float('-inf'),float('-inf')
    for num in nums:
        if num>a :
            a,b,c=num,a,b
        elif a>num>b:
            b,c =num,b
        elif b>num>c:
            c=num
    return a if c == float('inf') else c

def thirdMax1(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b,c=float('inf'),float('inf'),float('inf')
        for num in nums:
            if num>a:
                a,b,c=num,a,b
            elif a>num>b:
                b,c=num,b
            elif b>num>c:
                c=num
        return a if c==float('inf') else c

thirdMax1([3,2,1])

#%%
# 数组的遍历
# 495. 提莫攻击
from typing import List

def findPositionDuration(timeseries:List[int],duaration:int)->int:
    sober=ans=0
    for i in range(len(timeseries)):
        if timeseries[i]>=sober:
            ans+=duaration
        else:
            ans+=timeseries[i]-sober+duaration
        sober=timeseries[i]+duaration
    
    return ans

timeseries=[1,4]
duation=2
findPositionDuration(timeseries,duation)

#%%
# 数组的遍历
# 485. 最大连续 1 的个数
from typing import List

def consecutive1(nums:List[int])->int:
    maxcount=count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else: 
            maxcount=max(maxcount,count)
            count=0
    maxcount=max(maxcount,count)
    return maxcount

def consecutive2(nums:List[int])->int:
    k1=k2=0
    for i in range(len(nums)):
        if nums[i]==1:
            k1+=1
        else: 
            if k1>k2 :
                k2=k1
                k1=0
            k1=0
    if k1>k2 :k2=k1
    return k2

l=[1,1,1,1,0,1,1,0,1,1,1,1,1]
consecutive2(l)

#%%
'''
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
'''
from typing import List
def twosum(nums:List[int],target:int)->List[int]:
    hashtable=dict()
    for id,num in enumerate(nums):
        if target-num in hashtable:
            return [hashtable[target-num],id]
        else:
            hashtable[num]=id
    return []
twosum([2,3,4,5],8)
#%%
'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''
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

#%%
'''
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
'''
from typing import List
def maxProfit(prices:List[int])->int:
    profit=0
    for i in range(1,len(prices)):
        tem=prices[i]-prices[i-1]
        if tem>0:profit+=tem
    return profit
maxProfit([3,4,2,4,5])

#%%
