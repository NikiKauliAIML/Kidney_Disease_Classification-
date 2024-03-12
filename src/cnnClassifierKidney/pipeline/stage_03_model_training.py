from cnnClassifierKidney.config.configuration import ConfigurationManager
from cnnClassifierKidney.components.model_training import Training
from cnnClassifierKidney import logger

STAGE_NAME = "Model Training"

class ModelTraningPipeline:
    def __init__(self):
        pass

    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f"------ {STAGE_NAME} Started ------")
        obj = ModelTraningPipeline()
        obj.main()
        logger.info(f"------ {STAGE_NAME} Completed ------")

    except Exception as e:
        logger.exception(e)
        raise e