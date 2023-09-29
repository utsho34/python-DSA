def merge(nums1, m, nums2, n):
    pointer = len(nums1) - 1
    m = m - 1
    n = n-1
    while m>= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[pointer] = nums1[m]
            m -= 1
        else:
            nums1[pointer] = nums2[n]
            n -= 1
        pointer -= 1

    if n >= 0:
        nums1[: n+1] = nums2[: n+1]
    return nums1


nums1 = [3, 4, 6, 0, 0]
m = 3
nums2 = [1, 5]
n = 2
print(merge(nums1, m, nums2, n))
