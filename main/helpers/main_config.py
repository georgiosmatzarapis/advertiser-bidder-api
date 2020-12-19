""" Config which initializes configuration. """
# Python libs.
import os.path
import yaml


class Config:
    """ Configuration class. """

    def __init__(self):
        """ Class constructor. """
        config_file = "main/configs/config.yaml"

        if os.path.isfile(config_file):
            conf = yaml.safe_load(open(config_file, "r"))
            self.secret_key = conf["app"]["secret_key"]
            self.request_schema_path = conf["api"]["request_schema_path"]
            self.request_validator_path = conf["api"]["request_validator_path"]
            self.campaign_validator_path = conf["api"]["campaign_validator_path"]
            self.campaign_data_path = conf["api"]["campaign_data_path"]
            self.campaign_api_prefix = conf["api"]["campaign_api_prefix"]
            self.bid_request_prefix = conf["api"]["bid_request_prefix"]
            self.file_path = conf["logging"]["file_path"]
            self.level = conf["logging"]["level"]
            self.format = conf["logging"]["format"]
        else:
            print(f"Config file: {config_file} not found.")
            exit(1)


CONFIGURATION = Config()
