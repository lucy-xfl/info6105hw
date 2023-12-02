# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #leetocde111
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        min_depth = 0
        nodes = [root]
        while nodes:
            sz = len(nodes)
            min_depth += 1
            while sz > 0:
                now = nodes.pop(0)
                if now.left is None and now.right is None:
                    return min_depth
                elif now.left is None:
                    nodes.append(now.right)
                elif now.right is None:
                    nodes.append(now.left)
                else:
                    nodes.append(now.right)
                    nodes.append(now.left)
                sz -= 1
        return min_depth

    #leetcode222
    def countNodes(self, root) -> int:
        if root is None:
            return 0
        queue = [root]
        ans = 0
        while len(queue) > 0:
            ans += 1
            temp = queue.pop(0)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
        return ans

    #leetcode515
    def largestValues(self, root):
        ans = []
        if root is None:
            return ans
        que = [root]
        while len(que) > 0:
            len_layer = len(que)
            max_layer = que[0].val
            while len_layer > 0:
                len_layer -= 1
                temp = que.pop(0)
                max_layer = max(max_layer, temp.val)
                if temp.left is not None:
                    que.append(temp.left)
                if temp.right is not None:
                    que.append(temp.right)
            ans.append(max_layer)
        return ans

    #leetcode872
    def leafSimilar(self, root1, root2) -> bool:
        leaves1 = self.finding_leaves(root1)
        leaves2 = self.finding_leaves(root2)
        return leaves1 == leaves2

    def finding_leaves(self, root) -> list[int]:
        if root is None:
            return []
        if root.right is None and root.left is None:
            return [root.val]
        ans = []
        if root.right is not None:
            ans += self.finding_leaves(root.right)
        if root.left is not None:
            ans += self.finding_leaves(root.left)
        return ans

    #leetcode1302
    def deepestLeavesSum(self, root) -> int:
        ans = 0
        if root is None:
            return ans
        queue = [root]
        while len(queue) > 0:
            ans = 0
            len_layer = len(queue)
            while len_layer > 0:
                len_layer -= 1
                temp = queue.pop(0)
                ans += temp.val
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
        return ans

    #added question
    def findLeaves(self, root):
        ans = [[]]
        def dfs(u):
            if u == None:
                return -1
            leftLevel = dfs(u.left)
            rightLevel = dfs(u.right)
            currentLevel = (max(leftLevel, rightLevel)+1)
            while len(ans) <= currentLevel:
                ans.append([])
            ans[currentLevel].append(u.val)
            return currentLevel
        dfs(root)
        return ans




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Solution.get_all_leaves())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
