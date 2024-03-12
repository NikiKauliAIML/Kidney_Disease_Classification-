from cnnClassifierKidney.config.configuration import ConfigurationManager
from cnnClassifierKidney.components.data_ingestion import DataIngestion
from cnnClassifierKidney import logger

STAGE_NAME = "Data ingestion step"

class DataIngestionTrainingPipline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f"------ {STAGE_NAME} Started ------")
        obj = DataIngestionTrainingPipline()
        obj.main()
        logger.info(f"------ {STAGE_NAME} Completed ------")

    except Exception as e:
        logger.exception(e)
        raise e