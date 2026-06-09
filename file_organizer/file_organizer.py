import os
import shutil

extension_list = {
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "svg": "Images",
    "mp4": "Videos",
    "avi": "Videos",
    "mov": "Videos",
    "mkv": "Videos",
    "mp3": "Audios",
    "wav": "Audios",
    "doc": "Documents",
    "docx": "Documents",
    "pdf": "Documents",
    "txt": "Documents",
    "odt": "Documents"
}
categories = ["Images", "Videos", "Audios", "Documents", "Others"]
folder_path = input("Enter path of the folder to be organized:")
list_of_files = os.listdir(folder_path)

# make direcories if not already exists
for category in categories:
    path = os.path.join(folder_path, category)
    if not os.path.exists(path):
        os.mkdir(path)

for file in list_of_files:
    file_path = os.path.join(folder_path, file)
    # skip folders
    if os.path.isdir(file_path):
        continue
    # arrange folder wise
    extension = (file.split(".")[-1].lower()) if "." in file else ""
    if extension in extension_list:
        shutil.move(file_path, os.path.join(
            folder_path, extension_list[extension]))
    else:
        shutil.move(file_path, os.path.join(folder_path, "Others"))

    print(f"MOVED: {file} -> {extension_list.get(extension, "Others")}")
