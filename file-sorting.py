# pip install watchdog

from watchdog.observers import Observer
from os import listdir, rename, environ, makedirs
from os.path import isfile, join, splitext, exists, dirname
import time
from watchdog.events import FileSystemEventHandler


class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):  # on file modified
        for name in listdir(main_folder):
            src_file = join(main_folder, name)

            if not isfile(src_file):
                continue

            ext = splitext(name)[-1][
                  1::]  # [-1] is the last element of list, [1::] removes first character of extension (a dot symbol)
            target = folder_by_extension.get(ext, str.capitalize(ext))
            dst_file = join(main_folder, target, name)

            if not exists(dirname(dst_file)):
                makedirs(dirname(dst_file))

            while True:  # wait for file access
                try:
                    rename(src_file, dst_file)  # move file from track folder to target folder
                    break
                except:
                    time.sleep(5)


# environ["USERPROFILE"] <- path to user folder in Windows
main_folder = join(environ["USERPROFILE"], "Desktop", "Python", "003-file-sorting-by-extension")
folder_by_extension = {
    "jpg": "Photos",
    "mp3": "Music",
    "mp4": "Video",
    "py": "Python Scripts"
}

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
