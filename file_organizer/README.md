# File Organizer

A simple Python script that automatically organizes files into folders based on their file extensions.

The program scans a user-selected directory, creates category folders if they do not already exist, and moves each file into its corresponding folder.

## Features

* Automatically organizes files by extension
* Creates category folders if they do not exist
* Supports images, videos, audio files, and documents
* Places unsupported file types into an **Others** folder
* Skips existing folders
* Displays every file movement in the terminal
* Case-insensitive extension detection

## Supported Categories

| Category  | Extensions                |
| --------- | ------------------------- |
| Images    | png, jpg, jpeg, gif, svg  |
| Videos    | mp4, avi, mov, mkv        |
| Audios    | mp3, wav                  |
| Documents | doc, docx, pdf, txt, odt  |
| Others    | Any unsupported file type |

## Requirements

* Python 3.10+

No external libraries are required.

## Run

```bash
python3 file_organizer.py
```

The program will ask for the folder to organize:

```text
Enter path of the folder to be organized:
/home/user/Downloads
```

## Example

### Before

```text
Downloads/
├── photo.jpg
├── movie.mp4
├── music.mp3
├── notes.txt
├── archive.zip
└── logo.svg
```

### After

```text
Downloads/
├── Images/
│   ├── photo.jpg
│   └── logo.svg
├── Videos/
│   └── movie.mp4
├── Audios/
│   └── music.mp3
├── Documents/
│   └── notes.txt
└── Others/
    └── archive.zip
```

## Sample Output

```text
MOVED: photo.jpg -> Images
MOVED: movie.mp4 -> Videos
MOVED: music.mp3 -> Audios
MOVED: notes.txt -> Documents
MOVED: archive.zip -> Others
MOVED: logo.svg -> Images
```

## Concepts Practiced

* File handling
* Directory traversal
* Creating directories
* Moving files with `shutil`
* Dictionaries
* String manipulation
* Path handling using `os.path`
* Conditional logic

## Future Improvements

* Handle duplicate filenames safely
* Organize files recursively inside subfolders
* Add support for more file extensions
* Organize files by creation or modification date
* Preview changes before moving files
* Add an undo feature
* Automatically monitor and organize a folder in real time
* Create a GUI version using Tkinter or PyQt

## Author

Sabal
