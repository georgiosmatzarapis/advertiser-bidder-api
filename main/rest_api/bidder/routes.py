""" Module with bidder endpoints. """
# Python libs.
import json
import os.path
from cerberus import Validator
from flask_restplus import Namespace, Resource
# Project files.
from main import lg
from main.helpers.main_config import CONFIGURATION
from .lib import CampaignProcess


request_schema_path = CONFIGURATION.request_schema_path
request_validator_path = CONFIGURATION.request_validator_path
LOGGER = lg.get_logger(__name__)
NAMESPACE = Namespace("Bidder", description="Api namespace representing bidder.")

# File loading.
if os.path.isfile(request_schema_path) and (os.path.isfile(request_validator_path)):
    with open(request_schema_path) as file:
        REQUEST_SCHEMA = json.load(file)

    with open(request_validator_path) as file:
        REQUEST_VALIDATOR = json.load(file)
else:
    LOGGER.critical(f"Request file not found.")
    exit(1)

# Add json schema to request.
bid_request = NAMESPACE.schema_model("Bid", REQUEST_SCHEMA)

@NAMESPACE.route("/bid_request")
class BidderApi(Resource):
    """
    Api class for getting bid data.
    """

    ### ------------------ templated response ------------------ ###
    rsp_bad_request = {
        "isSuccess": False,
        "msg": "Bad Request, please provide a valid json body!"
    }

    @NAMESPACE.expect(bid_request)
    def post(self):
        """ Gets bid data. """

        req = NAMESPACE.payload
        # Validate request.
        if Validator().validate(req, REQUEST_VALIDATOR):
            rsp = CampaignProcess.find_highest_paying(req)
            return rsp
        else:
            LOGGER.error(f"Bad Request for {CONFIGURATION.bid_request_prefix}. | Status code: 400")
            return BidderApi.rsp_bad_request.get("msg"), 400
