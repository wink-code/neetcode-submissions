class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        def value_greater_than_2(counter: dict[int, int])->bool:
            if any(value >= 2 for value in counter.values()):
                return True
            return False
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            if dumplicated := value_greater_than_2(num_dict):
                return dumplicated
        return False
            
