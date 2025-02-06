# template to create project folder structure 

import os
import logging
from pathlib import Path

# Basic logging config
logging.basicConfig(level=logging.INFO,format="[ %(asctime)s ]: %(message)s: ")

# list of files 
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"

]

# splitting the dir and filenames in the list

for filepath in list_of_files:
   filepath = Path(filepath)
   print(filepath)
   filedir, filename = os.path.split(filepath)

   # creating directory
   if filedir != "":
    os.makedirs(filedir, exist_ok=True)
    logging.info(f"Creating dir: {filedir} for the file: {filename}" )

   # creating file
    #If the file does not exist → Create it.
    #If the file exists but is empty → Recreate it.

   # Check if file doesn't exist or is empty
   if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
    with open(filepath, 'w') as f:
        pass  # Creates an empty file
        logging.info(f"Creating empty file {filepath}")
   
   else:
     logging.info(f"{filename} already exists ")

