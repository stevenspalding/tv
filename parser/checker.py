#github.com/vladlonov/iptv_checker
print("IPTV Checker\n\n")
import threading,time,sys
try:
    import json
    import sys
    from operator import itemgetter
    import requests
except:
    print("Please install requests module!")
    sys.exit()

worked = []

def check_json_playlist(json_file_path, output_json_path):
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

    
    totel_items = len(data)
    
    print("Scanning {} lists... Worked will write in {}".format(totel_items, output_json_path))
    # time.sleep(5) 

    for item in data:
        # threading.Thread(target=check,args=(item,)).start()
        check(item)


    # Write M3U8 playlist to file
    with open(output_json_path, 'w') as m3u8_file:
        # m3u8_file.write(worked)
        json.dump(worked, m3u8_file)

    print("Worked: {}/{}".format(len(worked), totel_items))
    print(f"JSON playlist successfully created at '{output_json_path}'.")

def check(item):
    global worked

    url = item['url']

    print("Checking "+ url +"...")
        
    try:
        req=str(requests.get(url, timeout=(2,5)).status_code)
        if req == "200" or (req == "302"):
            print("OK. " + url)
            worked.append(item)
            
    except:
        print("ERROR. " + url)
            
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sorter.py <input_json_file> <output_json_file>")
    else:
        input_json_path = sys.argv[1]
        output_json_path = sys.argv[2]
        check_json_playlist(input_json_path, output_json_path)

