
#We need to build thread/process system that counts the number of characters in every URL that is given.
# the output suppose to be something like - Thread 2 Downloaded 7531 chars from https://jsonplaceholder.typicode.com/posts
#And give the total chars

import threading
import requests


lock = threading.Lock()

def downloader(url, idx,char_counter):

    data = requests.get(url).json()
    char_count = len(str(data))     # JSON string

    # store result using lock and print.
    with lock:
        char_counter[idx] = char_count
        print("Thread " + str(idx + 1) + " Downloaded " + str(char_count) + " chars from " + str(url))

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    char_counter = [0] * len(urls)
    threads = []

    for idx, url in enumerate(urls):
        t = threading.Thread(target=downloader, args=(url, idx,char_counter))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total = sum(char_counter)
    print("\nTOTAL chars downloaded: " + str(total))

if __name__ == '__main__':
    main()


