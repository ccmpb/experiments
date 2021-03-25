import requests
from datetime import date
import json
from pprint import pprint

def leafsid():
    return "10"

def seasonend():
    return "2021-07-21"

def nextgame(num=1):
    url = "https://statsapi.web.nhl.com/api/v1/schedule?teamId={}&startDate={}&endDate={}"
    nextgame = [] 

    resp = requests.get(url.format(leafsid(), date.today(), seasonend()))
    data = resp.json()

    for i in range(num):
        nextgame.append(data["dates"][i]["games"][0])

    return nextgame

def standings():
    url = "https://statsapi.web.nhl.com/api/v1/standings/wildCardWithLeaders"
    resp = requests.get(url.format(leafsid()))
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

    ng = nextgame()
    for game in nextgame(5):
        print(formatgame(game))

    print(formatstandings(standings()))

if __name__ == "__main__":
    main()
