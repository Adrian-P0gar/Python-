import csv


def display_inventory(inventory):
    '''Display the inventory like this:
    rope: 1
    torch: 6
    '''
    for item, count in inventory.items():
        print("{} : {}".format(item, count))


def add_to_inventory(inventory, added_items):
    for new_item in added_items:
        if new_item in inventory:
            inventory[new_item] += 1
        if new_item not in inventory:
            inventory.update({new_item: 1})
    return inventory


def print_table(inventory, order=None):

    inventory_items = []
    print("-" * 20)
    print(" item name " + " |" + "  count")
    print("-" * 20)

    if order == 'asc':
        inventory_items = sorted(
            inventory.items(), key=lambda ite: ite[1], reverse=False)
    elif order == 'des':
        inventory_items = sorted(
            inventory.items(), key=lambda ite: ite[1], reverse=True)
    else:
        inventory_items = inventory.items()
    for item, coun in inventory_items:
        print((11 - len(item)) * ' ' + item + " | " +
              (6 - len(str(coun))) * ' ' + str(coun))

    print("-" * 20)


def import_inventory(inventory, filename="/home/pogar/Python module/SI 4/test_inventory.csv"):

    with open(filename, 'r') as temp:
        temp = temp.read().split(",")
        add_to_inventory(inventory, temp)
    # d = 0
    # while d <= len(temp):
        for item in temp:
            inventory[item] += 1
            # d = d+1
            return inventory


def export_inventory(inventory, filename='/home/pogar/Python module/SI 4/export.csv'):

    inventory_for_export = ""

    for key, values in inventory.items():
        inventory_for_export += (key + "-" + str(values))
    myData = ','.join(inventory_for_export).strip()

    myFile = open('/home/pogar/Python module/SI 4/export.csv', 'w')
    with open(filename, 'w') as file:
        file.write(myData)


def main():
    if __name__ == "__main__":
        inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
        dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
        print(inv)
        x = import_inventory(add_to_inventory(inv, dragon_loot),
                             filename="/home/pogar/Python module/SI 4/test_inventory.csv")
        print(x)
        print_table(x, 'asc')
        export_inventory(
            x, filename='/home/pogar/Python module/SI 4/export.csv')


main()
