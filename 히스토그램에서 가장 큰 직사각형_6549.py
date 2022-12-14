import sys

tree = [0] * 100000
l = [2, 1, 4, 5, 2, 4, 2, 3]


def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = min(init(node * 2, start, (start + end) // 2), init(node * 2 + 1, (start + end) // 2 + 1, end))
        return tree[node]


init(1, 0, len(l)-1)
print(tree[:16])


heights = [1, 2, 3, 4, 5]
