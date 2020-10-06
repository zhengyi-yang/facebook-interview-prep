'''
Mock Phone Interviews of Facebook on LeetCode
'''

# Easy


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


class Palindrome:
    '''
    https: // leetcode.com/problems/valid-palindrome/
    '''

    def isPalindrome(self, s):
        s = ''.join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]


class Palindrome2:
    '''
    https://leetcode.com/problems/valid-palindrome-ii/
    '''

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]

        return True


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


class MoveZeroes:
    '''
    https://leetcode.com/problems/move-zeroes/
    '''

    def moveZeroes(self, nums):
        '''
        Do not return anything, modify nums in-place instead.
        '''
        zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1


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


class IntersectionArrays2:
    '''
    https://leetcode.com/problems/intersection-of-two-arrays-ii/
    '''
    from collections import Counter

    def intersect(self, nums1, nums2):
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)
        result = []

        if len(nums1_counter) > len(nums2_counter):
            nums1_counter, nums2_counter = nums2_counter, nums1_counter

        for num, count in nums1_counter.items():
            if num in nums2_counter:
                min_count = min(count, nums2_counter[num])
                result.extend([num] * min_count)

        return result

# Medium


class BulbSwitch:
    '''
    https://leetcode.com/problems/bulb-switcher/
    '''

    def bulbSwitch(self, n):
        return int(n**0.5)


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


class PermutationInString:
    '''
    https://leetcode.com/problems/permutation-in-string/
    '''
    from collections import Counter

    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[0:len(s1)])

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


class VerticalOrderTraversal:
    '''
    https://leetcode.com/problems/binary-tree-vertical-order-traversal/
    Definition for a binary tree node.
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    '''
    from collections import deque

    def verticalOrder(self, root):
        if not root:
            return []

        cols = {}
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, col = queue.popleft()
            if col in cols:
                cols[col].append(node.val)
            else:
                cols[col] = [node.val]

            if node.left:
                queue.append((node.left, col-1))

            if node.right:
                queue.append((node.right, col+1))

        return [l for _, l in sorted(cols.items())]


class BinaryTreeRightSideView:
    '''
    https://leetcode.com/problems/binary-tree-right-side-view/
    Definition for a binary tree node.
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    '''
    from collections import deque

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


class SmallestSubtreeAllDeepestNodes:
    '''
    https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
    Definition for a binary tree node.
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    '''

    def subtreeWithAllDeepest(self, root):
        def dfs(node, depth):
            if not node:
                return None, 0

            if not node.left and not node.right:
                return node, depth

            lnode, ldep = dfs(node.left, depth+1)
            rnode, rdep = dfs(node.right, depth+1)

            if ldep == rdep:
                return (node, ldep)
            elif ldep > rdep:
                return (lnode, ldep)
            else:
                return (rnode, rdep)

        node, _ = dfs(root, 0)
        return node


class SubarraySumEqualsK:
    '''
    https://leetcode.com/problems/subarray-sum-equals-k/
    '''

    def subarraySum(self, nums, k):
        sum_map = {0: 1}
        cur_sum = 0
        count = 0

        for n in nums:
            cur_sum += n

            if cur_sum-k in sum_map:
                count += sum_map[cur_sum-k]

            if cur_sum in sum_map:
                sum_map[cur_sum] += 1
            else:
                sum_map[cur_sum] = 1

        return count

# Hard


class LongestSubstringKDistinctCharacters:
    '''
    https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
    '''

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or not k:
            return 0

        counter = {s[0]: 1}
        longest = 0
        i, j = 0, 0

        while True:
            if len(counter) <= k:
                longest = max(longest, j-i+1)
                j += 1

                if j >= len(s):
                    break
                else:
                    if s[j] in counter:
                        counter[s[j]] += 1
                    else:
                        counter[s[j]] = 1
            else:
                if counter[s[i]] == 1:
                    del counter[s[i]]
                else:
                    counter[s[i]] -= 1

                i += 1
                if i > j:
                    j = i

        return longest


class ExpressionAddOperators:
    '''
    https://leetcode.com/problems/expression-add-operators/
    '''

    def addOperators(self, num, target):
        if not num:
            return []

        result = []

        def dfs(prefix, num, target):
            if not num:
                if eval(prefix) == target:
                    result.append(prefix)
                return

            if not prefix or not prefix[-1].isnumeric():
                if num[0] == '0':
                    dfs(prefix+'0', num[1:], target)
                else:
                    for i in range(1, len(num)+1):
                        new_prefix = prefix+num[:i]
                        new_num = num[i:]
                        dfs(new_prefix, new_num, target)
            else:
                for op in ('+', '-', '*'):
                    new_prefix = prefix+op
                    dfs(new_prefix, num, target)

        dfs('', num, target)

        return result
