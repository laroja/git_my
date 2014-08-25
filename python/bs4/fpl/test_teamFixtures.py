import requests
import json


res = requests.get('http://fantasy.premierleague.com/web/api/elements/10/')
jdata = json.loads(res.text)

fixtures = jdata.get('fixture_history').get('summary')
fixt_list = jdata.get('fixtures').get('all')
for item in fixt_list:
    fixtures.append(item)



