import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

projectName = str(input("Enter Project Name :"))

projectFiles = [
    ".github/workflows/",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/utils/utils.py",
    f"src/{projectName}/logging/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "params/params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb"
]

for filepath in projectFiles:

    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        logging.info(f"Creating directory {filedir}")
        os.makedirs(filedir, exist_ok=True)

    if not os.path.exists(filepath) or not os.path.getsize(filepath) == 0:
        logging.info(f"Creating file {filename} inside directory {filedir}")
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created file {filename} inside directory {filedir}")
    else:
        logging.info(f"File {filename} already exists inside directory {filedir}")