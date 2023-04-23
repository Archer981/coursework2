import os
from flask import Flask, send_from_directory
import dotenv
from config import Development, Production


dotenv.load_dotenv(override=True)


app = Flask(__name__)

if os.environ.get('APP_CONFIG') == 'development':
    app.config.from_object(Development)
else:
    app.config.from_object(Production)


os.environ['POSTS_PATH'] = app.config.get('POSTS_PATH', '')
os.environ['COMMENTS_PATH'] = app.config.get('COMMENTS_PATH', '')
os.environ['BOOKMARKS_PATH'] = app.config.get('BOOKMARKS_PATH', '')


# Не получается перенести импорт в начало файла, сначала надо задать пути.
# Единственное что - перенести инициализацию переменных во вьюшки через current_upp.config,
# но тогда надо будет их в каждой вьюшке задавать, а сейчас один раз в начале инициализируются.
from main.views import main_blueprint


app.register_blueprint(main_blueprint)


@app.errorhandler(404)
def page_not_found(error):
    return 'Страница не найдена, код 404'


@app.errorhandler(500)
def internal_server_error(error):
    return 'Ошибка на сервере, код 500'


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
