import collections
import json
import logging
import os


class Environ(dict):
    def __getitem__(self, key):
        if super().__contains__(key):
            return super().__getitem__(key)
        else:
            return os.environ[key]

    def get(self, key, default=None):
        if super().__contains__(key):
            return super().__getitem__(key)
        else:
            return os.environ.get(key, default)


ENV_MAP = collections.defaultdict(Environ)
ENV_MAP["DEV"]["name"]="lind"
print("Hello, " + ENV_MAP["DEV"]["name"])

documentConfig = {
    "maxFileSize": 104857600,
    "maxUploadFileCount": 50,
    "maxWordCount": 10000000,
    "singleFileMaxSize": 104857600,
    "singleFileMaxWordCount": 10000000
}
print("size,",documentConfig.get("maxFileSize"))

logging.info(json.dumps(documentConfig, ensure_ascii=False, indent=4))
