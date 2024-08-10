import json
from operator import itemgetter

import json
import sys

def sort_json_playlist(json_file_path, output_json_path):
    try:
        # Read JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in '{json_file_path}'. Make sure it is a valid JSON file.")
        return

    # Sort based on the 'category' key
    sorted_data = json.dumps(sorted(data, key=itemgetter('category')))
 
    # Write M3U8 playlist to file
    with open(output_json_path, 'w') as m3u8_file:
        m3u8_file.write(sorted_data)

    print(f"M3U8 playlist successfully created at '{output_json_path}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sorter.py <input_json_file> <output_m3u8_file>")
    else:
        input_json_path = sys.argv[1]
        output_json_path = sys.argv[2]
        sort_json_playlist(input_json_path, output_json_path)
