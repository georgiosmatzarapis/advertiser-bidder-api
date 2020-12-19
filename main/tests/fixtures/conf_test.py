import pytest

@pytest.fixture
def supply_url():
	return "http://127.0.0.1:5000/api/Bidder/bid_request"