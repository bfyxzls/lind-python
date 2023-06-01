import json
import csv
import pathlib
import subprocess
import math


def load_text(path):
    with open(path, "r") as f:
        return f.read()


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_csv(path):
    with open(path, "r") as f:
        fcsv = csv.DictReader(f)
        for row in fcsv:
            yield row


def iter_json(js):
    for k, v in js.items():
        if isinstance(v, str):
            yield v
        if isinstance(v, dict):
            yield iter_json(v)


def path_validate(path):
    """
    @desc: checkout
    :param path:
    :return:
    """
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    return path


def exec_cmd(cmd):
    proc = subprocess.call(
        [cmd],
        close_fds=True,  # here
        # ...
        shell=True,
        stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,
        # encoding="utf-8",
        # timeout=1
    )
    return proc


def format_credit(value):
    if not value:
        return 0.0
    return math.ceil(value * 100) / 100
