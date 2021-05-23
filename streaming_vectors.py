import json
import pandas as pd
import os

if __name__ == "__main__":
    df = pd.read_csv("data_export/state_vectors_ib2031.csv")
    for i, value in df.iterrows():
        value.drop(
            labels=[
                "icao241",
                "velocity",
                "heading",
                "vertrate",
                "callsign",
                "onground",
                "alert",
                "spi",
                "squawk",
                "baroaltitude",
                "geoaltitude",
                "lastposupdate",
                "lastcontact",
                "hour",
                "minute",
                "recent",
                "icao2419",
            ],
            inplace=True,
        )
        print(value)
        filename = "streaming/stream_vectors_{}.json".format(str(i).zfill(4))
        value.to_json(filename)
        os.utime(
            filename, (value.time, value.time)
        )  # Change creation time for spark to get it in order of flight time
