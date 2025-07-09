import threading
import time

def worker(num):
    """Thread worker function."""
    print(f"Worker thread {num}starting")
    time.sleep(2)
    print(f"Worker thread {num} finished")

# Create a thread
threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print("All worker threads have finished execution.")