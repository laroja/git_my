import requests
import json
import csv

#return a requests object
def get_playerRequest(web_name, id):
    http = web_name + str(id) + "/"
    response = requests.get(http)
    return response

#return a json object
def get_jsonObject(res):
    global jdata
    try:
        jdata = json.loads(res.text)
    except ValueError:
        print('Något stämmer ej')
    return jdata

#lista över nycklar 
# def get_playerKeys():
#     keys_list = [ 'team', 'first_name', 'second_name', 'total_points', 'minutes',  'assists', 'bonus', 'bps', 'clean_sheets', 'points_per_game', 'selected_by_percent', 'goals_conceded', 'goals_scored', 'cost_change_event', 'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall', 'status', 'ep_this', 'event_explain', 'event_points', 'event_total', 'form', 'dreamteam_count', 'ea_index', 'element_type', 'ep_next', 'id', 'own_goals', 'penalties_missed', 'penalties_saved', 'yellow_cards', 'red_cards', 'saves', 'selected_by', 'now_cost', 'transfers_in', 'transfers_in_event', 'transfers_out', 'transfers_out_event', 'type_name', 'value_form', 'value_season', 'web_name', 'code', 'team_code', 'team_id', 'team_name']
#     return keys_list

def prnt_csvHeader(csvfile, mode, pkeys_list):
    header_dict = {}
    #build dict with header terms
    for item in pkeys_list:
        header_dict[item] = 'none'
    #write header_dict to file
    with open(csvfile, mode) as fout:
        w = csv.DictWriter(fout, header_dict.keys())
        w.writeheader()

#Bygg ny dict med keys_listan och jdata-värdena
def get_playerDict(player_dict, jdata, pkeys_list):
    for key in pkeys_list:
        player_dict[key] = jdata[key]
    return player_dict

#För en spelare,skriv in header + dess värden till .csv fil
def prnt_csvPlayer(csvfile, mode, player_dict):
    with open(csvfile, 'a') as fout:
        w = csv.DictWriter(fout, player_dict.keys())
        w.writerow(player_dict)
#Att göra
#ladda upp google docs|auto-uppdatera varje dag
#Bygg statistik från rådatan - script
#Visualisera det
##
###Statistik
##class player:
##    def __init__(self, player_dict)
##
##        





if __name__ == ('__main__'):
    web_name = 'http://fantasy.premierleague.com/web/api/elements/'
    csvfile = 'fplcsv.csv'
    pkeys_list = ['team', 'first_name', 'second_name', 'total_points', 'minutes',  'assists', 'bonus', 'bps', 'clean_sheets', 'points_per_game', 'selected_by_percent', 'goals_conceded', 'goals_scored', 'cost_change_event', 'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall', 'status', 'ep_this', 'event_explain', 'event_points', 'event_total', 'form', 'dreamteam_count', 'ea_index', 'element_type', 'ep_next', 'id', 'own_goals', 'penalties_missed', 'penalties_saved', 'yellow_cards', 'red_cards', 'saves', 'selected_by', 'now_cost', 'transfers_in', 'transfers_in_event', 'transfers_out', 'transfers_out_event', 'type_name', 'value_form', 'value_season', 'web_name', 'code', 'team_code', 'team_id', 'team_name']
    #empty .csv file. Add a header.
    prnt_csvHeader(csvfile, 'w', pkeys_list)
    #Parse 600ish player objects
    for id in range(1, 600):
        player_dict = {}
        #get player request
        res = get_playerRequest(web_name, id)
        #get json object
        jdata = get_jsonObject(res)
        #get a full player_dict
        player_dict = get_playerDict(player_dict, jdata, pkeys_list)

        #For player, write values to .csv file
        prnt_csvPlayer(csvfile, 'a', player_dict)
        print("player"+str(id))
    
