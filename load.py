import json, requests


def download_players():
    r = requests.get('http://stats.nba.com/stats/commonallplayers/?LeagueID=00&Season=2015-16&IsOnlyCurrentSeason=0')
    f = open('workfile', 'w')
    if r.status_code == 200:
        for each in json.loads(r.text)['resultSets'][0]['rowSet']:
            if ', ' in each[1]:
                surname_name = each[1].split(', ')
                surname_name = "%s, %s"%(surname_name[0], surname_name[1])
            else:
                surname_name = "%s,  "%each[1]
            if each[-2]:
                team = "%s %s" % (each[8], each[9])
            else:
                team = "Former Player"
            player_str = "%s|%s" % (surname_name, team)
            f.write("%s\n"%player_str)
    else:
        r.raise_for_status()
download_players()