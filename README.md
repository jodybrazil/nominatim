# Nominatim lookup

A test project to do address lookups and retrieve a list of OSM IDs to uniquely identify an address.

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

This uses a local CSV file with addresses to lookup and then creates a CSV file with the addresses and a new column with the OSM ID.

```sh
python nominatim.py -f addresses.csv
```
