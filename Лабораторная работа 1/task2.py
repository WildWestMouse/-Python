volume = 1.44 # В Мб
num_pages = 100
num_strings = 50
num_symbols = 25
vol_in_sym = 4 # В б

count_books = int((volume * 1024 ** 2) // (num_pages * num_strings * num_symbols * vol_in_sym))
print("Количество книг, помещающихся на дискету:", count_books)
