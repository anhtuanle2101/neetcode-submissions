class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window 
        # monotonic decreasing queue
        dq = deque()
        results = []
        l, r = 0, 0
        while r < len(nums):
            if r - l + 1 < k:
                while dq and nums[r] >= nums[dq[-1]]:
                    dq.pop()
                dq.append(r)
                r += 1
                continue

            while dq and nums[r] >= nums[dq[-1]]:
                dq.pop()
            dq.append(r)
        
            if l > dq[0]:
                dq.popleft()

            results.append(nums[dq[0]])
            l += 1 
            r += 1
        
        return results


