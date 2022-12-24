import json


class CommentsDAO:
    def __init__(self, path):
        self.path = path
        self.counter = {}
        for comment in self.load_data():
            self.counter.setdefault(comment['post_id'], 0)
            self.counter[comment['post_id']] += 1

    def __repr__(self):
        return 'CommentsDAO - Модуль доступа к данным с комментариями'

    def load_data(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            read_comments = json.load(file)
        return read_comments

    def load_all(self):
        return self.load_data()

    def load_comments(self, pk):
        comments = []
        for comment in self.load_all():
            if comment['post_id'] == pk:
                comments.append(comment)
        return comments
