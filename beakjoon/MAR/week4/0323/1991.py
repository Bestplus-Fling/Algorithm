import sys
sys.stdin = open("1991.txt")
from collections import defaultdict


class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


def preorder(n):
    r = ''
    if t[n] is not None:
        r += t[n].item
    if t[n].left:
        r += preorder(t[n].left)
    if t[n].right:
        r += preorder(t[n].right)
    return r


def inorder(n):
    r = ''
    if t[n].left:
        r += inorder(t[n].left)
    if t[n] is not None:
        r += t[n].item
    if t[n].right:
        r += inorder(t[n].right)
    return r


def postorder(n):
    r = ''
    if t[n].left:
        r += postorder(t[n].left)
    if t[n].right:
        r += postorder(t[n].right)
    if t[n] is not None:
        r += t[n].item
    return r


N = int(input())
t = defaultdict(str)
for i in range(N):
    p, l, r = input().split()
    t[p] = p
    t[p] = Node(p)
    if l != '.':
        t[p].left = l
    if r != '.':
        t[p].right = r


print(preorder('A'))
print(inorder('A'))
print(postorder('A'))

