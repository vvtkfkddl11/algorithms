import sys

n = int(sys.stdin.readline().strip())
books = {}

for i in range(n):
    book = str(sys.stdin.readline().strip())
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max_count = max(books.values())  # 최대인 판매량 ex) 4

max_book_list = []
for book, num in books.items():
    if num == max_count:
        max_book_list.append(book)
sorted_max_books = sorted(max_book_list)
print(sorted_max_books[0])