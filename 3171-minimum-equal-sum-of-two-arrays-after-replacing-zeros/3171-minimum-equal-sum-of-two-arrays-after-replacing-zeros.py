class Solution(object):
    def minSum(self, nums1, nums2):
        count2=nums2.count(0)
        count1=nums1.count(0)
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1<sum2 and count1==0:
            return -1
        if sum2<sum1 and count2==0:
            return -1
        if count2==0 and sum1+count1>sum2:
            return -1
        if count1==0 and sum2+count2>sum1:
            return -1
        final1 = sum1+count1
        final2 = sum2+count2
        if sum1==sum2:
            if count1>count2:
                final = sum1+count1
            else:
                final = sum2 +count2
            return final 
        if final1>=final2:
            return final1
        else:
            return final2