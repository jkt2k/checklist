checklist=[]
running=True

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    for list_item in checklist:
        print(list_item)

def test():
    create("item1")
    create("item2")
    read(1)
    update(1,"item3")
    print(read(1))
    destroy(0)
    print(checklist)
    create("item17")
    list_all_items()

while running:
    selection=input("Create=C, Read=R, Update=U, Destroy=D, List=L")
    if selection=="C":
        addition=input("Input new item.")
        create(addition)
        print("Added!")
    elif selection=="R":
        index=int(input("Enter the index of the item you want to read, with the first item being 0."))
        print(read(index))
    elif selection=="U":
        index=int(input("Enter the index of the item you want to update, with the first item being 0."))
        replacement=input("What do you want to replace it with?")
        update(index,replacement)
        print("Updated!")
    elif selection=="D":
        index=int(input("Enter the index of the item you want to destroy, with the first item being 0."))
        destroy(index)
        print("Destroyed!")
    elif selection=="L":
        list_all_items()
    else:
        print("Invalid command.")