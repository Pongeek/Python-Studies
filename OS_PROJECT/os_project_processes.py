import multiprocessing
from unittest import result

import requests

def downloader(url, index, results,q):
    data = requests.get(url).json()
    results[index] = len(str(data))
    print("Process " + str(index + 1) + " Downloaded " + str(results[index]) + " chars from "  + str(url))

    q.put((index,len(str(data))))

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    q = multiprocessing.Queue()
    results = [0] * len(urls)
    processes = []

    for i, url in enumerate(urls):
        p = multiprocessing.Process(target=downloader, args=(url, i, results, q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    #We get the count from the array, and we add it to our results array
    for url in urls:
        i,count = q.get()
        results[i] = count

    print("\nTOTAL chars downloaded:", sum(results))



if __name__ == "__main__":
    main()
