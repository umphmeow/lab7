import random

class BookRecommendation:
    def __init__(self, k):
        self.k = k
        self.books = [{'title': f"Book{i + 1}"} for i in range(k)]
        self.all_book_sequences = []

    def read_books(self, books, k, current=[], result=[]):
        if len(current) == k:
            result.append(current)
        else:
            for i in range(len(books)):
                if books[i] not in current:
                    self.read_books(books, k, current + [books[i]], result)
        return result

    def rating_and_pages(self, books):
        for book in books:
            rating = round(random.uniform(1.0, 5.0), 1)
            pages = random.randint(50, 500)
            book['rating'] = rating
            book['pages'] = pages
        return books

    def get_permutations(self, books, r):
        if r == 0:
            return [[]]
        permutations = []
        for i in range(len(books)):
            for permutation in self.get_permutations(books[:i] + books[i + 1:], r - 1):
                permutations.append([books[i]] + permutation)
        return permutations

    def generate_book_sequences(self):
        if self.k == 0:
            print('Нельзя составить последовательности чтения книг')
        else:
            self.all_book_sequences = self.read_books(self.books, self.k)
            print("Все возможные последовательности чтения книг:")
            for sequence in self.all_book_sequences:
                print([book['title'] for book in sequence])

    def generate_rating_and_pages(self):
        self.books = self.rating_and_pages(self.books)
        print("Список книг с присвоенными рейтингом и количеством страниц:")
        for book in self.books:
            print(book)

# Usage example:
k = int(input("Введите количество книг: "))
recommendation = BookRecommendation(k)
recommendation.generate_book_sequences()
recommendation.generate_rating_and_pages()
