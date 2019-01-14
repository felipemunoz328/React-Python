import pprint

from uber_rides.session import Session
from uber_rides.client import UberRidesClient

def get_time_estimate( lat1, lon1, lat2, lon2):

    session = Session(server_token='Z_ubRQ6CIPlHGedtNc__jbc4nAHkunUYh3iNFH18')
    client = UberRidesClient(session)
    print(lat1)

    response = client.get_price_estimates(
        start_latitude=lat1,
        start_longitude=lon1,
        end_latitude=lat2,
        end_longitude=lon2,
        seat_count=2
        )

    estimate = response.json.get('prices')
    print(estimate)
    data = estimate[0]['duration']
    print (data)
    return data
