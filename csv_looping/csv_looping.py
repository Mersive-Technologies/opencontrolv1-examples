import requests
import csv
import argparse
import socket
import json
import utils

parser = argparse.ArgumentParser(description='CSV variable CLI')
# parser.add_argument('--pwd',
#                    help='admin password')

args = parser.parse_args()

print('Starting ...')

with open('pods.csv', newline='') as csvfile:
    podreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in podreader:
        ip = row[' #IP Address'].strip()
        password = row['password']
        print(f'Starting update: {ip.strip()}')
        try:
            token_response = utils.auth(password, ip)
            # Do reverse lookup to get data
            fqdn = socket.gethostbyaddr(ip)
            print(f'Determined {ip} FQDN is {fqdn[0]}')
            print('Would do PATCH here')
            data = '{"connection": {"ethernet": {"ip_configuration":{"hostname": "' + fqdn[0] + '"}}}}'
            print(json.dumps(data))
            r = utils.make_request_v2('patch', f'https://{ip}:5443/v2/config', data, token_response["access_token"])
            print(r.json())
        except requests.exceptions.RequestException as e:
            print(f'Error! {e}')
