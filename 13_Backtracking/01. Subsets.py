# https://leetcode.com/problems/subsets/

# -------------------------------------------- Method 1 ---------------------------------------------------------
# DFS => Without taking subset as Global variable        
class Solution:
    def subsets(self, nums):        
        res = []
        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset)
                return    # to stop this call here so this will not call another 2 dfs
            dfs(i+1, subset + [nums[i]])  # calling dfs Including nums[i] in subset
            # as every subset is using different subset array so we don't need to pop
            dfs(i+1, subset)     # calling dfs Excluding nums[i] in subset
        
        dfs(0, [])
        return res


# -------------------------------------------- Method 2 ---------------------------------------------------------
# DFS => Taking subset as a Global variable
class Solution:
    def subsets(self, nums):
        # https://youtu.be/REOH22Xwdkk
        res = []
        subset = []  # Global variable to use in all dfs calls
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())  # appending a copy of original global subset 
                return  # to stop this call here so this will not call another 2 dfs
            subset.append(nums[i]) # include nums[i]
            dfs(i+1)  # calling dfs Including nums[i] in subset
            subset.pop() # removing nums[i] as we will use subset to call dfs without including nums[i]
            dfs(i+1) # calling dfs Excluding nums[i] in subset
        
        dfs(0)
        return res
    

# -------------------------------------------- Method 3 ---------------------------------------------------------
# BFS
class Solution:
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            res += [r + [n] for r in res]
        return res

