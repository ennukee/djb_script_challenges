import requests as r
import datetime
import json

class WCL:
    def __init__(self):
        self.api_keys = {'public': '3f7e2d601f40b4a08e4e397680a03fa1'}
        self.WCL_base = 'https://www.warcraftlogs.com:443/v1/'
        self.valid_spell_ids = {
            'major': [],
            'minor': [],
            'personal': []
        }

    def cur_time(self):
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

    def parse_length(self, length):
        # Assumes length in milliseconds
        length //= 1000
        return '{0:01d}:{1:02d}'.format(length//60, length%60)

    def make_request(self, ext, **kwargs):
        payload = {'api_key': self.api_keys['public'], 'translate': kwargs.get('translate', 'true')}
        payload.update(kwargs)

        url = self.WCL_base + ext
        return r.get(url, params = payload)

    def report_fights(self, code, **kwargs):
        endpoint_extension = 'report/fights/' + code
        only_bosses = kwargs.get('boss_only', True)

        req = self.make_request(endpoint_extension)

        data = json.loads(req.text)

        fights = data['fights']
        if only_bosses:
            fights = list(filter(lambda f: f['boss'] != 0, fights))
        output = {'start': data['start'], 'end': data['end'], 'fights': fights}

        # The indices in the 'fights' key have the following keys / format
        #   "lastPhaseForPercentageDisplay": 0,
        #   "partial": 2,
        #   "fightPercentage": 722,
        #   "id": 19,
        #   "bossPercentage": 722,
        #   "name": "Krosus",
        #   "kill": false,
        #   "end_time": 4502553,
        #   "start_time": 4249019,
        #   "difficulty": 4,
        #   "boss": 1842,
        #   "size": 30

        return output

    def choose_fight(self, fights):
        print('-- Select which of the following fights to analyze --')
        for f in range(len(fights)):
            s = '{} - [{}] {} {} ({})'
            fight = fights[f]

            length = (fight['end_time'] - fight['start_time'])
            length = self.parse_length(length)
            diff = {2: 'LFR', 3: 'N', 4: 'H', 5: 'M'}.get(fight['difficulty'], '???')
            s = s.format(f, diff, fight['name'], 'Kill' if fight['kill'] else 'Wipe', length)
            if not fight['kill']:
                s += ' {}%'.format(fight['bossPercentage']/100)

            print(s)

        while True:
            inp = input('')
            try:
                v = int(inp)
                fights[v]['id'] # Throws an exception if out of bounds
                return v
            except Exception as e:
                print('Something went wrong, please select again!')

    def parse_fight(self, code, fights, f_id):
        s, e = fights[f_id]['start_time'], fights[f_id]['end_time']

        endpoint_extension = 'report/events/' + code
        req = self.make_request(endpoint_extension, start = s, end = e, filter="")

        json_req = json.loads(req.text)
        with open('output.json', 'w') as f:
            json.dump(json_req, f, indent=2)

def main(c):
    # Get the fight data for a report
    log_id = 'wvygjVx1d4QqRCDK'
    r = c.report_fights(log_id)
    f_id = c.choose_fight(r['fights'])
    c.parse_fight(log_id, r['fights'], f_id)

if __name__ == '__main__':
    main(WCL())
