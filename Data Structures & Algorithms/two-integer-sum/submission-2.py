
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,x in enumerate(nums):
            compliment = target - x
            if compliment in seen:
                return([seen[compliment],index])
            seen[x]= index
      

        
            