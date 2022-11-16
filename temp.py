
def traverse(node):
    if(node.left):
        traverse(node.left)
    data.push(node.value)
    if(node.right):
        traverse(node.right)