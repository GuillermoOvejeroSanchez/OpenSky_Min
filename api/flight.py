class Flight:
    """Represents the state of a vehicle at a particular time. It has the following fields:
    |  **icao24** - str Unique ICAO 24-bit address of the transponder in hex string representation. All letters are lower case.
    |  **firstSeen** - integer	Estimated time of departure for the flight as Unix time (seconds since epoch).
    |  **estDepartureAirport** - string	ICAO code of the estimated departure airport. Can be None if the airport could not be identified.
    |  **lastSeen** - integer	Estimated time of arrival for the flight as Unix time (seconds since epoch)
    |  **estArrivalAirport** - string	ICAO code of the estimated arrival airport. Can be None if the airport could not be identified.
    |  **callsign** - string	Callsign of the vehicle (8 chars). Can be None if no callsign has been received. If the vehicle transmits multiple callsigns during the flight, we take the one seen most frequently
    |  **estDepartureAirportHorizDistance** - integer	Horizontal distance of the last received airborne position to the estimated departure airport in meters
    |  **estDepartureAirportVertDistance** - integer	Vertical distance of the last received airborne position to the estimated departure airport in meters
    |  **estArrivalAirportHorizDistance** - integer	Horizontal distance of the last received airborne position to the estimated arrival airport in meters
    |  **estArrivalAirportVertDistance** - integer	Vertical distance of the last received airborne position to the estimated arrival airport in meters
    |  **departureAirportCandidatesCount** - integer	Number of other possible departure airports. These are airports in short distance to estDepartureAirport.
    |  **arrivalAirportCandidatesCount** - integer	Number of other possible departure airports. These are airports in short distance to estArrivalAirport.
    """

    def __init__(self, states: list) -> None:
        self.icao24: str = states["icao24"]
        self.firstSeen: int = states["firstSeen"]
        self.estDepartureAirport: str = states["estDepartureAirport"]
        self.lastSeen: int = states["lastSeen"]
        self.estArrivalAirport: str = states["estArrivalAirport"]
        self.callsign: str = states["callsign"]
        self.estDepartureAirportHorizDistance: int = states["estDepartureAirportHorizDistance"]
        self.estDepartureAirportVertDistance: int = states["estDepartureAirportVertDistance"]
        self.estArrivalAirportHorizDistance: int = states["estArrivalAirportHorizDistance"]
        self.estArrivalAirportVertDistance: int = states["estArrivalAirportVertDistance"]
        self.departureAirportCandidatesCount: int = states["departureAirportCandidatesCount"]
        self.arrivalAirportCandidatesCount: int = states["arrivalAirportCandidatesCount"]


class Tracks:
    """
    |  **icao24** - string Unique ICAO 24-bit address of the transponder in lower case hex string representation.
    |  **startTime** - integer Time of the first waypoint in seconds since epoch (Unix time).
    |  **endTime** - integer Time of the last waypoint in seconds since epoch (Unix time).
    |  **calllsign** - string Callsign (8 characters) that holds for the whole track. Can be None.
    |  **path** - list Waypoints of the trajectory (description below).
    """
    
    def __init__(self, states) -> None:
        self.icao24: str = states[0]
        self.startTime: int = states[1]
        self.endTime: int = states[2]
        self.calllsign: str = states[3]
        self.path: list(Path) = states[4]
    
    
class Path:
    """
    |  **time** - integer Time which the given waypoint is associated with in seconds since epoch (Unix time).
    |  **latitude** - float WGS-84 latitude in decimal degrees. Can be None.
    |  **longitude** - float WGS-84 longitude in decimal degrees. Can be None.
    |  **baro_altitude** - float Barometric altitude in meters. Can be None.
    |  **true_track** - float True track in decimal degrees clockwise from north (north=0°). Can be None.
    |  **on_ground** - boolean Boolean value which indicates if the position was retrieved from a surface position report.
    """
    
    def __init__(self, states) -> None:
        self.time:int = states[0]
        self.latitude:float = states[1]
        self.longitude:float = states[2]
        self.baro_altitude:float = states[3]
        self.true_track:float = states[4]
        self.on_ground:bool = states[5]