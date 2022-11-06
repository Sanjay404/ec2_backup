import requests
import threading
import time

THREADS = 100000
responses = 0


def madh8ckrSKil1z(i):
    global responses
    requests.get('https://whywhynotandhow.blogspot.com')
    print(f'[{i}] did an expl01t')
    responses += 1


def expl01t():
    threads = []
    try:
        for i in range(THREADS):
            t = threading.Thread(target=madh8ckrSKil1z, args=(i, ))
            t.start()
            threads.append(t)
            time.sleep(2)
    finally:
        for t in threads:
            t.join()


if __name__ == '__main__':
    expl01t()