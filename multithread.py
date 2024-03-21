import threading
import time
import random
import datetime

def thread_worker(thread_id):
    try:
        start_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print(f'Thread {thread_id} started at {start_time}')
        time.sleep(random.randint(1, 5))
        end_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print(f'Thread {thread_id} ended at {end_time}')
    except Exception as e:
        print(f'An error occurred in thread {thread_id}: {e}')

def main():
    print('Application started')
    start_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    print(f'All Thread started at {start_time}')
    threads = []
    # Create and start 5 threads
    for i in range(1, 6):
        thread = threading.Thread(target=thread_worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    end_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    print(f'All Thread completed at {end_time}')
    print('All threads have completed.')

if __name__ == '__main__':
    try:
        main()
        print('Application executed successfully.')
    except Exception as e:
        print(f'An error occurred: {e}')
