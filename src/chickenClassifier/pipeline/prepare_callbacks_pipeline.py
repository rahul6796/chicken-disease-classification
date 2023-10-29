from chickenClassifier.config.configuration import ConfigurationManager
from chickenClassifier.components.prepare_callbacks import PrepareCallback


class PrepareCallbacksPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        prepare_callbacks.get_tb_ckpt_callbacks()


