# TODO Найдите количество книг, которое можно разместить на дискете
floppy_size_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
floppy_size_bytes = floppy_size_mb * 1024 * 1024

chars_per_book = pages_per_book * lines_per_page * chars_per_line
book_size_bytes = chars_per_book * bytes_per_char

books_on_floppy = int (floppy_size_bytes / book_size_bytes)
print (f"Количество книг, помещающихся на дискету: {books_on_floppy}")