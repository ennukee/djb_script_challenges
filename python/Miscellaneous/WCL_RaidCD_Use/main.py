import requests as r
import datetime
import json

class WCL:
    def __init__(self):
        self.api_keys = {'public': '3f7e2d601f40b4a08e4e397680a03fa1'}
        self.WCL_base = 'https://www.warcraftlogs.com:443/v1/'
        self.valid_spell_ids = {
            'major': [740, 115310, 31821, 64843, 62618, 108280, 98008, 207946],
            'minor': [108281, 198838, 97462, 114049, 31884],
            'personal': [157153, 105809, 33891]
        }
        self.id_to_spell = {
            740: 'Tranquility',
            115310: 'Revival',
            31821: 'Aura Mastery',
            64843: 'Divine Hymn',
            62618: 'Power Word: Barrier',
            108280: 'Healing Tide Totem',
            108281: 'Ancestral Guidance',
            157153: 'Cloudburst Totem',
            198838: 'Earthen Shield Totem',
            98008: 'Spirit Link Totem',
            97462: 'Commanding Shout',
            114049: 'Ascendance',
            31884: 'Avenging Wrath',
            105809: 'Holy Avenger',
            33891: 'Incarnation: Tree of Life',
            207946: 'Light\'s Wrath'
        }

    def cur_time(self):
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

    def parse_length(self, length):
        # Assumes length in milliseconds
        length //= 1000
        return '{0:01d}:{1:02d}'.format(length//60, length%60)

    def generate_filter(self, **kwargs):
        major = kwargs.get('major', True)
        minor = kwargs.get('minor', False)
        personal = kwargs.get('personal', False)

        considered_ids = []
        for key in kwargs.keys():
            if key in self.valid_spell_ids.keys():
                if kwargs[key] == True:
                    considered_ids.extend(self.valid_spell_ids[key])

        return 'type="cast" and ({})'.format(' or '.join(map(lambda i: "ability.id={}".format(i), considered_ids)))

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
            inp = input('Pick a fight: ')
            try:
                v = int(inp)
                fights[v]['id'] # Throws an exception if out of bounds
                return v
            except Exception as e:
                print('Something went wrong, please select again!')



    def parse_fight(self, code, fights, f_id, **_):
        s, e = fights[f_id]['start_time'], fights[f_id]['end_time']

        endpoint_extension = 'report/events/' + code
        wcl_filter = self.generate_filter(**_)
        req = self.make_request(endpoint_extension, start = s, end = e, filter=wcl_filter)

        json_req = json.loads(req.text)['events']
        json_req = [x for x in json_req if x['classResources'][0]['max'] >= 1100000]

        st_output = []
        for spell in json_req:
            spell_id = spell['ability']['guid']
            st = '{} used at {}'
            st = st.format(self.id_to_spell[spell_id], self.parse_length(spell['timestamp'] - s))
            st_output.append(st)
        print('\n'.join(st_output))

    def get_log_id(self):
        print('The ID for a WarcraftLogs report can be seen in the URL. https://wcl.com/reports/THIS_IS_THE_ID.')
        log_id = input('Please enter a WarcraftLogs report ID: ').strip()

        head_req = r.head(self.WCL_base + 'report/fights/' + log_id, params={'api_key': self.api_keys['public']})
        if str(head_req.status_code) != '200':
            print('Invalid log ID. Please try again.\n')
            return self.get_log_id()
        else:
            return log_id


def main(c, log_id = None):
    # Get the fight data for a report
    print('-----------------------------')
    if not log_id:
        log_id = c.get_log_id()
    else:
        print('Pre-loaded log_id {} recognized'.format(log_id))
    print('-----------------------------')
    r = c.report_fights(log_id)
    f_id = c.choose_fight(r['fights'])
    print('-----------------------------')
    c.parse_fight(log_id, r['fights'], f_id, major = True, minor = True, personal = False)

if __name__ == '__main__':
    main(WCL())
