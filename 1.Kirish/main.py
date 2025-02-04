# Kitob classi
class Book:
    book_id_counter = 1

    def __init__(self, title, author, genre, price, quantity):
        self.id = Book.book_id_counter
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity
        Book.book_id_counter += 1

    def update(self, price=None, quantity=None):
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity

    def __str__(self):
        return f"ID: {self.id}, Nomi: {self.title}, Muallif: {self.author}, Narx: {self.price}, Miqdor: {self.quantity}"


# Foydalanuvchi classi
class User:
    user_id_counter = 1

    def __init__(self, name, phone, address):
        self.id = User.user_id_counter
        self.name = name
        self.phone = phone
        self.address = address
        User.user_id_counter += 1

    def __str__(self):
        return f"ID: {self.id}, Ism: {self.name}, Telefon: {self.phone}, Manzil: {self.address}"


# Sotuv classi
class Sale:
    sale_id_counter = 1

    def __init__(self, book, user):
        self.id = Sale.sale_id_counter
        self.book = book
        self.user = user
        self.price = book.price
        Sale.sale_id_counter += 1

    def __str__(self):
        return f"Sotuv ID: {self.id}, Kitob: {self.book.title}, Foydalanuvchi: {self.user.name}, Narx: {self.price}"


# Do'kon classi: Barcha operatsiyalarni boshqaradi
class Bookstore:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.sales = {}

    # Kitob qo'shish
    def add_book(self, title, author, genre, price, quantity):
        new_book = Book(title, author, genre, price, quantity)
        self.books[new_book.id] = new_book
        print(f"Kitob '{title}' muvaffaqiyatli qo'shildi! Kitob ID: {new_book.id}")

    # Kitobni yangilash
    def update_book(self, book_id, price=None, quantity=None):
        if book_id in self.books:
            self.books[book_id].update(price, quantity)
            print(f"Kitob ID {book_id} muvaffaqiyatli yangilandi.")
        else:
            print(f"Kitob ID {book_id} topilmadi.")

    # Kitobni o'chirish
    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Kitob ID {book_id} muvaffaqiyatli o'chirildi.")
        else:
            print(f"Kitob ID {book_id} topilmadi.")

    # Foydalanuvchi qo'shish
    def add_user(self, name, phone, address):
        new_user = User(name, phone, address)
        self.users[new_user.id] = new_user
        print(f"Foydalanuvchi '{name}' muvaffaqiyatli qo'shildi! Foydalanuvchi ID: {new_user.id}")

    # Sotuv qo'shish
    def add_sale(self, book_id, user_id):
        if book_id in self.books and user_id in self.users:
            book = self.books[book_id]
            user = self.users[user_id]
            if book.quantity > 0:
                book.quantity -= 1
                new_sale = Sale(book, user)
                self.sales[new_sale.id] = new_sale
                print(f"Sotuv ID {new_sale.id} muvaffaqiyatli qo'shildi!")
            else:
                print(f"Kitob '{book.title}' qolmadi.")
        else:
            print(f"Kitob ID yoki Foydalanuvchi ID topilmadi.")

    # Kitoblar ro'yxatini ko'rsatish
    def list_books(self):
        if self.books:
            for book in self.books.values():
                print(book)
        else:
            print("Hech qanday kitob mavjud emas.")

    # Foydalanuvchilar ro'yxatini ko'rsatish
    def list_users(self):
        if self.users:
            for user in self.users.values():
                print(user)
        else:
            print("Hech qanday foydalanuvchi mavjud emas.")

    # Sotuvlar ro'yxatini ko'rsatish
    def list_sales(self):
        if self.sales:
            for sale in self.sales.values():
                print(sale)
        else:
            print("Hech qanday sotuv mavjud emas.")


# Terminal menyusi uchun funksiya
def menu():
    store = Bookstore()
    
    while True:
        print("\nKitob Do'koni Boshqaruv Menyusi:")
        print("1. Kitob qo'shish")
        print("2. Kitob yangilash")
        print("3. Kitob o'chirish")
        print("4. Kitoblarni ko'rish")
        print("5. Foydalanuvchi qo'shish")
        print("6. Foydalanuvchilarni ko'rish")
        print("7. Sotuv qilish")
        print("8. Sotuvlar ro'yxatini ko'rish")
        print("0. Chiqish")

        choice = input("Tanlovingizni kiriting: ")

        if choice == "1":
            title = input("Kitob nomini kiriting: ")
            author = input("Muallifini kiriting: ")
            genre = input("Janrini kiriting: ")
            price = float(input("Narxini kiriting: "))
            quantity = int(input("Miqdorni kiriting: "))
            store.add_book(title, author, genre, price, quantity)

        elif choice == "2":
            book_id = int(input("Yangilanishi kerak bo'lgan kitob ID sini kiriting: "))
            price = float(input("Yangi narxini kiriting (skip uchun 0 kiriting): "))
            quantity = int(input("Yangi miqdorni kiriting (skip uchun 0 kiriting): "))
            store.update_book(book_id, price if price != 0 else None, quantity if quantity != 0 else None)

        elif choice == "3":
            book_id = int(input("O'chirilishi kerak bo'lgan kitob ID sini kiriting: "))
            store.delete_book(book_id)

        elif choice == "4":
            store.list_books()

        elif choice == "5":
            name = input("Foydalanuvchi ismini kiriting: ")
            phone = input("Telefon raqamini kiriting: ")
            address = input("Manzilini kiriting: ")
            store.add_user(name, phone, address)

        elif choice == "6":
            store.list_users()

        elif choice == "7":
            book_id = int(input("Sotiladigan kitob ID sini kiriting: "))
            user_id = int(input("Xarid qiluvchi foydalanuvchi ID sini kiriting: "))
            store.add_sale(book_id, user_id)

        elif choice == "8":
            store.list_sales()

        elif choice == "0":
            print("Chiqish...")
            break

        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")

# Menuni ishga tushirish
menu()
