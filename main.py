import players_and_teams as p
from flask import Flask, request, redirect, render_template
app = Flask(__name__)

_players, _teams = p.fetch_players()

@app.route('/', methods=['GET', 'POST'])
@app.route('/players', methods=['GET', 'POST'])
def players_search():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        team_name = str(request.form['search']).lower()
        if team_name in _teams:
            roster = p.get_team_roster(_teams[team_name], _players)
            return render_template('roster.html', team=team_name.title(), roster=roster)
        if ' ' in request.form['search']:
            name = str(request.form['search']).lower()
            name = name.split()
            name = "%s, %s" % (name[0], name[1])
            print(name)
            team = p.search_player(name, _players, 0 , len(_players) - 1)
            if team:
                team_name = team.lower()
                roster = p.get_team_roster(_teams[team_name], _players)
                return render_template('roster.html', team=team, roster=roster, searched_player=name.title().split(', '))
            else:
                name = name.split(', ')
                name = "%s, %s"%(name[1], name[0])
                print(name)
                team = p.search_player(name, _players, 0 , len(_players) - 1)
                if team:
                    team_name = team.lower()
                    roster = p.get_team_roster(_teams[team_name], _players)
                    print(roster)
                    return render_template('roster.html', team=team, roster=roster, searched_player=name.title().split(', '))
        return "NOT FOUND"





