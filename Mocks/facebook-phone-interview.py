'''
Mock Phone Interviews of Facebook on LeetCode
'''


class Tribonacci:
    '''
    https://leetcode.com/problems/n-th-tribonacci-number/
    '''

    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        # return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

        t0, t1, t2 = 0, 1, 1

        for _ in range(n-2):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2


class VerifyingAnAlienDictionary:
    '''
    https://leetcode.com/problems/verifying-an-alien-dictionary/
    '''

    def isAlienSorted(self, words, order):
        order_dict = {c: i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            if self._isGreater(words[i-1], words[i], order_dict):
                return False

        return True

    def _isGreater(self, word1, word2, order_dict):
        for c1, c2 in zip(word1, word2):
            if order_dict[c1] < order_dict[c2]:
                return False
            if order_dict[c1] > order_dict[c2]:
                return True

        return len(word1) > len(word2)


class IntersectionArrays:
    '''
    https://leetcode.com/problems/intersection-of-two-arrays/
    '''

    def intersection(self, nums1, nums2):
        return set(nums1).intersection(set(nums2))

    def intersectionSorted(self, nums1, nums2):
        # nums1.sort()
        # nums2.sort()

        i, j = 0, 0

        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                num = nums1[i]
                result.append(num)
                while(i < len(nums1) and nums1[i] == num):
                    i += 1
                while(j < len(nums2) and nums2[j] == num):
                    j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return result


class SparseVector:
    '''
    https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
    '''

    def __init__(self, nums):
        self.data = {i: n for i, n in enumerate(nums) if n != 0}

    def dotProduct(self, vec) -> int:
        data1 = self.data
        data2 = vec.data

        if len(data1) > len(data2):
            data1, data2 = data2, data1

        result = 0

        for i, n in data1.items():
            if i in data2:
                result += n * data2[i]

        return result


class BinaryTreeRightSideView:
    from collections import deque

    '''
    https://leetcode.com/problems/binary-tree-right-side-view/
    Definition for a binary tree node.
     class TreeNode:
         def __init__(self, val=0, left=None, right=None):
             self.val = val
             self.left = left
             self.right = right
    '''

    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = deque()
        queue.append((0, root))

        curr_level = 0
        curr_right = None

        while queue:
            level, node = queue.popleft()

            if level > curr_level:
                curr_level = level
                result.append(curr_right)

            if node:
                curr_right = node.val
                queue.append((level+1, node.left))
                queue.append((level+1, node.right))

        return result


class PermutationInString:
    '''
    https://leetcode.com/problems/permutation-in-string/
    '''

    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False

        s1_counter = self._buildCounter(s1)
        s2_counter = self._buildCounter(s2[0:len(s1)])

        for i in range(len(s2)-len(s1)):
            if s1_counter == s2_counter:
                return True
            else:
                pre_char = s2[i]
                if s2_counter[pre_char] == 1:
                    del s2_counter[pre_char]
                else:
                    s2_counter[pre_char] -= 1

                next_char = s2[i+len(s1)]
                if next_char in s2_counter:
                    s2_counter[next_char] += 1
                else:
                    s2_counter[next_char] = 1

        return s1_counter == s2_counter

    def _buildCounter(self, s):
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        return counter
