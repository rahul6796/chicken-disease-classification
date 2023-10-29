from chickenClassifier import logger
from chickenClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"{STAGE_NAME}")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as ex:
    logger.exception(ex)
    raise ex
