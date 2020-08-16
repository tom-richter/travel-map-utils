import argparse
import xml.etree.ElementTree as ET

INTERVAL = 10

parser = argparse.ArgumentParser(
    description='Convert file to Travel-Map compatible route file')
parser.add_argument("file_path")
parser.add_argument("mode")

args = parser.parse_args()
mode = args.mode
root = ET.parse(args.file_path).getroot()

gpx_file = open("route.json", "w+")
gpx_file.write("[\n")

if mode == "garmin-gpx":
    i = 0
    while i < len(root[1][1]):
        waypoint = ('  { "lat": ' + root[1][1][i].get("lat")[:10] +
                    ', "lng": ' + root[1][1][i].get("lon")[:10] + ' },\n')
        gpx_file.write(waypoint)
        i += INTERVAL

if mode == "footpath-route-gpx":
    i = 1
    while i < len(root[1]):
        waypoint = ('  { "lat": ' + str(root[1][i].get("lat"))[:10] + 
                    ', "lng": ' + str(root[1][i].get("lon"))[:10] + ' },\n')
        gpx_file.write(waypoint)
        i += INTERVAL

gpx_file.write("]\n")
gpx_file.close()
