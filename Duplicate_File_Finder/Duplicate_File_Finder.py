import os
import hashlib

files_dir = {}  # "file_hash" = "file_name"
directory = input("enter path of folder:")

for root, _, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            with open(file_path, "rb") as f:
                content = f.read()
        except (PermissionError, OSError):
            continue
        file_hash = hashlib.md5(content).hexdigest()
        if file_hash in files_dir:
            print("- Duplicate found!")
            print("- Original=", files_dir[file_hash])
            print("- Duplicate=", file)
        else:
            files_dir[file_hash] = file_path
print("Program exited!")
