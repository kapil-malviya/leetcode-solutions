class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # empty list to storeresult
        result = []
        # initialse pointer for iterating through the intervals
        i = 0
        # total no. of intervals 
        n = len(intervals)
        
        # add interval that end before newintervalstart
        while i < n and intervals[i][1] < newInterval[0] :
            # append intervals that don't overlap with newInterval
            result.append(intervals[i])
            i = i + 1
            
        # merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1] :
            # update newInterval to merge with overlapping interval
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i = i + 1
            
        # aadd merged newinterval to result
        result.append(newInterval)
        
        # add any remaining intervals that start after newInterval
        while i < n :
            result.append(intervals[i])
            i = i + 1
            
        return result