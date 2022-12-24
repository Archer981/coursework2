import json


class PostsDAO:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return 'PostsDAO - Модуль доступа к данным с сообщениями'

    def load_data(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            read_posts = json.load(file)
        return read_posts

    def load_all(self):
        return self.load_data()

    def load_post(self, pk):
        for post in self.load_data():
            if post['pk'] == pk:
                return post
        return

    def find_posts(self, substr):
        posts = []
        for post in self.load_all():
            if substr.lower() in post['content'].lower():
                posts.append(post)
        return posts
