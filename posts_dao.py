import json


class PostsDAO:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return 'PostsDAO - Модуль доступа к данным с сообщениями'

    def get_posts_all(self):
        """Получение всех постов"""
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def get_post_by_pk(self, pk):
        """Получение поста по pk"""
        for post in self.get_posts_all():
            if post['pk'] == pk:
                words = []
                for word in post['content'].split():
                    if word[0] == '#':
                        if word[-1].isalpha():
                            words.append('<a href="/tag/' + word[1:].lower() + '">#' + word[1:] + '</a>')
                        else:
                            words.append('<a href="/tag/' + word[1:-1].lower() + '">#' + word[1:-1] + '</a>' + word[-1])
                    else:
                        words.append(word)
                post['content'] = ' '.join(words)
                return post
        return

    def search_for_posts(self, substr):
        """Поиск поста по переменной"""
        posts = []
        for post in self.get_posts_all():
            if substr.lower() in post['content'].lower():
                posts.append(post)
        return posts

    def get_post_by_bookmarks(self, bookmarks):
        """Поиск поста с закладками"""
        posts = []
        for post in self.get_posts_all():
            if bookmarks.get(post['pk'], False):
                posts.append(post)
        return posts

    def get_post_by_user(self, user):
        """Поиск постов по автору"""
        posts = []
        for post in self.get_posts_all():
            if post['poster_name'] == user:
                posts.append(post)
        return posts

    def get_post_by_tag(self, tag):
        """Поиск постов по тэгу"""
        posts = []
        for post in self.get_posts_all():
            if tag in post['content']:
                posts.append(post)
        return posts
