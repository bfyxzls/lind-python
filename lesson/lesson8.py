from multiprocessing import Process


def worker():
    print("Worker process is running")


if __name__ == '__main__':
    # 创建进程
    process = Process(target=worker)
    process.start()
    process.join()  # 等待进程结束
