class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def remove(self, value, parent_node=None):
        current_node = self
        while current_node is not None:
            # value is less than the current node's value look left
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            # value is greater than the current node's value, look right
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            # found node to remove
            else:
                # check if it has to children nodes
                if current_node.left is not None and current_node.right is \
                        not None:
                    # smallest value of right subtree
                    current_node.value = current_node.right.get_min_value()
                    # remove the smallest value of right subtree since it is
                    #   replacing the original node that we are removing
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        # This is a single node tree, do nothing
                        pass
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left \
                        is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if \
                        current_node.left is not None else current_node.right
                break
        return self