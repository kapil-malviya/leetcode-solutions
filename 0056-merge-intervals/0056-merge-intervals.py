class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def sort_by_start(interval):
            return interval[0]
        
        if not intervals:
            return []
        
        intervals.sort(key=sort_by_start)
        
        merged_intervals = [intervals[0]]
        
        for current_interval in intervals[1:] :
            previous_interval = merged_intervals[-1]
            
            if current_interval[0] <= previous_interval[1] :
                previous_interval[1] = max(previous_interval[1], current_interval[1])
                
            else :
                merged_intervals.append(current_interval)
                
        return merged_intervals