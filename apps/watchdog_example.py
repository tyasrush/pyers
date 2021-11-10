import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import time
import psutil

while True:
    cpu_usage = psutil.cpu_percent(interval=0.5)
    print(f"cpu usage: {cpu_usage}")
    time.sleep(0.7)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.isAlive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()