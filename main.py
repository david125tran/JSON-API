import requests

#---------------------------------- Positionstack.com JSON REST API ----------------------------------
# We use the position stack API to make a free call to receive the latitude & longitude of an address.
# This data is returned in JSON format.

ps_url = "http://api.positionstack.com/v1/forward"
ps_auth_key = "249d1116075a0056a19aaad35feab23c"
ps_address = "New Brunswick, NJ 08901"
ps_params = {
    "access_key": ps_auth_key,
    "query": ps_address
}

# Send the API call
response = requests.get(url=ps_url, params=ps_params)
response.raise_for_status()         # Get the status code if attempt is unsuccessful to help with debugging
ps_data = response.json()

latitude = ps_data['data'][0]['latitude']
longitude = ps_data['data'][0]['longitude']

#---------------------------------- Sunrise-sunset.org JSON REST API ----------------------------------
# We then use those latitude/longitude coordinates to send an API request to sunrise-sunset.org API
# to get back the sunrise and sunset time of that location.

ss_url = "https://api.sunrise-sunset.org/json"
ss_params = {
    "lat": latitude,
    "long": longitude,
    "formatted": 0
}

response = requests.get(url=ss_url, params=ss_params)
response.raise_for_status()         # Get the status code if attempt is unsuccessful to help with debugging
ss_data = response.json()

# Transform the data to a date format of Hour:Minute:Second
sunrise = ss_data['results']['sunrise'].split("T")[1].split("+00:00")[0]
sunset = ss_data['results']['sunset'].split("T")[1].split("+00:00")[0]

# Return the result
print(f"Today at {ps_address}, the sun rose at {sunrise} and the sun will set at {sunset}")