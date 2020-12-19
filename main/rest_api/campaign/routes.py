""" Module with campaign endpoint. """
# Python libs.
import json
import os.path
from flask_restplus import Namespace, Resource
# Project files.
from main import lg
from main.helpers.main_config import CONFIGURATION


LOGGER = lg.get_logger(__name__)
NAMESPACE = Namespace("Campaign", description="Api namespace representing campaign.")


@NAMESPACE.route("/campaign_data")
class CampaignApi(Resource):
    """
    Api class about serving campaign data.
    """

    def get(self):
        """ Returns campaigns. """

        return CampaignApi.load_campaign(self, CONFIGURATION.campaign_data_path)

    @staticmethod
    def load_campaign(self, path):
        """ 
        Loads campaign data. 
        
        :param str path: File's path, from which campaign data are retrieved.
        """

        if os.path.isfile(path):
            with open(path) as file:
                CAMPAIGN_DATA = json.load(file)
            LOGGER.info(f"Successed request for {CONFIGURATION.campaign_api_prefix}. | Status code: 200")
            return CAMPAIGN_DATA, 200
        else:
            LOGGER.error(f"No available data from {CONFIGURATION.campaign_api_prefix}. | Status code: 404")
            return "Not Found", 404
