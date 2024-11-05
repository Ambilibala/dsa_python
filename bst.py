class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self):
        item = int(input("Enter the data to insert: "))
        new_node = Node(item)
        if self.root is None
            self.root = new_node
        else:
            q = self.root
            while q is not None:
                p = q
                if q.data > item:
                    q = q.left
                elif q.data < item:
                    q = q.right
                else:
                    print("Duplicates are not allowed")
                    return
            if p.data > item:
                p.right = new_node
            else:
                p.left = new_node

    def preorder(self, ptr):
        if ptr is None:
            return
        print(ptr.data, end='\t')
        self.preorder(ptr.left)
        self.preorder(ptr.right)

    def inorder(self, ptr):
        if ptr is None:
            return
        self.inorder(ptr.left)
        print(ptr.data, end='\t')
        self.inorder(ptr.right)

    def postorder(self, ptr):
        if ptr is None:
            return
        self.postorder(ptr.left)
        self.postorder(ptr.right)
        print(ptr.data, end='\t')

    def search(self):
        d = int(input("Enter the data to search: "))
        q = self.root
        while q is not None:
            if q.data > d:
                q = q.left
            elif q.data < d:
                q = q.right
            else:
                print("Data found:", q.data)
                return
        print("Data not found")

    def main(self):
        while True:
            print("Enter the choice:")
            print("1. Insert")
            print("3. Inorder")
            print("4. Postorder")
            print("5. Preorder")
            print("6. Search")
            print("7. Exit")
            choice = int(input())
            if choice == 1:
                self.insert()
            elif choice == 3:
                self.inorder(self.root)
            elif choice == 4:
                self.postorder(self.root)
            elif choice == 5:
                self.preorder(self.root)
            elif choice == 6:
                self.search()
            elif choice == 7:
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    tree = BinaryTree()
    tree.main()