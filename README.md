# Nominatim lookup

A test project to do address lookups and retrieve a list of OpenStreetMap IDs and Nominatim Place IDs to uniquely identify an address. Either can be used to uniquely identify a location. Storing both seems redundant for this putpose but seems valuable until it can be determined which will serve as a better ID.

## Details about Place ID and OpenStreetMap ID

The place_id and osm_id are identifiers associated with specific geographic locations, but they serve different purposes and come from different sources.

Place ID: The place_id is an identifier used by the Nominatim geocoding service. It is specific to the Nominatim database and is assigned to each unique place or location within that database. Place IDs are useful for retrieving additional details or performing further queries related to a particular place in the Nominatim database.

OSM ID: The osm_id (OpenStreetMap ID) is an identifier used in the OpenStreetMap project, which is a collaborative mapping project that creates and provides free geographic data. The osm_id uniquely identifies an object (such as a node, way, or relation) within the OpenStreetMap database. It is widely used to reference and access the associated geographic data stored in OpenStreetMap.

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

This uses a local CSV file with a single column of addresses to lookup and then creates a CSV file with the addresses and a new column with the OSM ID.

NOTE: the delimiter is a semicolon (;) for the CSV to allow commas to be used in the address.

```sh
python nominatim.py <input_file> <output_file>
```

for example:

```sh
python nominatim.py addresses.csv output.csv
```
