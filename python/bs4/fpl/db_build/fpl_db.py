import os
import requests
import json
import sqlite3



def make_db():
    conn = sqlite3.connect('player.db')
    print("opened db")
    conn.execute('''create table players(id int primary key,
    name text, age int);''')
    print("table created")
    conn.close()

def update_db(db, pl_dict):
    conn2 = sqlite3.connect(db)
    conn2.execute("insert into players(id,name,age) values(5,'Olof',22)")
    conn2.commit()
    print("records created")
    conn2.close()

if __name__ == ('__main__'):
    html = "http://fantasy.premierleague.com/web/api/elements/10/"
    re = requests.get(html)
    jdata = json.loads(re.text)

    pl_dict = {}

    for key in jdata.keys():
        pl_dict[key] = jdata.get(key)

    #make_db()
    update_db("player.db", pl_dict)
    
