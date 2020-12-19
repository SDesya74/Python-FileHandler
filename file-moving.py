from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from os.path import join, isfile
import time

folder_from = "From"
folder_to = "To"


class FileHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        for file in os.listdir(folder_from):
            source_path = join(folder_from, file)
            target_path = join(folder_to, file)
            os.rename(source_path, target_path)
            print(f"Перемещён файл: {file}")


observer = Observer()
handler = FileHandler()
observer.schedule(handler, folder_from)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
