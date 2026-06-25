# Duplicate File Finder

A command-line Duplicate File Finder built in Python.

This program scans a directory and its subdirectories, detects duplicate files by comparing their file hashes, and optionally removes the duplicate copies.

## Features

* Recursive directory scanning
* Duplicate file detection using MD5 hashing
* Supports all file types
* Displays original and duplicate file locations
* Optional duplicate file deletion
* Handles permission and file access errors
* Works across nested folders

## Requirements

* Python 3.10+

## Run

```bash
python3 Duplicate_File_Finder.py
```

## How It Works

The program:

1. Recursively scans all files inside the specified directory.
2. Reads each file in binary mode.
3. Generates an MD5 hash of the file contents.
4. Compares hashes to identify duplicates.
5. Stores unique file hashes in a dictionary.
6. Reports duplicate files found.
7. Optionally deletes duplicate copies.

## Example Usage

```text
enter path of folder: ./test_folder

--- Duplicate found! ---
Original= ./test_folder/photo.jpg
Duplicate= photo (copy).jpg

--- Duplicate found! ---
Original= ./test_folder/document.pdf
Duplicate= document (copy).pdf

-------------------------------------
2 duplicate pairs found!

Do you want to remove the duplicate files? (y/n)
```

## Example Output

```text
--- Duplicate found! ---
Original= /home/user/files/image.png
Duplicate= image (copy).png

-------------------------------------
1 duplicate pairs found!
```

## Concepts Practiced

* File handling
* Directory traversal with os.walk()
* Hashing with hashlib
* Dictionaries
* Exception handling
* Binary file operations
* Data comparison
* Automation scripting

## Limitations

* Uses MD5 hashing, which is suitable for duplicate detection but not recommended for security purposes.
* Currently reads entire files into memory, which may be inefficient for very large files.

## Future Improvements

* Use SHA-256 hashing
* Process large files in chunks
* Show file sizes
* Interactive file selection before deletion
* Export duplicate reports to a text file
* GUI version
* Ignore selected file extensions
* Display scanning progress

## Author

Sabal
