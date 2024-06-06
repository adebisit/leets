from typing import Optional
from dsTypes.tree import TreeNode

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))