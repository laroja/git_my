import requests
import json
import csv

class club:
    #20 teams
    #name, fixture list: dict{team: 'xxx', '1': '[date, opposition, H/A], etc}
    #Init, skapa ett default lag
    def __init__(self):
    	self.club_name = 'default'
    	self.fixtures_dict = get_20_dictValues()



    #Genererar en dict på 20 värden
    def get_20_dictValues(self):
    	pass

    #Main, specificerar det tidigare default laget.
    def main(self):
    	#Ange lagets namn. Ange hela fixture dicten.
    	pass



if __name__ == ('__main__'):
	#Gå igenom alla lag sidorna. Bygg object för varje lag. Placera objekt i dict. Output the dict to a .csv file
	teams_dict = {}
	for teamId in range(1, 21):
		newclub = club()	#initiate a new club

		res = requests.get('lag.html')	#get lagets html
		j_teamData = json.loads(res.text) #bygg ett jsonObject

		teamname = j_teamData.get['TeamValue...............']	#Ange lagets DictName
		teams_dict[teamname] = newclub.main() 	#bygg ett element i dict med club.main med j_teamData

	#Skriv ut teams_dict till en .csv, där varje rad motsvarar ett clubObject.

		
	


#request team page
#json object on request
#Make empty list. Fill dict {json.'teamname': classObject
