import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

# This defines the paths you want to track and organise ur files.

TRACKED_FOLDER = Path.home() / "Downloads"

DESTINATION_MAP = {
    ".pdf": Path.home() / "Documents" / "PDFs",
    ".png": Path.home() / "Pictures" / "Screenshots",
    ".jpg": Path.home() / "Pictures",
    ".zip": Path.home() / "Documents" / "Archives",
}

def wait_for_file_release(filepath, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            #Try open the file exclusively. If it succeeds, Windows has released it.
            with open(filepath, 'a'):
                return True
        except IOError:
            time.sleep(0.5)
    return False


class CleanHandler(FileSystemEventHandler):
    #This function triggers automatically when a file is created.
    def on_created(self, event):
        #Ignore directories, files are what we need focusing on.
        if event.is_directory:
            return
        
        #Converts incoming string path to a path object.
        filepath = event.src_path
        filename = filepath.name
        extension = filepath.suffix.lower()

        #This checks if the file extension is the right one for to track.
        if extension in DESTINATION_MAP:
            dest_dir = DESTINATION_MAP[extension]

            #Ensure that the destination folder exists.
            dest_dir.mkdir(parents=True, exist_ok=True)

            #Call the wait function to ensure Windows is done downloading it.
            print(f"New file detected: {filename}. Waiting for download to finish...")
            if wait_for_file_release(filepath):
            # Move the file safely using Pathlib's slash syntax.
                try:
                    destination_path =dest_dir / filename
                    shutil.move(str(filepath), str(destination_path))
                    print(f"Successfully Moved: {filename} -> {dest_dir}")
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
            else:
                print(f"Timed out waiting for {filename} to be released.")
            

if __name__ == "__main__":
    event_handler = CleanHandler()
    observer = Observer()
    observer.schedule(event_handler, path=str(TRACKED_FOLDER), recursive=False)

    print(f"Watchdog is running and monitoring: {TRACKED_FOLDER}")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping Watchdog...")
        observer.stop()
    observer.join()       
