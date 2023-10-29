from chickenClassifier import logger
from chickenClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from chickenClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline
from chickenClassifier.pipeline.prepare_callbacks_pipeline import PrepareCallbacksPipeline
from chickenClassifier.pipeline.training_pipeline import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"{STAGE_NAME}")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as ex:
    logger.exception(ex)
    raise ex


STAGE_NAME = "Prepare base model stage"

try:
    logger.info(f"{STAGE_NAME}")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
except Exception as ex:
    logger.exception(ex)
    raise ex


# STAGE_NAME = "Prepare callbacks stage"
#
# try:
#     logger.info(f"{STAGE_NAME}")
#     prepare_callbacks = PrepareCallbacksPipeline()
#     prepare_callbacks.main()
# except Exception as ex:
#     logger.error(f"failed to preparecallback :: {ex}")


STAGE_NAME = "Model Training"

try:
    logger.info(f"{STAGE_NAME}")
    model_training = ModelTrainingPipeline()
    model_training.main()
except Exception as ex:
    logger.error(f"failed to model training :: {ex}")
