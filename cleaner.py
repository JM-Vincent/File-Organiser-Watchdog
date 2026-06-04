import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# This defines the paths you want to track and organise ur files.

TRACKED_FOLDER = os.path.expanduser("~/Downloads")
DESTINATION_MAP = {
    ".pdf": os.path.expanduser("~/Documents/PDFs"),
    ".png": os.path.expanduser("~/Pictures/Screenshots"),
    ".jpg": os.path.expanduser("~/Pictures"),
    ".jpeg": os.path.expanduser("~/Pictures"),
    ".zip": os.path.expanduser("~/Documents/Archives"),

}

class CleanHandler(FileSystemEventHandler):
    #This function triggers automatically when a file is created.
    def on_created(self, event):
        #Ignore directories, files are what we need focusing on.
        if event.is_directory:
            return
        
        filepath = event.src_path
        filename = os.path.basename(filepath)
        _, extension = os.path.splitext(filename)

        #This checks if the file extension is the right one for to track.
        if extension.lower() in DESTINATION_MAP:
            dest_dir = DESTINATION_MAP[extension.lower()]

            #Ensure that the destination folder exists.
            os.makedirs(dest_dir, exist_ok=True)

            #Moves the file.
            try:
                #Small sleep ensures the file is fully downloaded/written before moving.
                time.sleep(1)
                shutil.move(filepath, os.path.join(dest_dir, filename))
                print(f"Moved: {filename} -> {dest_dir}")
            
            except Exception as e:
                print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    event_handler = CleanHandler()
    observer = Observer()
    observer.schedule(event_handler, path=TRACKED_FOLDER, recursive=False)

    print(f"Watchdog is running and monitoring: {TRACKED_FOLDER}")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping Watchdog...")
        observer.stop()
    observer.join()       
