# Call the pipline one by one

from cnnClassifierKidney import logger
from cnnClassifierKidney.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline
from cnnClassifierKidney.pipeline.stage_02_prepare_base_model import PrepareBasedModelPipline
from cnnClassifierKidney.pipeline.stage_03_model_training import ModelTraningPipeline

STAGE_NAME = "Data Ingestion Pipline"

try:
    logger.info(f"------ {STAGE_NAME} Started ------")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f"------ {STAGE_NAME} Completed ------")

except Exception as e:
    logger.exception(e)
    raise e

# ----------------Base model pipline-----------------------
STAGE_NAME = "Prepare Based model Pipline"

if __name__ == '__main__':
    try:
        logger.info(f"------ {STAGE_NAME} Started ------")
        obj = PrepareBasedModelPipline()
        obj.main()
        logger.info(f"------ {STAGE_NAME} Completed ------")

    except Exception as e:
        logger.exception(e)
        raise e
    

# ----------------Base model pipline-----------------------
STAGE_NAME = "Model Training"

if __name__ == '__main__':
    try:
        logger.info(f"------ {STAGE_NAME} Started ------")
        obj = ModelTraningPipeline()
        obj.main()
        logger.info(f"------ {STAGE_NAME} Completed ------")

    except Exception as e:
        logger.exception(e)
        raise e