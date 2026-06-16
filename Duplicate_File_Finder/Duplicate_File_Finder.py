import os
import hashlib

files_dir = {}  # "file_hash" = "file_name"
directory = input("enter path of folder:")
duplicate_file = []

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
            print("--- Duplicate found! ---")
            print("Original=", files_dir[file_hash])
            print("Duplicate=", file)
            duplicate_file.append(os.path.join(root, file))
        else:
            files_dir[file_hash] = file_path

duplicate_file_count = len(duplicate_file)
print("-------------------------------------")
if duplicate_file_count == 0:
    print("No duplicate file found!")
else:
    print(duplicate_file_count, "duplicate pairs found!")

if duplicate_file_count > 0:
    choice = input("Do you want to remove the duplicate files? (y/n)")
    if choice == "y":
        for file in duplicate_file:
            try:
                os.remove(file)
                print(f"- {file}  [Deleted] !")
            except PermissionError:
                print(f"No Permission to Delete dupefile: {file}")
print("PROGRAM EXITED!")
