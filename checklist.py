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

def select(index, response):
    selected=True
    while selected:
        if response=="M":
            mark_complete(index)
            print("Item marked as complete!")
            selected=False
        elif response=="R":
            print(read(index))
            selected=False
        elif response=="U":
            replacement=input("What do you want to replace it with?")
            update(index,replacement)
            print("Updated!")
            selected=False
        elif response=="D":
            destroy(index)
            print("Destroyed!")
            selected=False
        else:
            print("Invalid command")

def mark_complete(index):
    checklist[index]=checklist[index]+" [Complete]"

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
    selection=input("Create=C, Read=R, Update=U, Destroy=D, List=L, Select=S")
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
    elif selection=="S":
        index=int(input("Enter the index of the item you want to select, with the first item being 0."))
        print("Item selected.")
        response=input("Read=R, Update=U, Destroy=D, Mark Complete=M")
        select(index,response)
    else:
        print("Invalid command.")