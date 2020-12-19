# pip install watchdog

from watchdog.observers import Observer
from os import listdir, rename, environ, makedirs
from os.path import join, splitext, exists, dirname
import time
from watchdog.events import FileSystemEventHandler


class FileHandler(FileSystemEventHandler):
    def on_any_event(self, event):  # on file modified
        print("hello")
        for name in listdir(main_folder):
            src_file = join(main_folder, name)

            ext = splitext(name)[-1][
                  1::]  # [-1] is the last element of list, [1::] removes first character of extension (a dot symbol# )
            target = get_folder_by_extension(ext)
            dst_file = join(main_folder, target, name)

            if not exists(dirname(dst_file)):
                makedirs(dirname(dst_file))

            while True:  # wait for file access
                try:
                    rename(src_file, dst_file)  # move file from track folder to target folder
                    break
                except:
                    time.sleep(5)


folder_by_extension = [
    ("Photos", ["jpg", "png"]),
    ("Documents", ["txt", "docx"])
]


def get_folder_by_extension(ext):
    for row in folder_by_extension:
        folder_name = row[0]
        extensions = row[1]
        if ext in extensions:
            return folder_name

    return str.capitalize(ext)


main_folder = "Sort"

handler = FileHandler()
observer = Observer()
observer.schedule(handler, main_folder)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
