# Link Our Teachers

Aus dem Ursprünglichen [AXA7FHEN_cleaned.csv](AXA7FHEN_cleaned.csv) wurde ein gesäuberter und normalisierter SQL Dump [dump-datahack-202505161457.sql](dump-datahack-202505161457.sql) erstellt.

Mithilfe des [makettl.py](makettl.py) Skript wurde aus dem SQL ein TTL erstellt. ([zusammenfassung_output.ttl](zusammenfassung_output.ttl))

Das TTL kann mit GraphDB eingesehen und Visualisiert werden.
Mithilfe des [cities_lat_long.sql](cities_lat_long.sql) Skript konnte in kombination mit https://github.com/dr5hn/countries-states-cities-database.git ein CSV erstellt werden.
Das CSV mit den Orten kann dann mit QGIS verwendet werden um eine Heatmap zu erstellen.