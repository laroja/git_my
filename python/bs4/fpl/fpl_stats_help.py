#fantasy player - file

f = requests.get('http://fantasy.premierleague.com/web/api/elements/1/')

#Build json object
jdata = json.loads(f.text)
#make json object easier to read
pprint.pprint(jdata)
#soup object - bs4
soup = BeautifulSoup(f.text)

#
