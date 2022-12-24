import pytest
import requests


class TestAPI:
    def test_api(self):
        response = requests.get('http://127.0.0.1:5000/api/posts')
        assert response.status_code == 200
        keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
        keys2 = set(response.json()[0].keys())
        assert keys == keys2

    def test_api_post(self):
        response = requests.get('http://127.0.0.1:5000/api/posts/1')
        assert response.status_code == 200
        assert response.json()['pk'] == 1
