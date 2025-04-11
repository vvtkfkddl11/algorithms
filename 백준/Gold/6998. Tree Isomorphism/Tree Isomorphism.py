import sys
from collections import defaultdict


def solve():
    def build_tree(tokens):
        tree = defaultdict(list)
        
        def parse(idx):
            if idx >= len(tokens) or tokens[idx] == '#':
                return None, idx + 1
            
            node = tokens[idx]
            idx += 1
            
            while idx < len(tokens) and tokens[idx] != '#':
                child, idx = parse(idx)
                if child:
                    tree[node].append(child)
            
            return node, idx + 1
        
        root, _ = parse(0)
        return tree, root
    
    def compute_canonical_form(tree, node, memo=None):
        if memo is None:
            memo = {}
            
        if node not in tree or not tree[node]:
            return "0"
        
        if node in memo:
            return memo[node]
        
        subtrees = []
        for child in tree[node]:
            subtree_form = compute_canonical_form(tree, child, memo)
            subtrees.append(subtree_form)
        
        subtrees.sort()
        
        result = "1(" + ",".join(subtrees) + ")"
        memo[node] = result
        return result
    
    def are_isomorphic(tree1, root1, tree2, root2):
        return compute_canonical_form(tree1, root1) == compute_canonical_form(tree2, root2)
    
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        tree1_tokens = sys.stdin.readline().split()
        tree2_tokens = sys.stdin.readline().split()
        
        tree1, root1 = build_tree(tree1_tokens)
        tree2, root2 = build_tree(tree2_tokens)
        
        if are_isomorphic(tree1, root1, tree2, root2):
            print("The two trees are isomorphic.")
        else:
            print("The two trees are not isomorphic.")

solve()