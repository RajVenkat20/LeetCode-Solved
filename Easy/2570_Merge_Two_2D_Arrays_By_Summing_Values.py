class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ptr1, ptr2 = 0, 0
        res = []
        size1, size2 = len(nums1), len(nums2)

        while(ptr1 < size1 and ptr2 < size2):
            if(nums1[ptr1][0] < nums2[ptr2][0]):
                res.append(nums1[ptr1])
                ptr1 += 1
            elif(nums1[ptr1][0] > nums2[ptr2][0]):
                res.append(nums2[ptr2])
                ptr2 += 1
            else:
                total = nums1[ptr1][1] + nums2[ptr2][1]
                idx = nums1[ptr1][0]
                res.append([idx, total])
                ptr1 += 1
                ptr2 += 1

        while(ptr1 < size1):
            res.append(nums1[ptr1])
            ptr1 += 1
        
        while(ptr2 < size2):
            res.append(nums2[ptr2])
            ptr2 += 1

        return res