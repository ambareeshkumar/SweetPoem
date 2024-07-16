import os
import urllib.request as request
from pathlib import Path

from SweetPoem.entity import DataIngestionConfig
from SweetPoem.utils.utils import get_size
from SweetPoem.logging import logging


class DataIngestion:

    def __init__(self, config : DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok = True)
            filename, headers = request.urlretrieve(
                url = self.config.SOURCE_URL,
                filename = self.config.local_data_file
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        # def download_shakespeare_data(folder_path, file_name="shakespeare.txt"):

        #     if not os.path.exists(folder_path):
        #         os.makedirs(folder_path)

        #     url = "https://www.gutenberg.org/files/100/100-0.txt"

        #     response = requests.get(url)

        #     file_path = os.path.join(folder_path, file_name)
        #     with open(file_path, "w", encoding='utf-8') as file:
        #         file.write(response.text)
            
        #     print(f"Shakespeare dataset has been downloaded and saved to {file_path}")

        # folder_path = "./Data/shakespeare"

        # download_shakespeare_data(folder_path)