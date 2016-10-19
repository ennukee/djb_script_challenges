import urllib.request
import requests
import json

wl_base = "https://www.warcraftlogs.com:443/v1/"
wl_api_key = '3f7e2d601f40b4a08e4e397680a03fa1'

def fights(fight_id):
  url = wl_base + "report/fights/" + fight_id
  params = dict(
                  api_key=wl_api_key
                )
  resp = requests.get(url=url, params=params)
  if resp.status_code == 200:
    with open('./{}_fight.json'.format(fight_id), 'w') as f:
      t = json.loads(resp.text)
      f.write(json.dumps(t, indent=2))
    print('Outputted to {}_fight.json'.format(fight_id))
  else:
    print('Invalid response code')

def events(fight_id, start = 0):
  url = wl_base + "report/events/" + fight_id
  params = dict(
                  api_key=wl_api_key,
                  start=start,
                  end=start + (15 * 1000)
                )
  resp = requests.get(url=url, params=params)
  if resp.status_code == 200:
    with open('./{}_events.json'.format(fight_id), 'w') as f:
      t = json.loads(resp.text)
      f.write(json.dumps(t, indent=2))
    print('Outputted to {}_events.json'.format(fight_id))
  else:
    print('Invalid response code')


if __name__ == '__main__':
  events('Gzj9CZTxvkAQWD1g', 844643)
