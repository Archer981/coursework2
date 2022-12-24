import pytest
from posts_dao import PostsDAO


class TestPosts:
    def test_get_posts_all(self):
        posts = PostsDAO('./data/posts.json')
        assert type(posts.get_posts_all()) == list

    def test_get_posts_by_pk(self):
        posts = PostsDAO('./data/posts.json')
        post = posts.get_post_by_pk(1)
        assert len(post) == 7
        assert post['pk'] == 1
        post = posts.get_post_by_pk(0)
        assert post is None

    def test_search_for_posts(self):
        posts = PostsDAO('./data/posts.json')
        post = posts.search_for_posts('hghfhfjfjfdhgfhgf')
        assert post == []

    def test_get_post_by_bookmarks(self):
        posts = PostsDAO('./data/posts.json')
        post = posts.get_post_by_bookmarks({1: True, 2: False, 3: True})
        assert len(post) == 2

    def test_get_post_by_user(self):
        posts = PostsDAO('./data/posts.json')
        post = posts.get_post_by_user('hghfhfjfjfdhgfhgf')
        assert post == []

    def test_get_post_by_tag(self):
        posts = PostsDAO('./data/posts.json')
        post = posts.get_post_by_tag('hghfhfjfjfdhgfhgf')
        assert post == []
