import os
import shutil
from pathlib import Path
import time

USER_PATH = os.path.expanduser('~')
directories = ["Downloads", "Desktop"]

def create_custom_path(FOLDER):
    return os.path.join(USER_PATH, FOLDER)

doc_exts = [".pdf", ".docx"]
image_exts = [".jpg", ".JPG", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png",".gif",".webp", ".bmp",".tiff", ".tif", ".HEIC", ".svg"]

file_dict = {}

start_time = time.perf_counter()

for dir in directories:
    PATH = create_custom_path(dir)
    PATH_OBJ = Path(PATH)

    for file in PATH_OBJ.iterdir():
        file_ext = file.suffix
        file_str = str(file)

        if file_ext in image_exts:
            file_dict[file_str] = "Images"
        elif file_ext in doc_exts:
            file_dict[file_str] = "Documents"

try:
    os.mkdir(os.path.join(create_custom_path("Desktop") , "Documents"))
    os.mkdir(os.path.join(create_custom_path("Desktop") , "Images"))
except FileExistsError:
    pass


for file_path, directory_name in file_dict.items():
    shutil.move(file_path, os.path.join(create_custom_path("Desktop"), directory_name))

end_time = time.perf_counter()

print(f"{len(file_dict)} files sorted")
print(f"Sorting Time: {end_time - start_time}ms")