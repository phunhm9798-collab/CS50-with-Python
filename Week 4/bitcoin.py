# Import the necessary modules
import sys
import json
from sys import argv, exit
import requests

# Get the information from Coincap
# Replace 'YourAPIkey" with the one that you got from Coincap
try:
    response = requests.get(
        'https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourAPIkey')
except requests.RequestException:
    sys.exit("There was an exception while handling the api request")

# Slices the data to get the wanted value
response_json = response.json()
price = float(response_json['data']['priceUsd'])

# Define a loop that check the command line argument
if len(sys.argv) != 2:
    exit('Missing command-line argument')
else:
    try:
        number = float(argv[1])
    except:
        exit('Command-line argument is not a number')

# Output the bitcoin price
print(f'${price * number:,.4f}')
