import threading
import requests

def downloader(url, index, results):
    data = requests.get(url).json()
    results[index] = len(str(data))
    print("Thread " + str(index + 1) + " Downloaded " + str(results[index]) + " chars from "  + str(url))


def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]

    results = [0] * len(urls)
    threads = []

    for i, url in enumerate(urls):
        t = threading.Thread(target=downloader, args=(url, i, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nTOTAL chars downloaded:", sum(results))

if __name__ == "__main__":
    main()
