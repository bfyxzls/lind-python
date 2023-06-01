from flask import Blueprint

from utils.tool import load_json

userPrint = Blueprint("lawsuit", __name__)


@userPrint.route(f"/", methods=["GET"])
def list():
    msg = {
        "code": 200,
        "msg": "ok",
    }
    data = load_json("json.json")
    msg.update({"data": data})  # 合并字典
    return msg
