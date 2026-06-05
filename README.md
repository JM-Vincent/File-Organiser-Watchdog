# File-Organiser-Watchdog

A smart background script that monitors a specific folder (like your messy Downloads folder) and automatically moves files into categorized subfolders the second they land.

## 🎯 Purpose

This project is a learning exercise in Python that demonstrates:
- File system monitoring using watchdog
- Automated file organization based on file types
- Background process management
- Python scripting best practices

## ✨ Features

- **Real-time Monitoring**: Watches a specified folder for new files
- **Automatic Organization**: Instantly moves files into categorized subfolders based on file type
- **Category Support**: Organizes files into:
  - 📷 **Images** (jpg, png, gif, bmp, svg, webp, etc.)
  - 📄 **PDFs** (pdf)
  - 📦 **Installers** (exe, msi, dmg, pkg, deb, etc.)
  - And more categories as needed
- **Background Operation**: Runs as a daemon process without interrupting your workflow

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- `watchdog` library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/JM-Vincent/File-Organiser-Watchdog.git
cd File-Organiser-Watchdog
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Update the target folder path in the script (default is Downloads):
```python
WATCH_FOLDER = "/path/to/your/folder"  # e.g., ~/Downloads
```

2. Run the script:
```bash
python file_organiser.py
```

3. To run in the background:
   - **On Linux/Mac**: `nohup python file_organiser.py &`
   - **On Windows**: Create a scheduled task or use `pythonw.exe`

## 📁 Project Structure

```
File-Organiser-Watchdog/
├── README.md                  # This file
├── requirements.txt           # Project dependencies
└── file_organiser.py         # Main script
```

## 🔧 Configuration

You can customize the organization categories by modifying the file type mappings in the script:

```python
FILE_CATEGORIES = {
    'Images': ['.jpg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'PDFs': ['.pdf'],
    'Installers': ['.exe', '.msi', '.dmg', '.pkg', '.deb'],
    # Add more categories as needed
}
```

## 📚 Learning Outcomes

This project covers:
- **File I/O Operations**: Reading, moving, and organizing files
- **Event-Driven Programming**: Using the watchdog library to monitor file system events
- **Error Handling**: Gracefully handling edge cases and exceptions
- **Configuration Management**: Setting up and customizing behavior
- **Process Management**: Running scripts as background processes

## 🐛 Known Limitations

- Works on Windows, macOS, and Linux (with watchdog support)
- May have timing issues with very large file transfers
- Requires read/write permissions to the target folder

## 🔮 Future Enhancements

- [ ] Configuration file support (.ini or .yaml)
- [ ] Logging system for tracking organized files
- [ ] Web interface for management
- [ ] Custom category rules via regex patterns
- [ ] Undo functionality

## 📝 License

This project is open source and available for personal and educational use.

---

**Made with ❤️ for learning Python**
