import sys
from itertools import permutations


def solve():
    # 트리 구성 함수 - 리스트 기반
    def build_tree(tokens):
        def parse(idx):
            if idx >= len(tokens) or tokens[idx] == '#':
                return [], idx + 1
            
            # 현재 노드와 그 자식들을 포함하는 트리
            tree = [tokens[idx]]  # 첫 번째 요소는 노드의 값
            children = []  # 이후 요소들은 자식 서브트리들
            idx += 1
            
            while idx < len(tokens) and tokens[idx] != '#':
                subtree, idx = parse(idx)
                if subtree:  # 빈 트리가 아니면 자식으로 추가
                    children.append(subtree)
            
            tree.append(children)  # 자식 트리들 추가
            return tree, idx + 1
        
        tree, _ = parse(0)
        return tree
    
    # 트리 동형성 검사 함수 (완전 탐색) - 리스트 기반
    def is_isomorphic(tree1, tree2):
        # 둘 다 빈 트리면 동형
        if not tree1 and not tree2:
            return True
        
        # 하나만 빈 트리면 동형이 아님
        if not tree1 or not tree2:
            return False
        
        # 트리의 구조: [노드값, [자식1, 자식2, ...]]
        children1 = tree1[1] if len(tree1) > 1 else []
        children2 = tree2[1] if len(tree2) > 1 else []
        
        # 자식 수가 다르면 동형이 아님
        if len(children1) != len(children2):
            return False
        
        # 자식이 없으면 동형
        if not children1:
            return True
        
        # 자식이 하나면 그 자식들이 동형인지 확인
        if len(children1) == 1:
            return is_isomorphic(children1[0], children2[0])
        
        # 자식이 여러 개인 경우, 모든 가능한 매핑을 시도
        for perm in permutations(range(len(children2))):
            is_matching = True
            
            for i, idx in enumerate(perm):
                if not is_isomorphic(children1[i], children2[idx]):
                    is_matching = False
                    break
                    
            if is_matching:
                return True
                
        return False
    
    # 메인 로직
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        tree1_tokens = sys.stdin.readline().split()
        tree2_tokens = sys.stdin.readline().split()
        
        tree1 = build_tree(tree1_tokens)
        tree2 = build_tree(tree2_tokens)
        
        if is_isomorphic(tree1, tree2):
            print("The two trees are isomorphic.")
        else:
            print("The two trees are not isomorphic.")

solve()