class Book:
    BASE_NAME = "Book Name"

    def update_book_name(self, change: bool):
        self.BASE_NAME = "Update Book Name"

    def get_book_name(self): return self.BASE_NAME