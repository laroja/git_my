import requests
import json


res = requests.get('http://fantasy.premierleague.com/web/api/elements/1/')

jdata = json.loads(res.text)

#lista över nycklar 
keys = ['assists', 'bonus', 'bps', 'clean_sheets', 'code', 'cost_change_event', 'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall', 'dreamteam_count', 'ea_index', 'element_type', 'ep_next', 'ep_this', 'event_explain', 'event_points', 'event_total', 'first_name', 'form', 'goals_conceded', 'goals_scored', 'id', 'minutes', 'now_cost', 'own_goals', 'penalties_missed', 'penalties_saved', 'points_per_game', 'red_cards', 'saves', 'second_name', 'selected_by', 'selected_by_percent', 'status', 'team', 'team_code', 'team_id', 'team_name', 'total_points', 'transfers_in', 'transfers_in_event', 'transfers_out', 'transfers_out_event', 'type_name', 'value_form', 'value_season', 'web_name', 'yellow_cards']

player_dict = {}

#Bygg ny dict med keys_listan och jdata-värdena
for key in keys:
    player_dict['key'] = jdata['key']

#För en spelare,skriv in header + dess värden till .csv fil
with open('fplcsv.csv', 'a') as f:
	w = csv.DictWriter(f, player_dict.keys())
	w.writeheader()
	w.writerow(player_dict)


#Att göra
#Ovan för alla spelare, loop.|ladda upp google docs|auto-uppdatera varje dag
#Bygg statistik från rådatan - script
#Visualisera det
