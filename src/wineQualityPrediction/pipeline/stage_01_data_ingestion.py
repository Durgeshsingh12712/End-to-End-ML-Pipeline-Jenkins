from src.wineQualityPrediction.config.configuration import ConfigurationManager
from src.wineQualityPrediction.components.data_ingestion import DataIngestion
from src.wineQualityPrediction import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):    
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        