import pytest
from comments_dao import CommentsDAO


class TestComments:
    def test_get_comments(self):
        comments = CommentsDAO('./data/comments.json')
        assert type(comments.get_comments()) is list

    def test_get_comments_by_post_id(self):
        comments = CommentsDAO('./data/comments.json')
        assert comments.get_comments_by_post_id(1)[0]['post_id'] == 1
