n = int(input())

tree = {}

def pre_tree(node):
    global preorder
    if node != '.':
        preorder += node
        pre_tree(tree[node][0])
        pre_tree(tree[node][1])

def in_tree(node):
    global inorder
    if node != '.':
        in_tree(tree[node][0])
        inorder += node
        in_tree(tree[node][1])

def post_tree(node):
    global postorder
    if node != '.':
        post_tree(tree[node][0])
        post_tree(tree[node][1])
        postorder += node

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위 순회
preorder = ''
pre_tree('A')
# 중위 순회
inorder = ''
in_tree('A')
# 후위 순회
postorder = ''
post_tree('A')

print(preorder)
print(inorder)
print(postorder)