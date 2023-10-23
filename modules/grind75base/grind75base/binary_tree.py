class TreeNode:
    def __init__(self, x=None, left=None, right=None):
        self.value = x
        self.left = left
        self.right = right


def build_binary_tree(node: TreeNode = TreeNode(), level: int = 1, order: int = 0, data: list = []):
    value_pos = _cal_level_pos(level=level)

    # dieu kien de break recursive
    if len(data) <= value_pos - 1 + order:
        return None

    node.value = data[value_pos - 1 + order]

    if node.value is None:
        return None

    node.left = build_binary_tree(
        node=TreeNode(), level=level + 1, order=order * 2, data=data
    )

    node.right = build_binary_tree(
        node=TreeNode(), level=level + 1, order=order * 2 + 1, data=data
    )

    return node


# mình không nghĩ được luôn công thức tổng quát của 2**0 + 2**1 + 2**2 + ... + 2**n nên sẽ viết hàm nhờ máy giải
# Trả về pos của phần tử đầu tiên của level, phần tử có order bằng 0
def _cal_level_pos(level: int):
    pos = 1

    for i in range(1, level):
        pos += 2 ** (i - 1)

    return pos
