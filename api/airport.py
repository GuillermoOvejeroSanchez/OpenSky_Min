class Airport:
    """"""

    def __init__(self, flight) -> None:
        self.icao = flight["icao"]
        self.iata = flight["iata"]
        self.name = flight["name"]
        self.city = flight["city"]
        self.type = flight["type"]
        self.position = Position(flight["position"])

    def get_dict(self) -> str:
        repr = dict()

        repr["icao"] = self.icao
        repr["iata"] = self.iata
        repr["name"] = self.name
        repr["city"] = self.city
        repr["type"] = self.type
        repr["position"] = self.position.get_dict()

        return repr


class Position:
    def __init__(self, pos) -> None:
        self.longitude = pos["longitude"]
        self.latitude = pos["latitude"]
        self.altitude = pos["altitude"]
        self.reasonable = pos["reasonable"]

    def get_dict(self) -> str:
        repr = dict()
        repr["longitude"] = self.longitude
        repr["latitude"] = self.latitude
        repr["altitude"] = self.altitude
        repr["reasonable"] = self.reasonable
        return repr
