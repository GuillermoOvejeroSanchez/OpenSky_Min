# OpenSky Api

## Modelos de los datos de respuesta

- StateVector
- Flight
- Tracks
- Path
- Airport
- Position

## Impala Shell (Traffic)

Acceder a la Shell

```bash
ssh -p 2230 -l USERNAME data.opensky-network.org
```

Guardar salida de la shell en un fichero

```bash
script -f -c "ssh -p 2230 -l USERNAME data.opensky-network.org" log.txt
```

Transformar salida de la Shell en un CSV para poder analizarlo

```bash
cat log.txt | grep "^|.*" | sed -e 's/\s*|\s*/,/g' -e 's/^,\|,$//g' -e 's/NULL//g' | awk '!seen[$0]++' >> log.csv
```

Vuelo aletorio del dia 16 de Mayo de 2021

```sql
SELECT * FROM state_vectors_data4 WHERE hour=unix_timestamp('2021-05-16 12:00:00') ORDER BY rand() LIMIT 1;
```

- Spain coordinates: (-9.39288367353, 35.946850084, 3.03948408368, 43.7483377142) Obtained from [Github Gist](https://gist.github.com/graydon/11198540)

Distintos vuelos para la delimitacion de España

```sql
SELECT COUNT(DISTINCT icao24) FROM state_vectors_data4 WHERE lat<=43.74 AND lat>=35.94 AND lon<=3.03 AND lon>=-9.39 AND hour>=unix_timestamp('2021-05-07 01:00:00') and hour<=unix_timestamp('2021-05-09 23:00:00');
```

```sql
SELECT COUNT(DISTINCT icao24)
FROM state_vectors_data4
WHERE lat<=43.74 AND lat>=35.94
AND lon<=3.03 AND lon>=-9.39
AND hour>=unix_timestamp('2021-05-14 01:00:00')
AND hour<=unix_timestamp('2021-05-16 23:00:00');
```

```sql
SELECT COUNT(1) FROM state_vectors_data4 WHERE lat<=43.74 AND lat>=35.94 AND lon<=3.03 AND lon>=-9.39 AND hour>=unix_timestamp('2021-05-10 12:00:00');
```

Numero de Vuelos con Salida/Llegada al aeropuerto LEMD(Barajas)

```sql
SELECT callsign,f.estdepartureairport,f.estarrivalairport,COUNT(callsign) FROM flights_data4 f WHERE (f.estdepartureairport = 'LEMD' or f.estarrivalairport = 'LEMD') and f.day>=unix_timestamp('2021-05-10 00:00:00') group by callsign,f.estdepartureairport,f.estarrivalairport ORDER BY COUNT(callsign);
```

Obtenga 1 posición (la última) por avión cada minuto

```sql
SELECT * FROM state_vectors_data4 v JOIN (SELECT QUOTIENT(time, 60) AS minute, MAX(time) AS recent, icao24 FROM state_vectors_data4 WHERE hour=1480762800 GROUP BY icao24, minute) AS m ON v.icao24=m.icao24 AND v.time=m.recent WHERE v.hour=1480762800;
```

```sql
SELECT count(1) FROM state_vectors_data4 v JOIN (SELECT QUOTIENT(time, 60) AS minute, MAX(time) AS recent, icao24 FROM state_vectors_data4 WHERE hour>=unix_timestamp('2021-05-14 12:00:00') GROUP BY icao24, minute) AS m ON v.icao24=m.icao24 AND v.time=m.recent WHERE v.hour>=unix_timestamp('2021-05-14 12:00:00') and v.hour<=unix_timestamp('2021-05-15 12:00:00') and lat<=43.74 AND lat>=35.94 AND lon<=3.03 AND lon>=-9.39;
```
