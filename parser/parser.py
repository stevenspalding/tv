import json
import sys

def create_m3u8_playlist(json_file_path, output_m3u8_path):
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

    # Create M3U8 playlist
    m3u8_content = "#EXTM3U\n"

    for item in data:
        title = item.get('title', '')
        logo = item.get('logo', '')
        url = item.get('url', '')
        category = item.get('category', '')

        # Add entry to M3U8 playlist
        if title and url:
            m3u8_content += f"#EXTINF:-1 tvg-logo=\"{logo}\" group-title=\"{category}\",{title}\n{url}\n"

    # Write M3U8 playlist to file
    with open(output_m3u8_path, 'w') as m3u8_file:
        m3u8_file.write(m3u8_content)

    print(f"M3U8 playlist successfully created at '{output_m3u8_path}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python parser.py <input_json_file> <output_m3u8_file>")
    else:
        input_json_path = sys.argv[1]
        output_m3u8_path = sys.argv[2]
        create_m3u8_playlist(input_json_path, output_m3u8_path)
import json
import sys
