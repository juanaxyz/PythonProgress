import os

inventory_toko = {
    "cola cola": 5
}


def clear_terminal():
    if os.name == "posix":
        _ = os.system('clear')
    elif os.name == "nt":
        _ = os.system('cls')
    else:
        print("\n"*100)


def menu():
    print(
        """
1.\t add product
2.\t display all product
3.\t update stock product
4.\t search product
5.\t delete product
0.\t exit
""")


def add_product():
    print("menu add product")
    key_prod = input("insert product name : ")
    stok_prod = input("insert stock product : ")

    try:
        inventory_toko[key_prod] = int(stok_prod)
        print(
            f"product {key_prod} sucess fully inserted to the inventory with stock : {stok_prod}")
    except:
        print("error while inserting product")


def display_all_product():
    for product, stock in inventory_toko.items():
        print(f"{product} : {stock}")


def update_product():
    product_name = input("product name : ")
    while inventory_toko.get(product_name, 0) == 0:
        print("product not found")
        return
    new_stock = input("insert new stock of product : ")
    inventory_toko[product_name] = new_stock


def search_product(product_name):
    return inventory_toko.get(product_name, 0)


def confirmation():
    confirm = input("back to menu ? y/n : ")
    if confirm == "n":
        return False
    else:
        return True


if __name__ == "__main__":
    loop = True
    while loop:
        menu()
        choosen_menu = input("choose menu = ")
        clear_terminal()
        match int(choosen_menu):
            case 1:
                add_product()
                loop = confirmation()
            case 2:
                display_all_product()
            case 3:
                update_product()
            case 4:
                product_name = input("product name : ")
                result = search_product(product_name)
                print(f"stock : {result}" if result !=
                      0 else "product not found")
            case 5:
                product_name = input("product name : ")
                deleted_product = inventory_toko.pop(product_name, 0)
                print(
                    f"product {product_name} successfully deleted from inventory" if deleted_product != 0 else "can't delete product")
            case 0:
                print("thanks for using this program :) ")
                print("good byee...")
                break
