import requests
import csv
import argparse

parser = argparse.ArgumentParser(description='Reboot Pods CLI')
parser.add_argument('--pwd',
                    help='admin password')

args = parser.parse_args()

print('Starting pod reboot...')
url = '/api/control/reboot'
if (args.pwd):
    url = url + f'?password={args.pwd}'

with open('pods.csv', newline='') as csvfile:
    podreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in podreader:
        ip = row[' #IP Address']
        print(f'Rebooting {ip.strip()}{url}')
        try:
            requests.get(f'http://{ip.strip()}{url}', timeout=20)
        except:
            continue
