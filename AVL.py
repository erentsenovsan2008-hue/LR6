class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Поворот
        x.right = y
        y.left = T2

        # Обновление высот
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Поворот
        y.left = x
        x.right = T2

        # Обновление высот
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, root, key):
        # 1. Стандартная вставка в БДП
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root # Дубликаты не разрешены

        # 2. Обновление высоты предка
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Получение баланс-фактора
        balance = self.get_balance(root)

        # 4. Балансировка (4 случая)
        # Левый-Левый
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Правый-Правый
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Левый-Правый
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Правый-Левый
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def delete(self, root, key):
        # 1. Стандартное удаление из БДП
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Узел найден
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Узел с двумя детьми: берем наименьший в правом поддереве
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        # 2. Обновление высоты
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Балансировка
        balance = self.get_balance(root)

        # Левый-Левый
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        # Левый-Правый
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Правый-Правый
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        # Правый-Левый
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
