def fetch_players():
    players = []
    teams = {}
    i = 0
    f = open('workfile', 'r')
    for each in f:
        info, team_name = each[:-1].split('|')
        players.append((info, team_name))
        team_name = team_name.lower()
        if team_name in teams:
            teams[team_name].append(i)
        else:
            teams[team_name] = [i]
        i += 1
    f.close()
    return players, teams

def search_player(name, players, l, r):
    index = int((l + r) / 2)
    if l > r:
        return None
    if name == players[index][0].lower():
        print(name, players[index][0].lower())
        return players[index][1]
    elif name > players[index][0].lower():
        print(name, players[index][0].lower())
        return search_player(name, players, index + 1, r)
    else:
        return search_player(name, players, l, index - 1)


def get_team_roster(indexes, players):
    roster = []
    for i in indexes:
        player = players[i][0].split(', ')
        roster.append(player)
    return roster