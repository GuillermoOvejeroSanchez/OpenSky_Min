class States:
    def __init__(self, response) -> None:
        self.timestamp = response["time"]
        self.states = list()
        if response["states"]:
            for state in response["states"]:
                self.states.append(StateVector(state))
            self.states_msg = response["states"]

class Callsign:
    def __init__(self, msg) -> None:
        self.callsign = msg["callsign"]
        self.route = msg["route"]
        self.updateTime = msg["updateTime"]
        self.operatorIata = msg["operatorIata"]
        self.flightNumber = msg["flightNumber"]

class StateVector:
    """Represents the state of a vehicle at a particular time. It has the following fields:

    |  **icao24** - str	Unique ICAO 24-bit address of the transponder in hex str representation.
    |  **callsign** - str	Callsign of the vehicle (8 chars). Can be None if no callsign has been received.
    |  **origin_country** - str	Country name inferred from the ICAO 24-bit address.
    |  **time_position** - int	Unix timestamp (seconds) for the last position update. Can be None if no position report was received by OpenSky within the past 15s.
    |  **last_contact** - int	Unix timestamp (seconds) for the last update in general. This field is updated for any new, valid message received from the transponder.
    |  **longitude** - float	WGS-84 longitude in decimal degrees. Can be None.
    |  **latitude** - float	WGS-84 latitude in decimal degrees. Can be None.
    |  **baro_altitude** - float	Barometric altitude in meters. Can be None.
    |  **on_ground** - bool	bool value which indicates if the position was retrieved from a surface position report.
    |  **velocity** - float	Velocity over ground in m/s. Can be None.
    |  **true_track** - float	True track in decimal degrees clockwise from north (north=0°). Can be None.
    |  **vertical_rate** - float	Vertical rate in m/s. A positive value indicates that the airplane is climbing, a negative value indicates that it descends. Can be None.
    |  **sensors** - int[]	IDs of the receivers which contributed to this state vector. Is None if no filtering for sensor was used in the request.
    |  **geo_altitude** - float	Geometric altitude in meters. Can be None.
    |  **squawk** - str	The transponder code aka Squawk. Can be None.
    |  **spi** - bool	Whether flight status indicates special purpose indicator.
    |  **position_source** - int	Origin of this state’s position: 0 = ADS-B, 1 = ASTERIX, 2 = MLAT
    """

    def __init__(self, state: list) -> None:
        self.icao24: str = state[0]
        self.callsign: str = state[1].strip()
        self.origin_country: str = state[2]
        self.time_position: int = state[3]
        self.last_contact: int = state[4]
        self.longitude: float = state[5]
        self.latitude: float = state[6]
        self.baro_altitude: float = state[7]
        self.on_ground: bool = state[8]
        self.velocity: float = state[9]
        self.true_track: float = state[10]
        self.vertical_rate: float = state[11]
        self.sensors: list(int) = state[12]
        self.geo_altitude: float = state[13]
        self.squawk: str = state[14]
        self.spi: bool = state[15]
        self.position_source: int = state[16]