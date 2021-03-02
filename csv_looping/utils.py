import sys
import requests

def auth(password=None, url=None):
     host = f'https://{url}:5443/v2'
     print(f'Autenticating to: {host}')
     headers = {'content-type': 'application/x-www-form-urlencoded'}
     payload = f'grant_type=password&username=admin&password={password}'

     try:
             r = requests.post(host + '/token', headers=headers, data=payload, verify=False)
             r.raise_for_status()
     except requests.exceptions.Timeout as e:
             print('Connection timed out'.format(e))
             sys.exit(1)
     except requests.exceptions.ConnectionError as e:
             print('ERROR! Could not connect!')
             print(e)
             sys.exit(1)
     except requests.exceptions.HTTPError as e:
             print('ERROR! HTTP error')
             print(e)
             sys.exit(1)
     else:
             print(f'Status code: {r.status_code}')
             print(f'Response: {r.json()}')
             return r.json()

def make_request_v2(method, path, data=None, access_token=None):
        if access_token is None:
                login_result = auth(None)
                access_token = login_result['access_token']

        # click.echo(f'Got Access Token: {access_token}')

        new_path = path
        headers = {'Authorization': 'Bearer ' + access_token, 'content-type': 'application/json'}
        print(f'Connecting to {new_path}')
        try:
                r = requests.request(method, new_path, headers=headers, data=data, verify=False, timeout=10)
        except requests.exceptions.Timeout:
                print('Connection timed out')
                sys.exit(1)
        except requests.exceptions.ConnectionError as e:
                print('ERROR! Could not make_request_v2')
                print(e)
                sys.exit(1)
        else:
                return r

