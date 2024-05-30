
class CartItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.nama}: ${self.harga}"

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def display_menu(self):
        print("Menu:")
        print("1. Menambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang di Keranjang") 
        print("4. Lihat Total Belanja") 
        print("5. Exit")

    def add_item(self):
        nama = input("Enter nama barang: ")
        harga = float(input("Enter item harga: "))
        item = CartItem(nama, harga) #
        self.cart.append(item)
        print(f"{nama} added to cart.")

    def remove_item(self):
        nama = input("Enter item nama to remove: ")
        for item in self.cart:
            if item.nama == nama:
                self.cart.remove(item)
                print(f"{nama} removed from cart.")
                break
        else:
            print(f"{nama} not found in cart.")

    def show_item_in_cart(self): 
        nama = input("Enter item nama to show: ")
        for item in self.cart:
            if item.nama == nama:
                print(item)
                break
        else:
            print(f"{nama} not found in cart.")

    def show_all_items(self): 
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("All items in cart:")
            for item in self.cart:
                print(item)

    def exit_program(self):  
        print("Goodbye!")

    def process_choice(self, choice):
        if choice == '1':
            self.add_item()
        elif choice == '2':
            self.remove_item()
        elif choice == '3':
            self.show_item_in_cart()
        elif choice == '4':
            self.show_all_items()
        elif choice == '5':
            self.exit_program()
        else:
            print("Invalid choice. Please try again.")

def main():
    shopping_cart = ShoppingCart()
    while True:
        shopping_cart.display_menu()
        choice = input("Enter your choice: ")
        shopping_cart.process_choice(choice)
        if choice == '5':
            break

if __nama__ == "__main__":
    main()
