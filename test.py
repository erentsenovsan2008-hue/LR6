if __name__ == "__main__":
    print("=== Тестирование AVL-дерева ===")
    avl = AVLTree()
    root = None
    keys_avl = [10, 20, 30, 40, 50, 25]
    
    print("Вставка:", keys_avl)
    for key in keys_avl:
        root = avl.insert(root, key)
    
    print("In-order обход AVL:", end=" ")
    avl.inorder(root)
    print()
    
    print("Удаление 30 из AVL")
    root = avl.delete(root, 30)
    print("In-order обход AVL после удаления:", end=" ")
    avl.inorder(root)
    print("\n")


    print("=== Тестирование Красно-черного дерева ===")
    rb = RBTree()
    keys_rb = [55, 40, 65, 60, 75, 57]
    
    print("Вставка:", keys_rb)
    for key in keys_rb:
        rb.insert(key)
    
    print("In-order обход КЧ (R=Red, B=Black):")
    rb.inorder()
    
    print("Удаление 55 из КЧ")
    rb.delete_node(55)
    print("In-order обход КЧ после удаления:")
    rb.inorder()