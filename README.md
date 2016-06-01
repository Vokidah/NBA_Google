# NBA_Google

# run local
To run this program please go to the NBA_Google folder and type

python search.py

After that your program will run on localhost:5000 and you can search exact name and surname of a basketball player.

I get all players and their teams from nba.com only once when I run app. During the getting process I fill players array and team hash. 

In players array I save player name and his team. In team hash I save key - team name and a value - list of players indexes. 

Summary:

Player team search - O(log N) complexity and O(N) space

Team roster search - O(1) complexity and O(M * N) space , where M is a number of teams, and N is a number of players.

you can play with it on https://vokidah-nba.appspot.com
