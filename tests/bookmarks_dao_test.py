import pytest
from bookmarks_dao import BookmarksDAO


class TestBookmarks:
    def test_load_all(self):
        bookmarks = BookmarksDAO('./data/bookmarks.json')
        assert type(bookmarks.load_all()) is list

    def test_get_bookmark(self):
        bookmarks = BookmarksDAO('./data/bookmarks.json')
        assert bookmarks.get_bookmark(10000) is False

    def test_change_bookmark(self):
        bookmarks = BookmarksDAO('./data/bookmarks.json')
        status_1 = bookmarks.get_bookmark(1)
        bookmarks.change_bookmark(1)
        assert status_1 != bookmarks.get_bookmark(1)

    def test_total_bookmarks(self):
        bookmarks = BookmarksDAO('./data/bookmarks.json')
        total = bookmarks.total_bookmarks()
        bookmarks.change_bookmark(1)
        assert total - 1 <= bookmarks.total_bookmarks() <= total + 1

    def test_bookmarks_in_digits(self):
        bookmarks = BookmarksDAO('./data/bookmarks.json')
        result = bookmarks.bookmarks_in_digits()
        for k in result.keys():
            assert type(k) is int
