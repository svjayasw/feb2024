import requests
import json
import argparse

def ftch_from_api():
    api_u = "https://www.travel-advisory.info/api"   #used the api given in doc file
    response = requests.get(api_u)
    return response.json()

#below we will save the api data to data.json file
def sve_file(data, filename="data.json"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def ld_file(filename="data.json"):
    with open(filename, 'r') as file:
        return json.load(file)

def lookup_for_country_name(country_code, data):
    country_info = data.get('data', {}).get(country_code, {})
    return country_info.get('name', f"Country code '{country_code}' not found.")

def main():
    parser = argparse.ArgumentParser(description="Country Lookup CLI")
    parser.add_argument("--countryCodes", nargs='+', help="county codes to look up")

    args = parser.parse_args()

    if not args.countryCodes:
        print("Please give at least one county code")
        return

    # Uncomment below to fetch data from the API
    data = ftch_from_api()

    # Comment   if using the real API
   # data = ld_file()

    #sve_file(data)  # Save 
#based on below for loop , we will get the needed output of country name
    for country_code in args.countryCodes:
        country_name = lookup_for_country_name(country_code, data)
        print(f"{country_code}: {country_name}")

if __name__ == "__main__":
    main()
             
