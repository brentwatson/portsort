import time
import server
import client
import threading

unsorted = [4, 23, 1, 6, 98, 38, 5]

thread = threading.Thread(target=server.start, args=(unsorted,), daemon=True)
thread.start()
time.sleep(1)

sorted = client.start()
print(sorted)
