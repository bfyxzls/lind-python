FROM python:3.6

WORKDIR /app
COPY * ./
RUN pip --default-timeout=100 install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
RUN ls
ENTRYPOINT ["python"]
CMD ["test-web.py"]


