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


from main.views import main_blueprint


app.register_blueprint(main_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run()
