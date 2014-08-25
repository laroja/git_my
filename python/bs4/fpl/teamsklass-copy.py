import requests
import json
import csv

class club:
    #20 teams
    #name, fixture list: dict{'1': '[date, opposition, H/A], etc}
    #Init, skapa ett default lag
    def __init__(self, name, allfixtures):
    	self.club_name = name
    	self.fixtures = allfixtures 

    #write to file, name + kyes in fixtures_dict
    def prnt(self, csvfile):
        print('enter prnt')
        c_list = [self.club_name]
        for item in self.fixtures:
            c_list.append(item)
        with open(csvfile, 'a') as fout:
            wr = csv.writer(fout, quoting=csv.QUOTE_ALL)
            wr.writerow(c_list)
##
##        d_list = [self.club_name]
##        for item in self.fixtures:
##            d_list.append(item)
##        with open(csvfile, 'a') as fout:
##            wr = csv.writer(fout, quoting=csv.QUOTE_ALL)
##            wr.writerow(d_list)
        print('leaving prnt')

def build_full_fixture_list():
    print('enter build_full')
    #sök 1-600, Se om lag finns i dict.keys. Om inte, dict[key]='full fixture list'. retrn full dict
    team_fixt = {}
    team_list = []
    for nbr in range(1, 700):
        print('player: ', nbr)
        res = requests.get('http://fantasy.premierleague.com/web/api/elements/'+str(nbr)+'/')
        try:
            j_teamData = json.loads(res.text)
        except ValueError:
            print('Något stämmer ej')
        team = j_teamData.get('team_name')           
        if team not in team_fixt.keys():                                #Not yet found, build full fixture list of played and unplayed matches.
            fixtures = j_teamData.get('fixture_history').get('summary')
            fixt_list = j_teamData.get('fixtures').get('all')
            for item in fixt_list:
                fixtures.append(item)
            team_fixt[team] = fixtures
            team_list.append(team)
    print('leave build')
    return (team_fixt, team_list)

if __name__ == ('__main__'):
    #Gå igenom alla lag sidorna. Bygg object för varje lag. Placera objekt i dict. Output the dict to a .csv file
    print('enter main')
    team_tup = build_full_fixture_list()
    t_dict = team_tup[0]
    t_list = team_tup[1]
    allteams_dict = {}
    csvfile = 'teams_csv.csv'
    with open(csvfile, 'w') as fout:
        fout.write('')
    for name in t_list:
        print('enter main for')
        newclub = club(name, t_dict[name])	#initiate a new club	
        allteams_dict['name'] = newclub
        newclub.prnt(csvfile)
        print(name)

  
