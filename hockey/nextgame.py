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

def formatgame(game):
        teams =  game["teams"]
        home = teams["home"]
        away = teams["away"]
        gamedate = game["gameDate"]

        gameinfo = "{} ({}-{}-{}) @ {} ({}-{}-{}) {}"
    
        return gameinfo.format(
            away["team"]["name"], 
            away["leagueRecord"]["wins"],
            away["leagueRecord"]["losses"],
            away["leagueRecord"]["ot"],
            home["team"]["name"],
            home["leagueRecord"]["wins"],
            home["leagueRecord"]["losses"],
            home["leagueRecord"]["ot"],
            gamedate,
        )

def main():

    ng = nextgame()
    for game in nextgame(1):
        print(formatgame(game))

if __name__ == "__main__":
    main()
