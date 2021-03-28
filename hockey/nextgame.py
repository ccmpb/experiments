import requests
import datetime 
from datetime import date
import json
from pprint import pprint
from rich.console import Console
from rich.table import Table

class NHLApi:
    def __init__(self, url,  params):
        self.url = url
        self.params = params
        self.data = None 

        pprint(self.url)
        pprint(self.params)
    
    def fetch(self):
        resp = requests.get(self.url.format(*self.params))
        self.data = resp.json()


class Schedule(NHLApi):
    def __init__(self, teamid=None, start=None, end=None):
        if not teamid:
            teamid = defaultteam()
        if not start:
            start = date.today()
        if not end:
            end = seasonend()
        
        url = "https://statsapi.web.nhl.com/api/v1/schedule?teamId={}&startDate={}&endDate={}"
        params = [ teamid, start, end]

        super().__init__(url, params)

        self.fetch()

    def show(self):
        table = Table(title="Schedule")
        table.add_column("Date")
        table.add_column("Matchup")

        for date in self.data["dates"]:
            game = Game(date["games"][0])
            matchup = "{} @ {}" 
            away = game.awayteam()
            home = game.hometeam()
            
            table.add_row(
                game.date(),
                matchup.format(away, home)
            )

        console = Console()
        console.print(table)

class Game:
    def __init__(self, data):
        self.data = data
        pass
    
    def date(self):
        gametime = datetime.datetime.strptime(self.data["gameDate"], "%Y-%m-%dT%XZ")
        return gametime.strftime("%x %X")
    
    def hometeam(self):
        team = Team(self.data["teams"]["home"])
        return team

    def awayteam(self):
        team = Team(self.data["teams"]["away"])
        return team


class Team:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        team = "{} ({}-{}-{})"
        return team.format(
            self.data["team"]["name"],
            self.data["leagueRecord"]["wins"],
            self.data["leagueRecord"]["losses"],
            self.data["leagueRecord"]["ot"],
        )

class TeamStats(NHLApi):
    def __init__(self, teamid=None):
        if not teamid:
            teamid = defaultteam()

        url = "https://statsapi.web.nhl.com/api/v1/teams/{}/stats"
        params = [ teamid ]

        super().__init__(url, params)

        self.fetch()
    
    def show(self):
        pprint(self.data)


def defaultteam():
    return "10"

def seasonend():
    return "2021-07-21"

def nextgame(num=1):
    url = "https://statsapi.web.nhl.com/api/v1/schedule?teamId={}&startDate={}&endDate={}"
    nextgame = [] 

    resp = requests.get(url.format(defaultteam(), date.today(), seasonend()))
    data = resp.json()

    for i in range(num):
        nextgame.append(data["dates"][i]["games"][0])

    return nextgame

def standings():
    url = "https://statsapi.web.nhl.com/api/v1/standings/wildCardWithLeaders"
    resp = requests.get(url.format(defaultteam()))
    data = resp.json()
    return data

def formatstandings(standings):
    for record in standings["records"]:
        print(record["division"]["name"]) 
        for team in record["teamRecords"]:
            print(formatteam(team))
        print()

def formatteam(team):
    t = "{} ({}-{}-{})"
    return t.format(
        team["team"]["name"],
        team["leagueRecord"]["wins"],
        team["leagueRecord"]["losses"],
        team["leagueRecord"]["ot"],
    )

def formatgame(game):
    teams =  game["teams"]
    home = teams["home"]
    away = teams["away"]
    gamedate = game["gameDate"]

    gameinfo = "{} @ {} {}"

    return gameinfo.format(
        formatteam(away),
        formatteam(home),
        gamedate,
    )

def main():
    # printschedule(schedule(defaultteam()))
    sched = Schedule()
    sched.show()

    ts = TeamStats()
    ts.show()
    
    # ng = nextgame()
    # for game in nextgame(5):
    #     print(formatgame(game))
    #
    # print(formatstandings(standings()))

if __name__ == "__main__":
    main()
