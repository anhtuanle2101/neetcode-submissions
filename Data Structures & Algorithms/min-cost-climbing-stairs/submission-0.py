class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[0]
        two = cost[1]

        for i in range(2, len(cost)):
            nxt = min(one, two) + cost[i]
            one = two
            two = nxt
        
        return min(one, two)