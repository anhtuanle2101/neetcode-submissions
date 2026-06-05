'''
    given an integer array piles where piles[i] is the number of bananas in the ith pile

    given an integer h, which represents the number of hours you have to eat all the bananas
    
    return min banana per hour rate of k where the money can eat all the bananas within n hours
    - k: [0, max(piles)]
    - calculate the hour at k rate to eat -> for bananas in piles: total_hours += math.ceil(bananas/rate)
    - get the middle rate, if the hour values <= target hour -> valid but can eat more -> look for greater rate
    otherwise, if the hour values > target hour -> invalid, eating too much -> look for smaller rate
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            middle_rate = left + (right - left) // 2
            
            #calculate the hour to eat at middle_rate
            total_hours = 0
            for bananas in piles:
                total_hours += math.ceil(bananas/middle_rate)
            
            if total_hours <= h:
                right = middle_rate - 1
            elif total_hours > h:
                left = middle_rate + 1
    
        return left
                
