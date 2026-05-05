class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        def value_greater_than_2(counter_dict: dict[int, int]):
            return any(value>=2 for value in counter_dict.values())
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if duplicated:=value_greater_than_2(counter):
                return duplicated
        return False
