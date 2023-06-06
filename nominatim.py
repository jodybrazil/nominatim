import sys
import csv
import requests
from urllib.parse import quote


def search_address(address):
    encoded_address = quote(address)
    url = f"https://nominatim.openstreetmap.org/search?q={encoded_address}&format=json"
    response = requests.get(url)
    data = response.json()

    if data:
        place_id = data[0].get("place_id", "")
        osm_id = data[0].get("osm_id", "")
        return place_id, osm_id
    else:
        return "", ""


def process_addresses(input_file, output_file):
    with open(input_file, "r", newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        header = next(reader)  # Get the header row

        with open(output_file, "w", newline="") as output_csv:
            writer = csv.writer(output_csv, delimiter=";")
            writer.writerow(header + ["Place ID", "OSM ID"])  # Write header row

            for row in reader:
                address = row[0]
                place_id, osm_id = search_address(address)
                writer.writerow(row + [place_id, osm_id])  # Write output row

    print(f"Processed addresses saved to {output_file}.")


# Usage example
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python address_search.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        process_addresses(input_file, output_file)
