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

