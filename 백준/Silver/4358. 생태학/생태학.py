from sys import stdin
input = stdin.readline

def ecology():
    tree_dict = {}
    tree_name_list = set()
    
    tree_num = 0
    
    while True:
        tree = input().rstrip()
        
        if not tree:
            break
        tree_num += 1
        
        if tree not in tree_dict.keys():
            tree_dict[tree] = 1
            tree_name_list.add(tree)
        else:
            tree_dict[tree] += 1
    
    tree_names = sorted(list(tree_name_list))
    
    return tree_dict, tree_names, tree_num


if __name__ == "__main__":
    tree_dict, tree_names, tree_num = ecology()
    
    for tree in tree_names:
        print(f"{tree} {((tree_dict[tree] / tree_num) * 100):.4f}")