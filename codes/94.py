from types import Optional, List
from dsTypes.tree import TreeNode

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root == None:
        return []
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)