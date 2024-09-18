
products = []

while True:
    print("\nMenu")
    print("1. Add product")
    print("2. Delete product")
    print("3. Clear list")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == '1':  
        product = input("Enter product: ")
        products.append(product)
        print(f"Product '{product}' was added.")

    elif choice == '2':  
        if len(products) == 0:
            print("The list is empty.")
        else:
            print("List of products:")
            for index, product in enumerate(products):
                print(f"{index + 1}. {product}")
            delete_choice = int(input("Choose the nuber of the product to delete: "))
            if delete_choice >= 1 and delete_choice <= len(products):
                deleted_product = products.pop(delete_choice - 1)
                print(f"The product '{deleted_product}' was deleted.")
            else:
                print("Invalid choice.")

    elif choice == '3':  
        products.clear()
        print("The list was cleared successfully.")

    elif choice == '4':  
        print("Thannk you for using our program")
        break

    else:
        print("Invalid choice. Please try again")

