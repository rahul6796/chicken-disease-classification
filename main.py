from chickenClassifier import logger
from chickenClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from chickenClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline


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
