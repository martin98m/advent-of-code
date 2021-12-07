max_val = 80
count_child = 0


class family_tree:
    def __init__(self, val, next_val, first=False):
        self.value = val
        if first:
            self.left = family_tree(val+1, 7) if val+1 < max_val else None
            self.right = family_tree(val+1, 9) if val+1 < max_val else None
        else:
            l = val + next_val
            self.left = family_tree(l, 7) if l <= max_val else None
            r = val + next_val
            self.right = family_tree(r, 9) if r <= max_val else None


def printInorder(root):
    if root:
        # First recur on left child
        if root.left is None and root.right is None:
            # print(root.value)
            global count_child
            count_child = count_child + 1
        else:
            printInorder(root.left)
            printInorder(root.right)


if __name__ == '__main__':

    # treea = family_tree(3,6,True)
    # treeb = family_tree(4,6,True)
    # treec = family_tree(3,6,True)
    # treed = family_tree(1,6,True)
    # treee = family_tree(2,6,True)

    # printInorder(treea)
    # print("--")
    # printInorder(treeb)
    # print("--")
    # printInorder(treec)
    # print("--")
    # printInorder(treed)
    # print("--")
    # printInorder(treee)

    # print(count_child)

    # text_file = open("test.txt", "r")
    text_file = open("input.txt", "r")
    lines = [int(x) for x in text_file.read().split(",")]
    i = 0
    for fish in lines:
        print(i)
        i = i + 1
        # family_tree(fish, 6, True)
        printInorder(family_tree(fish, 6, True))
    print("over")
    print(count_child)