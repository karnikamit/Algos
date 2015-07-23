__author__ = 'karnikamit'


def pentagonal(n):
    return (n*(3*n-1))/2

nums = [pentagonal(i) for i in xrange(3, 100)]
nums1 = nums
for i in xrange(3, 10):
    d = nums1[i-3]-nums[i-3]
    print d
    s = nums1[i-3]+nums[i-3]
    print s
    if d == s:
        print nums[i]
# for n in nums:
#     for m in nums1:
#         s = n + m
#         d = abs(n-m)
#         if s == d:
#             print 'here'
#             print n, m