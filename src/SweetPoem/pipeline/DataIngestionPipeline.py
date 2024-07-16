from SweetPoem.config.configuration import ConfigurationManager
from SweetPoem.components.DataIngestion import DataIngestion
from SweetPoem.logging import logging



class DataIngestion_Pipeline:

    def __init__(self):
        pass

    def main(self):
        print("staring")
        logging.info("Data Ingestion Pipeline Started")
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        logging.info("Data Ingestion Pipeline Completed")


if __name__ == "__main__":
    pipeline = DataIngestion_Pipeline()
    pipeline.main()