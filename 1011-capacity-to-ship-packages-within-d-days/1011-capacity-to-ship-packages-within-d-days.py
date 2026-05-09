class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Helper function to check if we can ship with given capacity
        def canShip(capacity: int) -> bool:
            days_needed = 1
            current_weight = 0
            
            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = weight
                else:
                    current_weight += weight
            
            return days_needed <= days
        
        # Binary search boundaries
        low = max(weights)       # At least the heaviest package
        high = sum(weights)      # At most all packages in one day
        
        answer = high
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if canShip(mid):
                answer = mid
                high = mid - 1   # Try smaller capacity
            else:
                low = mid + 1    # Need larger capacity
        
        return answer
