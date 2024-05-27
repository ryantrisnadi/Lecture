'''
=================================================
Graded Challenge 1

Nama  : Ryan Trisnadi
Batch : HCK - 017 (Pondok Indah)

MASUKKAN ALASAN DISINI: Program ini dibuat sebagai system untuk menerima data pembeli dari USER, dan memberi pilihan untuk pilih barang lain-lainnya sebelum diproses untuk pembayaran.  
=================================================
'''

#use miro
#create the code
    #NEED LIST
    #add classes:
        #Cart Item
        #Shopping Cart
    #Use while loops and conditional Ifs
    #if error, must show error sign

#remember to error test





def display_menu():
    print("\nMenu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

def add_item(cart):
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    cart[item] = price
    print(f"{item} added to cart.")

def remove_item(cart):
    item = input("Enter item name to remove: ")
    if item in cart:
        del cart[item]
        print(f"{item} removed from cart.")
    else:
        print(f"{item} not found in cart.")

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item, price in cart.items():
            print(f"{item}: ${price:.2f}")

def checkout(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        total = sum(cart.values())
        print(f"Total: ${total:.2f}")
        cart.clear()
        print("Thank you for shopping with us!")

def main():
    cart = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item(cart)
        elif choice == '2':
            remove_item(cart)
        elif choice == '3':
            view_cart(cart)
        elif choice == '4':
            checkout(cart)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
