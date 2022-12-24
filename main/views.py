import os
import logging
from flask import Blueprint, render_template, redirect, current_app, request, url_for, jsonify
from pathlib import Path
from posts_dao import PostsDAO
from comments_dao import CommentsDAO
from bookmarks_dao import BookmarksDAO


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logger = logging.getLogger('api_logger')
logger.setLevel(logging.INFO)
api_log_file = Path(__file__).resolve().parent.parent / Path('logs/api.log')
file_handler = logging.FileHandler(api_log_file, 'w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


posts = PostsDAO(os.environ.get('POSTS_PATH'))
comments = CommentsDAO(os.environ.get('COMMENTS_PATH'))
bookmarks = BookmarksDAO(os.environ.get('BOOKMARKS_PATH'))


@main_blueprint.route('/')
def index():
    return render_template('index.html', posts=posts.get_posts_all(),
                           trunc=current_app.config.get('POSTS_PREVIEW_ROUNDING'),
                           comments_counter=comments.counter,
                           bookmarks=bookmarks.total_bookmarks(),
                           bookmark=bookmarks.bookmarks_in_digits())


@main_blueprint.route('/posts/<int:pk>')
def post_page(pk):
    post = posts.get_post_by_pk(pk)
    if not post:
        return redirect('/')
    comments.counter.setdefault(pk, 0)
    bookmark_status = bookmarks.get_bookmark(pk)
    return render_template('post.html',
                           post=post, comments=comments.get_comments_by_post_id(pk),
                           comments_counter=comments.counter[pk],
                           bookmark=bookmark_status)


@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s', '')
    posts_found = posts.search_for_posts(substr)
    if not posts_found:
        return redirect('/')
    return render_template('search.html', posts=posts_found,
                           trunc=current_app.config.get('POSTS_PREVIEW_ROUNDING'),
                           comments_counter=comments.counter,
                           counter=len(posts_found),
                           bookmark=bookmarks.bookmarks_in_digits())


@main_blueprint.route('/bookmark', methods=['POST'])
def bookmark_switch():
    pk = int(request.form.get('pk'))
    bookmarks.change_bookmark(pk)
    return redirect(url_for('.post_page', pk=pk))


@main_blueprint.route('/bookmarks')
def bookmarks_page():
    return render_template('bookmarks.html', posts=posts.get_post_by_bookmarks(bookmarks.bookmarks_in_digits()),
                           trunc=current_app.config.get('POSTS_PREVIEW_ROUNDING'),
                           comments_counter=comments.counter,
                           bookmark=bookmarks.bookmarks_in_digits())


@main_blueprint.route('/users/<string:user>')
def user_page(user):
    return render_template('user-feed.html', posts=posts.get_post_by_user(user),
                           trunc=current_app.config.get('POSTS_PREVIEW_ROUNDING'),
                           comments_counter=comments.counter,
                           bookmark=bookmarks.bookmarks_in_digits())


@main_blueprint.route('/tag/<string:tag>')
def tag_page(tag):
    return render_template('tag.html', posts=posts.get_post_by_tag(tag),
                           trunc=current_app.config.get('POSTS_PREVIEW_ROUNDING'),
                           comments_counter=comments.counter,
                           bookmark=bookmarks.bookmarks_in_digits(), tag=tag)


@main_blueprint.route('/api/posts')
def api_posts():
    logger.info('Запрос /api/posts')
    return jsonify(posts.get_posts_all())


@main_blueprint.route('/api/posts/<int:pk>')
def api_post_by_pk(pk):
    result = posts.get_post_by_pk(pk)
    if not result:
        return 'Такого поста нет'
    logger.info(f'Запрос /api/posts/{pk}')
    return jsonify(result)
