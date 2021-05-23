import requests
import time
import base64
import json
from states import Callsign, States, StateVector
from flight import Flight, Path, Tracks
from airport import Position, Airport
from datetime import datetime, timedelta
import pandas as pd


class OpenSkyApi:
    @staticmethod
    def get_auth(username, password):
        return base64.b64encode(bytes(":".join([username, password]), "utf-8")).decode(
            "utf-8"
        )

    API = "https://opensky-network.org/api/"

    def __init__(self, username=None, password=None) -> None:
        self._auth = OpenSkyApi.get_auth(username, password)
        self._headers = {
            "Authorization": "Basic {}".format(self._auth),
            "Cookie": "XSRF-TOKEN=e4e53b87-b6f5-452b-a206-bce6a33e22c8",
        }
        self.last_request = None

    def get_states(self):
        url = OpenSkyApi.API + "states/all"
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None
        return json.loads(response.text)

    def get_states_icao24(self, icao24):
        # 4952c4 icao24 example
        url = OpenSkyApi.API + "states/all?icao24={}".format(icao24)
        print(url)
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None
        return States(json.loads(response.text))

    def get_states_timestamp(self, timestamp):
        # 4952c4 icao24 example
        url = OpenSkyApi.API + "states/all?time={}".format(timestamp)
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None
        return States(json.loads(response.text))

    def get_states_box(self, lomin=0, lamin=0, lomax=0, lamax=0):
        # 4952c4 icao24 example
        url = (
            OpenSkyApi.API
            + "states/all?lomin={lomin}&lamin={lamin}&lomax={lomax}&lamax={lamax}".format(
                lomin=lomin, lamin=lamin, lomax=lomax, lamax=lamax
            )
        )
        response = requests.request("GET", url, headers=self._headers, data={})
        states = States(json.loads(response.text))
        if not response.ok:
            return None
        return states

    def get_trajectory(self, icao24, time=int(time.time())):
        # Apparently not Working on any flight
        url = OpenSkyApi.API + "tracks?icao24={}&time={}".format(icao24, time)
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None
        track = json.loads(response.text)
        return Tracks(track)

    def get_route(self, callsign):
        url = OpenSkyApi.API + "routes?callsign={}".format(callsign)
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None
        return Callsign(json.loads(response.text))

    def get_airports(self, lomin=0, lamin=0, lomax=0, lamax=0):
        # 4952c4 icao24 example
        url = (
            OpenSkyApi.API
            + "airports/region?lomin={lomin}&lamin={lamin}&lomax={lomax}&lamax={lamax}".format(
                lomin=lomin, lamin=lamin, lomax=lomax, lamax=lamax
            )
        )
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None

        airports = list()
        response_json = json.loads(response.text)
        for airport in response_json:
            airports.append(Airport(airport))
        return airports

    def get_airport(self, icao):
        url = OpenSkyApi.API + "airports?icao={}".format(icao)
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None
        response_json = json.loads(response.text)
        return Airport(response_json)

    def get_flights_all(self, begin, end):
        url = OpenSkyApi.API + "flights/all?begin={}&end={}".format(begin, end)
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None
        response_json = json.loads(response.text)
        flights = list()
        for flight in response_json:
            flights.append(Flight(flight))
        return flights

    def get_flights_aircraft(self, icao24, begin, end):
        url = OpenSkyApi.API + "flights/aircraft?icao24={}&begin={}&end={}".format(
            icao24, begin, end
        )
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None
        if response.ok:
            flight = json.loads(response.text)
            return Flight(flight[0])
        return None

    def get_flights_arrival(self, airport, begin, end):
        url = OpenSkyApi.API + "flights/arrival?airport={}&begin={}&end={}".format(
            airport, begin, end
        )
        response = requests.request("GET", url, headers=self._headers, data={})
        if response.status_code == 503:
            time.sleep(1)
        if not response.ok:
            return None
        flight_list = list()
        flights = json.loads(response.text)
        for flight in flights:
            flight_list.append(Flight(flight))
        return flight_list

    def get_flights_departure(self, airport, begin, end):
        url = OpenSkyApi.API + "flights/departure?airport={}&begin={}&end={}".format(
            airport, begin, end
        )
        response = requests.request("GET", url, headers=self._headers, data={})
        if response.status_code == 503:
            time.sleep(1)
        if not response.ok:
            return None
        flight_list = list()
        flights = json.loads(response.text)
        for flight in flights:
            flight_list.append(Flight(flight))
        return flight_list

    def get_flight_tracks(self, icao24, time=0):
        url = OpenSkyApi.API + "tracks/all?icao24={}&time={}".format(icao24, time)
        response = requests.request("GET", url, headers=self._headers, data={})
        if not response.ok:
            return None
        track = json.loads(response.text)
        return Tracks(track)


def try_endpoints(osa):
    print(datetime.tzinfo)
    now = int(time.time())
    begin = int(now - timedelta(hours=0.5).seconds)
    end = int(now - (now % 5))
    route = osa.get_route("IBE6501")
    tracks = osa.get_flight_tracks("344502", time=end)  # None
    trajectory = osa.get_trajectory("344502", end)  # None
    state = osa.get_states_icao24("344502")
    arrivals = osa.get_flights_arrival("LEMD", begin=begin, end=end)  # None
    departure = osa.get_flights_departure("LEMD", begin=begin, end=end)  # None


if __name__ == "__main__":
    osa = OpenSkyApi(username="Wilson", password="password")
    states = osa.get_states_box(
        lomin=-10.415039, lamin=36.261992, lomax=3.262939, lamax=42.399122
    )

    airports = osa.get_airports(
        lomin=-180,
        lamin=-60,
        lomax=180,
        lamax=60,
    )

    spain_airports = osa.get_airports(
        lomin=-9.392,
        lamin=35.946,
        lomax=3.039,
        lamax=43.748,
    )

    airports_list = [x.get_dict() for x in airports]
    df = pd.DataFrame.from_records(airports_list)
    df.to_csv("./airports.csv")
