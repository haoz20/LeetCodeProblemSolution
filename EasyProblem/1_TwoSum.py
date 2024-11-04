class Hash_Map():
    def __init__(self, size):
        self.size = size
        self.hash = [[] for _ in range(size)]

    def _hash_function(self, key):
        # Modulus operation to determine bucket index
        return key % self.size

    def put(self, key, value):
        index = self._hash_function(key)
        # Store as (key, value) pair in appropriate bucket
        self.hash[index].append((key, value))

    def contains_key(self, key):
        index = self._hash_function(key)
        for k, v in self.hash[index]:
            if k == key:
                return True
        return False

    def get(self, key):
        index = self._hash_function(key)
        for k, v in self.hash[index]:
            if k == key:
                return v
        return None


class Solution(object):
    def twoSum(self, nums, target):
        n = Hash_Map(len(nums))
        for i in range(len(nums)):
            cur = nums[i]
            #target = cur + x
            x = target - cur
            if n.contains_key(x):
                return [n.get(x), i]
            n.put(cur, i)
        return None
