import json
import sys

"""
Looking for "dailyprogrammerfun"
"""

def find_json_location_str(jsoninput, searchval):
    if not isinstance(jsoninput, dict) and not isinstance(jsoninput, list):
        return []
    for key, value in jsoninput.items() if isinstance(jsoninput, dict) \
        else enumerate(jsoninput):
        if value == searchval:
            return [key]
        next_result = find_json_location_str(value, searchval)
        if next_result:
            return [key] + next_result
    return []

def main():
    jsoninput = json.load(open(sys.argv[1]))
    searchval = sys.argv[2]
    location = find_json_location_str(jsoninput, searchval)
    print(' -> '.join(map(str,location)))

if __name__ == "__main__":
    main()
