import requests
import json
import csv

class club:
    #20 teams
    #name, fixture list: dict{'1': '[date, opposition, H/A], etc}
    #Init, skapa ett default lag
    def __init__(self):
    	self.club_name = 'default'
    	self.fixtures_dict = get_38_dictValues()

    #Genererar en dict på 20 värden
    def get_38_dictValues(self):
    	pass

    #Main, specificerar det tidigare default laget.
    def main(self, teamname, j_teamData):
    	#Ange lagets namn. Ange hela fixture dicten.
    	self.club_name = teamname
        #build fixtures_list
        for key in self.fixtures_dict.keys():
            self.fixtures_dict[key] = j_teamData[key]

    #write to file, name + kyes in fixtures_dict
    def prnt(self, csvfile):
        c_list = [self.club_name]
        for key in self.fixtures_dict.keys():
            c_list.append(key)
        with open(csvfile, 'a') as fout:
            wr = csv.writer(fout, quoting=csv.QUOTE_ALL)
            wr.writerow(c_list)

        d_list = [self.club_name]
        for value in self.fixtures_dict.values():
            d_list.append(value)
        with open(csvfile, 'a') as fout:
            wr = csv.writer(fout, quoting=csv.QUOTE_ALL)
            wr.writerow(d_list)

if __name__ == ('__main__'):
	#Gå igenom alla lag sidorna. Bygg object för varje lag. Placera objekt i dict. Output the dict to a .csv file
	
	for teamId in range(1, 21):
		newclub = club()	#initiate a new club
		res = requests.get('lag.html')	#get lagets html
		j_teamData = json.loads(res.text) #bygg ett jsonObject
		teamname = j_teamData.get['TeamValue...............']	#Ange lagets DictName
        newclub.main(teamname, j_teamData)
        newclub.prnt(csvfile)
   
#request team page
#json object on request
#Make empty list. Fill dict {json.'teamname': classObject
