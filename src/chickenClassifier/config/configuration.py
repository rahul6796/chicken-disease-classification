from chickenClassifier.constant import *
from chickenClassifier.utils.common import read_yaml, create_directories
from chickenClassifier.entity import DataIngestionConfig

class ConfigurationManager:

    def __init__(self,
                 config_file=CONFIG_FILE_PATH,
                 params_file=PARAMS_FILE_PATH):

        self.config = config_file
        self.param = params_file
        create_directories(self.config.artifacts)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
