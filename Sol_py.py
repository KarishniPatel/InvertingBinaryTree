def invertTree(node):
  if node is None:
    return None

  node.left, node.right = node.right, node.left

  invertTree(node.left)
  invertTree(node.right)

  return node
