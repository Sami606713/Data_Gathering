import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

project_name = 'data_gathering'
list_of_files = [
    'requirements.txt',
    'setup.py',
    'main.py',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/logging.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py"
    # f"src/{project_name}/data_gathering/__init__.py",
    # f"src/{project_name}/saving_data"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    dir_name, file_name = os.path.split(file_path)

    if dir_name and not os.path.exists(dir_name):
        logging.info(f"Creating the directory: {dir_name}")
        os.makedirs(dir_name, exist_ok=True)

    if not os.path.isfile(file_path):
        with open(file_path, "w") as f:
            pass # Create an empty file
            logging.info(f"Creating the empty file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
