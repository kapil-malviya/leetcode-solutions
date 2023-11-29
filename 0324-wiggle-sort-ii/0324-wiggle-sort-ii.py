class Solution:
    
    def merge_sort(self, arr):
        
        if len(arr) <= 1:
            return arr  

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # recursively sort left and right halves
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge_two_sorted_lists(left, right)

    def merge_two_sorted_lists(self, a, b):
        # merge two sorted lists into a single sorted list
        
        len_a = len(a)
        len_b = len(b)
        
        i = j = 0

        merged = []

        # merge elements from a and b in sorted order
        while i < len_a and j < len_b:

            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1

        # append remaining elements from a and b
        merged.extend(a[i:])
        merged.extend(b[j:])

        return merged

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Perform wiggle sort on the input array in-place.
        """
        # sorting array using merge sort
        sorted_nums = self.merge_sort(nums)
        
        # finding middle index
        mid = (len(sorted_nums) - 1) // 2
        
        # rearranging elements for wiggle sort
        nums[::2], nums[1::2] = sorted_nums[mid::-1], sorted_nums[:mid:-1]
