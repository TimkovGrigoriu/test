# TODO заменить значение пропущенного элемента средним арифметическим
disk_Mb = 1.44
num_pages = 100
num_rows = 50
num_sumb = 25
butes_for_sumb = 4

book_in_butes = butes_for_sumb*num_sumb*num_rows*num_pages
disk_in_butes = disk_Mb*1024*1024
num_of_books = disk_in_butes // book_in_butes
mum_of_books = int(num_of_books)
print("Количество книг, помещающихся на дискету:", mum_of_books)
