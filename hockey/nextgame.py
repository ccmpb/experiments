import requests
from datetime import date
import json
from pprint import pprint

def leafsid():
    return "10"

def seasonend():
    return "2021-05-21"

def nextgame():
    url = "https://statsapi.web.nhl.com/api/v1/schedule?teamId={}&startDate={}&endDate={}"
    resp = requests.get(url.format(leafsid(), date.today(), seasonend()))
    data = resp.json()
    nextgame = data["dates"][0]["games"][0]
    return nextgame

def main():
    ng = nextgame()
    teams =  ng["teams"]
    home = teams["home"]
    away = teams["away"]

    gamedate = ng["gameDate"]

    gameinfo = "{} ({}-{}-{}) @ {} ({}-{}-{}) {}"
    
    print(gameinfo.format(
        away["team"]["name"], 
        away["leagueRecord"]["wins"],
        away["leagueRecord"]["losses"],
        away["leagueRecord"]["ot"],
        home["team"]["name"],
        home["leagueRecord"]["wins"],
        home["leagueRecord"]["losses"],
        home["leagueRecord"]["ot"],
        gamedate,
    ))

if __name__ == "__main__":
    main()
