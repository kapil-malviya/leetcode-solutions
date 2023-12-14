class Solution:
    
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

    def maxProduct(self, nums: List[int]) -> int:
        self.insertion_sort(nums)

        # calculate maximum product using last two elements
        return (nums[-1] - 1) * (nums[-2] - 1)