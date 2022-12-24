import json


class CommentsDAO:
    def __init__(self, path):
        self.path = path
        self.counter = {}
        for comment in self.get_comments():
            self.counter.setdefault(comment['post_id'], 0)
            self.counter[comment['post_id']] += 1

    def __repr__(self):
        return 'CommentsDAO - Модуль доступа к данным с комментариями'

    def get_comments(self):
        """Получение всех комментариев"""
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_comments_by_post_id(self, pk):
        """Получение комментариев по номеру поста"""
        comments = []
        for comment in self.get_comments():
            if comment['post_id'] == pk:
                comments.append(comment)
        return comments
