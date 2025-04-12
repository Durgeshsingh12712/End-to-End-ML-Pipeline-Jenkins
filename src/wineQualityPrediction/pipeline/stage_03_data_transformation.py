import os
from pathlib import Path
from src.wineQualityPrediction import logger
from src.wineQualityPrediction.config.configuration import ConfigurationManager
from src.wineQualityPrediction.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your Data Schema is not Valid")
        except Exception as e:
            print(e)