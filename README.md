# Nominatim lookup

A test project to do address lookups and retrieve a list of OpenStreetMap IDs (osm_id) to uniquely identify an address. See more details here [https://nominatim.org/release-docs/develop/api/Output/#notes-on-field-values]. OSM Objects must always be referred to both with their object ids and their respective object type (node, way, relation). To create a unique id for each address, we should use osm_type + osm_id.

Other alternatives to consider:

- osm_type + osm_id
- osm_type + osm_id + class
- lat + lon

## Setup

Setup python environment

```sh
python3 -m venv venv
```

Install requirements

```sh
source venv/bin/activate
pip install -r requirements-dev.txt
```

## Run

This uses a local CSV file with a single column of addresses to lookup and then creates a CSV file with the addresses and new columns with the OSM type, OSM ID, and UniqueID which is a combination of type and id separated with an underscore ("_").

NOTE: the delimiter is a semicolon (;) for the CSV to allow commas to be used in the address.

```sh
python nominatim.py <input_file> <output_file>
```

for example:

```sh
python nominatim.py addresses.csv output.csv
```
