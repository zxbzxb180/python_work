from queue import Queue

if __name__ == '__main__':
    message_queue = Queue()

    message_queue.put('chenxi', timeout=3)
    message = message_queue.get()
