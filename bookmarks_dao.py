import json


class BookmarksDAO:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return 'BookmarksDAO - Модуль доступа к данным с закладкам'

    def load_all(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_bookmark(self, pk):
        pk = str(pk)
        bookmarks = self.load_all()
        bookmarks[0].setdefault(pk, False)
        return bookmarks[0][pk]

    def change_bookmark(self, pk):
        pk = str(pk)
        bookmarks = self.load_all()
        bookmarks[0].setdefault(pk, False)
        bookmarks[0].update({pk: not bookmarks[0][pk]})
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(bookmarks, file)

    def total_bookmarks(self):
        counter = 0
        for value in self.load_all()[0].values():
            if value:
                counter += 1
        return counter
