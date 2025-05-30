class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if(len(B) < len(A)):
            A, B = B, A

        l, r = 0, len(A) - 1
        while(True):
            i = (l + r) // 2
            j = half - (i + 1) - 1 # (i + 1) because we need the parition 'size' of A, and the -1 at the end because after we get the partition size for B, which is 'j', we need the index of the partition size, hence -1

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            if(Aleft <= Bright and Bleft <= Aright):
                if(total % 2):
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 
            elif(Aleft > Bright):
                r = i - 1
            else:
                l = i + 1