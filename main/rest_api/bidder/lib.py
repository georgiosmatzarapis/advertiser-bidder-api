""" This module contains helper functions for bidder api. """
# Python libs.
import requests
import json
import os.path
from flask import Response
from cerberus import Validator
# Project files.
from main import lg
from main.helpers.main_config import CONFIGURATION


LOGGER = lg.get_logger(__name__)


class CampaignProcess:
    """
    Class which implements bidder functionality.
    """

    def __init__(self, **kwargs):
        """ 
        Class constructor.

        :param(s) kwargs: Bid data from request.
        """

        self.__dict__.update(**kwargs)


    def find_highest_paying(self):
        """ 
        Filters out campaigns which do not match the targetting criteria.
        For the rest of campaigns, finds the highest paying campaign.
        """

        # Retrieve campaigns from mocked API.
        try:
            campaigns = requests.get(f"http://127.0.0.1:5000/{CONFIGURATION.campaign_api_prefix}")
        except requests.ConnectionError as e:
            LOGGER.error(e)
            return Response("Internal Server Error", status=500)
        else:
            # [CASE]: Available data from campaign API.
            if campaigns.status_code == 200:
                
                # [CASE]: Available campaigns.
                if len(campaigns.json()) != 0:

                    ### ------------------ Validate Data From Campaign API ------------------ ###
                    # Check for the existence of validator file.
                    if not CampaignProcess.load_campaign_validator(self, CONFIGURATION.campaign_validator_path):
                        return Response("Internal Server Error", status=500)

                    validate_campaigns = []

                    for campaign in campaigns.json():
                        if Validator().validate(campaign, CampaignProcess.load_campaign_validator(self, CONFIGURATION.campaign_validator_path)):
                            validate_campaigns.append(campaign)

                    # [CASE]: No validate data.
                    if len(validate_campaigns) == 0:
                        LOGGER.error(f"No validate data from {CONFIGURATION.campaign_api_prefix}. | Status code: 404")
                        return Response("Not Found", status=404)

                    ### ------------------ Check Targetting Matching ------------------ ###
                    else:
                        campaigns_with_country = []
                        bid_country = self["device"]["geo"]["country"]

                        for campaign in validate_campaigns:
                            if bid_country in campaign["targetedCountries"]:
                                campaigns_with_country.append(campaign)

                        # [CASE]: No Matching.
                        if (len(campaigns_with_country) == 0):
                            LOGGER.debug("No matching campaigns with bid's one. | Status code: 204")
                            return Response(dict(), status=204)

                        ### ------------------ Find Highest Paying Campaign ------------------ ###
                        else:
                            temp_campaigns = []

                            for campaign in campaigns_with_country:
                                temp_campaigns.append({"id": campaign["id"],
                                                       "price": campaign["price"]})

                            # Find dict. which includes biggest price.
                            campaign_with_max_price = max(temp_campaigns, key=lambda x:x["price"])
                            
                            for campaign in campaigns_with_country:
                                if campaign["id"] == campaign_with_max_price["id"]:

                                    # Create bid response.
                                    bid_response = {"id": self["id"],
                                                    "bid": {
                                                        "campaignId": campaign["id"],
                                                        "price": campaign["price"],
                                                        "adm": campaign["adm"]
                                    }}
                                    LOGGER.info(f"Successed request for {CONFIGURATION.bid_request_prefix}. | Status code: 200")
                                    return bid_response

                else:
                    LOGGER.debug("No available campaigns. | Status code: 204")
                    return Response(dict(), status=204)


            else:
                return Response("Not Found", status=404)


    @staticmethod
    def load_campaign_validator(self, path):
        """ 
        Loads campaign validator. 
        
        :param str path: File's path, from which campaign validator is retrieved.
        """

        if os.path.isfile(path):
            with open(path) as file:
                CAMPAIGN_VALIDATOR = json.load(file)
            return CAMPAIGN_VALIDATOR
        else:
            LOGGER.error(f"Campaign validator file: {path} not found.")
            return False
