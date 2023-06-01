import logging

from flask import Flask

from api.user import userPrint

app = Flask(__name__)
app.register_blueprint(userPrint, url_prefix="/users")


@app.route("/")
def hello_world():
    logging.info("hello,world");
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s][%(module)s][%(funcName)s][%(lineno)s] %(message)s",  # 日志级别，模块名，函数名，行号，消息
        level=logging.INFO,
    )
    app.run(host="0.0.0.0", port=9010, threaded=True, use_reloader=False)
