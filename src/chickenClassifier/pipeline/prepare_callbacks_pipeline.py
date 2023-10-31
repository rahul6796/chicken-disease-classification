from chickenClassifier.config.configuration import ConfigurationManager
from chickenClassifier.components.prepare_callbacks import PrepareCallback

from chickenClassifier import logger

STAGE_NAME = "Prepare Callback"


class PrepareCallbacksPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        prepare_callbacks.get_tb_ckpt_callbacks()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareCallbacksPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
