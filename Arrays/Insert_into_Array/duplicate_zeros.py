"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""

#Solution
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros_to_duplicate = 0
    
        # Count the number of zeros to determine shifting positions
        for num in arr:
            if num == 0:
                zeros_to_duplicate += 1
        
        print(zeros_to_duplicate)

        n = len(arr)
        i = n - 1
        j = n + zeros_to_duplicate - 1

        # Perform shifting and duplicating in reverse order
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            j -= 1

            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1
            i -= 1