```bash
[hadoop-29:21000] > show tables;
+--------------------------+
| name                     |
+--------------------------+
| acas_data4               |
| allcall_replies_data4    |
| flarm_raw                |
| flights                  |
| flights_data4            |
| identification_data4     |
| operational_status_data4 |
| position_data4           |
| rollcall_replies_data4   |
| sensor_visibility        |
| sensor_visibility_data3  |
| state_vectors            |
| state_vectors_data3      |
| state_vectors_data4      |
| velocity_data4           |
+--------------------------+
[hadoop-29:21000] > describe acas_data4;
+------------------------------+-------------------+---------+
| name                         | type              | comment |
+------------------------------+-------------------+---------+
| sensors                      | array<struct<     |         |
|                              |   serial:int,     |         |
|                              |   mintime:double, |         |
|                              |   maxtime:double  |         |
|                              | >>                |         |
| rawmsg                       | string            |         |
| mintime                      | double            |         |
| maxtime                      | double            |         |
| msgcount                     | bigint            |         |
| icao24                       | string            |         |
| islongformat                 | boolean           |         |
| isairborne                   | boolean           |         |
| hascrosslinkcapability       | boolean           |         |
| sensitivitylevel             | smallint          |         |
| replyinformation             | smallint          |         |
| altitude                     | double            |         |
| hasvalidrac                  | boolean           |         |
| activeresolutionadvisories   | smallint          |         |
| resolutionadvisorycomplement | smallint          |         |
| nopassbelow                  | boolean           |         |
| nopassabove                  | boolean           |         |
| noturnleft                   | boolean           |         |
| noturnright                  | boolean           |         |
| hasterminated                | boolean           |         |
| hasmultiplethreats           | boolean           |         |
| hour                         | int               |         |
+------------------------------+-------------------+---------+
[hadoop-29:21000] > describe allcall_replies_data4;
+--------------+-------------------+---------+
| name         | type              | comment |
+--------------+-------------------+---------+
| sensors      | array<struct<     |         |
|              |   serial:int,     |         |
|              |   mintime:double, |         |
|              |   maxtime:double  |         |
|              | >>                |         |
| rawmsg       | string            |         |
| mintime      | double            |         |
| maxtime      | double            |         |
| msgcount     | bigint            |         |
| icao24       | string            |         |
| capabilities | smallint          |         |
| interrogator | string            |         |
| hour         | int               |         |
+--------------+-------------------+---------+
[hadoop-29:21000] > describe flarm_raw;
+--------------------+---------+-------------------------------------------------------------------------------------+
| name               | type    | comment                                                                             |
+--------------------+---------+-------------------------------------------------------------------------------------+
| sensortype         | string  | Type of the sensor                                                                  |
| sensorlatitude     | double  | Latitude of the sensor                                                              |
| sensorlongitude    | double  | Longitude of the sensor                                                             |
| sensoraltitude     | int     | Altitude of the sensor in meters (int)                                              |
| timeatserver       | double  | Time at the ingestion server                                                        |
| timeatsensor       | double  | Time at the sensor (not used yet)                                                   |
| timestamp          | double  | Timestamp                                                                           |
| timeatplane        | int     | Time at which the position was broadcasted by the FLARM device                      |
| rawmessage         | string  | 26 bytes FLARMv6 Raw message                                                        |
| crc                | string  | CRC Pertaining to the FLARMv6 Raw message                                           |
| rawsoftmessage     | string  | Soft bits, 4 per real bit, of a FLARMv6 Raw message (4*26 bytes)                    |
| sensorname         | string  | Name of the sensor as broadcasted by OGN                                            |
| ntperror           | float   | Error of the sensor\'s clock compared to NTP                                         |
| userfreqcorrection | float   | Dongle ppm correction set by the user                                               |
| autofreqcorrection | float   | Additional dongle ppm correction set by automatic calibration                       |
| frequency          | double  | Exact frequency at which the message was received                                   |
| channel            | int     | Channel on which the message was received (Important for hopping schemes US/AUS/NZ) |
| snrdetector        | double  | SNR at the detector                                                                 |
| snrdemodulator     | double  | SNR at the demodulator                                                              |
| typeogn            | boolean | Type of the message (True > OGN, False > FLARM)                                     |
| crccorrect         | boolean | Is the CRC of the message correct?                                                  |
| hour               | int     |                                                                                     |
+--------------------+---------+-------------------------------------------------------------------------------------+
[hadoop-29:21000] > describe flights;
+-------------+--------+---------+
| name        | type   | comment |
+-------------+--------+---------+
| icao24      | string |         |
| firstseen   | string |         |
| lastseen    | string |         |
| duration    | bigint |         |
| callsign    | string |         |
| departure   | string |         |
| destination | string |         |
+-------------+--------+---------+
[hadoop-29:21000] > describe flights_data4
+----------------------------------+----------------------+
| name                             | type                 |
+----------------------------------+----------------------+
| icao24                           | string               |
| firstseen                        | int                  |
| estdepartureairport              | string               |
| lastseen                         | int                  |
| estarrivalairport                | string               |
| callsign                         | string               |
| track                            | array<struct<        |
|                                  |   time:int,          |
|                                  |   latitude:double,   |
|                                  |   longitude:double,  |
|                                  |   altitude:double,   |
|                                  |   heading:float,     |
|                                  |   onground:boolean   |
|                                  | >>                   |
| serials                          | array<int>           |
| estdepartureairporthorizdistance | int                  |
| estdepartureairportvertdistance  | int                  |
| estarrivalairporthorizdistance   | int                  |
| estarrivalairportvertdistance    | int                  |
| departureairportcandidatescount  | int                  |
| arrivalairportcandidatescount    | int                  |
| otherdepartureairportcandidates  | array<struct<        |
|                                  |   icao:string,       |
|                                  |   horizdistance:int, |
|                                  |   vertdistance:int   |
|                                  | >>                   |
| otherarrivalairportcandidates    | array<struct<        |
|                                  |   icao:string,       |
|                                  |   horizdistance:int, |
|                                  |   vertdistance:int   |
|                                  | >>                   |
| day                              | int                  |
+----------------------------------+----------------------+
[hadoop-29:21000] > describe identification_data4
+-----------------+-------------------+---------+
| name            | type              | comment |
+-----------------+-------------------+---------+
| sensors         | array<struct<     |         |
|                 |   serial:int,     |         |
|                 |   mintime:double, |         |
|                 |   maxtime:double  |         |
|                 | >>                |         |
| rawmsg          | string            |         |
| mintime         | double            |         |
| maxtime         | double            |         |
| msgcount        | bigint            |         |
| icao24          | string            |         |
| emittercategory | smallint          |         |
| ftc             | smallint          |         |
| identity        | string            |         |
| hour            | int               |         |
+-----------------+-------------------+---------+
[hadoop-29:21000] > describe operational_status_data4;
+---------------------------------+-------------------+---------+
| name                            | type              | comment |
+---------------------------------+-------------------+---------+
| sensors                         | array<struct<     |         |
|                                 |   serial:int,     |         |
|                                 |   mintime:double, |         |
|                                 |   maxtime:double  |         |
|                                 | >>                |         |
| rawmsg                          | string            |         |
| icao24                          | string            |         |
| mintime                         | double            |         |
| maxtime                         | double            |         |
| msgcount                        | bigint            |         |
| subtypecode                     | tinyint           |         |
| unknowncapcode                  | boolean           |         |
| unknownopcode                   | boolean           |         |
| hasoperationaltcas              | smallint          |         |
| has1090esin                     | boolean           |         |
| supportsairreferencedvelocity   | smallint          |         |
| haslowtxpower                   | smallint          |         |
| supportstargetstatereport       | smallint          |         |
| supportstargetchangereport      | smallint          |         |
| hasuatin                        | boolean           |         |
| nacv                            | tinyint           |         |
| nicsupplementc                  | smallint          |         |
| hastcasresolutionadvisory       | boolean           |         |
| hasactiveidentswitch            | boolean           |         |
| usessingleantenna               | boolean           |         |
| systemdesignassurance           | tinyint           |         |
| gpsantennaoffset                | tinyint           |         |
| airplanelength                  | int               |         |
| airplanewidth                   | double            |         |
| version                         | tinyint           |         |
| nicsupplementa                  | boolean           |         |
| positionnac                     | double            |         |
| geometricverticalaccuracy       | int               |         |
| sourceintegritylevel            | tinyint           |         |
| barometricaltitudeintegritycode | smallint          |         |
| trackheadinginfo                | smallint          |         |
| horizontalreferencedirection    | boolean           |         |
| hour                            | int               |         |
+---------------------------------+-------------------+---------+
[hadoop-29:21000] > describe position_data4;
+--------------+-------------------+---------+
| name         | type              | comment |
+--------------+-------------------+---------+
| sensors      | array<struct<     |         |
|              |   serial:int,     |         |
|              |   mintime:double, |         |
|              |   maxtime:double  |         |
|              | >>                |         |
| rawmsg       | string            |         |
| mintime      | double            |         |
| maxtime      | double            |         |
| msgcount     | bigint            |         |
| icao24       | string            |         |
| nicsuppla    | boolean           |         |
| hcr          | double            |         |
| nic          | smallint          |         |
| survstatus   | smallint          |         |
| nicsupplb    | boolean           |         |
| odd          | boolean           |         |
| baroalt      | boolean           |         |
| lat          | double            |         |
| lon          | double            |         |
| alt          | double            |         |
| nicsupplc    | boolean           |         |
| groundspeed  | double            |         |
| gsresolution | double            |         |
| heading      | double            |         |
| timeflag     | boolean           |         |
| surface      | boolean           |         |
| hour         | int               |         |
+--------------+-------------------+---------+
[hadoop-29:21000] > describe rollcall_replies_data4;
+----------------------+-------------------+---------+
| name                 | type              | comment |
+----------------------+-------------------+---------+
| sensors              | array<struct<     |         |
|                      |   serial:int,     |         |
|                      |   mintime:double, |         |
|                      |   maxtime:double  |         |
|                      | >>                |         |
| rawmsg               | string            |         |
| mintime              | double            |         |
| maxtime              | double            |         |
| msgcount             | bigint            |         |
| icao24               | string            |         |
| message              | string            |         |
| isid                 | boolean           |         |
| flightstatus         | tinyint           |         |
| downlinkrequest      | tinyint           |         |
| utilitymsg           | tinyint           |         |
| interrogatorid       | tinyint           |         |
| identifierdesignator | tinyint           |         |
| valuecode            | smallint          |         |
| altitude             | double            |         |
| identity             | string            |         |
| hour                 | int               |         |
+----------------------+-------------------+---------+
[hadoop-29:21000] > describe sensor_visibility;
+--------------------+--------+---------+
| name               | type   | comment |
+--------------------+--------+---------+
| time               | double |         |
| sensorserialnumber | int    |         |
| icao24             | string |         |
| day                | int    |         |
+--------------------+--------+---------+
[hadoop-29:21000] > describe sensor_visibility_data3;
+--------------------+--------+---------+
| name               | type   | comment |
+--------------------+--------+---------+
| time               | double |         |
| sensorserialnumber | int    |         |
| icao24             | string |         |
| day                | int    |         |
+--------------------+--------+---------+
[hadoop-29:21000] > describe state_vectors;
+--------------------+---------+---------+
| name               | type    | comment |
+--------------------+---------+---------+
| time               | double  |         |
| icao24             | string  |         |
| lastpositionupdate | double  |         |
| lastvelocityupdate | double  |         |
| longitude          | double  |         |
| latitude           | double  |         |
| altitude           | double  |         |
| onground           | boolean |         |
| heading            | double  |         |
| verticalrate       | double  |         |
| velocity           | double  |         |
| callsign           | string  |         |
| day                | int     |         |
+--------------------+---------+---------+
[hadoop-29:21000] > describe state_vectors_data3;
+--------------------+---------+---------+
| name               | type    | comment |
+--------------------+---------+---------+
| time               | double  |         |
| icao24             | string  |         |
| lastpositionupdate | double  |         |
| lastvelocityupdate | double  |         |
| longitude          | double  |         |
| latitude           | double  |         |
| altitude           | double  |         |
| onground           | boolean |         |
| heading            | double  |         |
| verticalrate       | double  |         |
| velocity           | double  |         |
| callsign           | string  |         |
| day                | int     |         |
+--------------------+---------+---------+
[hadoop-29:21000] > describe state_vectors_data4;
+---------------+------------+-----------------------------+
| name          | type       | comment                     |
+---------------+------------+-----------------------------+
| time          | int        | Inferred from Parquet file. |
| icao24        | string     | Inferred from Parquet file. |
| lat           | double     | Inferred from Parquet file. |
| lon           | double     | Inferred from Parquet file. |
| velocity      | double     | Inferred from Parquet file. |
| heading       | double     | Inferred from Parquet file. |
| vertrate      | double     | Inferred from Parquet file. |
| callsign      | string     | Inferred from Parquet file. |
| onground      | boolean    | Inferred from Parquet file. |
| alert         | boolean    | Inferred from Parquet file. |
| spi           | boolean    | Inferred from Parquet file. |
| squawk        | string     | Inferred from Parquet file. |
| baroaltitude  | double     | Inferred from Parquet file. |
| geoaltitude   | double     | Inferred from Parquet file. |
| lastposupdate | double     | Inferred from Parquet file. |
| lastcontact   | double     | Inferred from Parquet file. |
| serials       | array<int> | Inferred from Parquet file. |
| hour          | int        |                             |
+---------------+------------+-----------------------------+
[hadoop-29:21000] > describe velocity_data4;
+---------------+-------------------+---------+
| name          | type              | comment |
+---------------+-------------------+---------+
| sensors       | array<struct<     |         |
|               |   serial:int,     |         |
|               |   mintime:double, |         |
|               |   maxtime:double  |         |
|               | >>                |         |
| rawmsg        | string            |         |
| mintime       | double            |         |
| maxtime       | double            |         |
| msgcount      | bigint            |         |
| icao24        | string            |         |
| supersonic    | boolean           |         |
| intentchange  | boolean           |         |
| ifrcapability | boolean           |         |
| nac           | smallint          |         |
| ewvelocity    | double            |         |
| nsvelocity    | double            |         |
| baro          | boolean           |         |
| vertrate      | double            |         |
| geominurbaro  | double            |         |
| heading       | double            |         |
| velocity      | double            |         |
| hour          | int               |         |
+---------------+-------------------+---------+
```
