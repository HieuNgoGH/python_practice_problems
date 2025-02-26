"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in
non-decreasing order.The final sorted array should not be returned by the function, but instead be stored inside the
array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n."""


def merge(nums1, m, nums2, n):

    # eliminate any trailing 0's in array nums1
    counter = len(nums1) - 1
    while counter >= m:
        if nums1[counter] == 0:
            nums1.pop()
            counter -= 1
        else:
            counter = -1

    # add the elements from the nums2 list into nums1 using the length of nums2 as the counter limit
    counter = 0
    while counter < n:
        nums1.append(nums2[counter])
        counter += 1

    # sort the array by starting at first index loop and with second loop scan the following indexes
    # if number is lower move the second counter, else swap the numbers
    counter1 = 0
    counter2 = 0
    while counter1 < (m + n) - 1:
        while counter2 < m + n:
            if nums1[counter1] <= nums1[counter2]:
                counter2 += 1
            elif nums1[counter1] > nums1[counter2]:
                temp = nums1[counter1]
                nums1[counter1] = nums1[counter2]
                nums1[counter2] = temp
                counter2 += 1
        counter1 += 1
        counter2 = counter1 + 1




















