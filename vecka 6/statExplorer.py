import requests # type: ignore
import json


def getSeason(season):
    r = requests.get(f"http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/{season}")
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print("ERROR: season not found")
        exit()

def getGameday(season, day):
    r = requests.get(f"http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/{season}/{day}")
    if r.status_code == 200:
       return json.loads(r.text)
    else:
        print("ERROR: Gameday not found")
        exit()


def getExactScore():
    season = int(input("Year: "))
    homeScore=int(input("Home score: "))
    awayScore=int(input("Away score: "))
    matches = []
    seasonDict = getSeason(season)
    gameMatches=0

    gamedays = seasonDict["gamedays"]

    for day in gamedays:
        gamedayDict = getGameday(season, day)
        games = gamedayDict["games"]
        matchingGames = []
        for game in games:
            if game["score"]["home"]["goals"] ==homeScore and  game["score"]["away"]["goals"] == awayScore:
                matchingGames.append(game)
                gameMatches+=1
        if len(matchingGames) > 0:
            matches.append({"day": gamedayDict["date"], "games": matchingGames})
                
        for match in matches:
            print(match["day"])
            print("-------------------------------")
            for game in match["games"]:
                print(f"{game["score"]["home"]["goals"]} - {game["score"]["away"]["goals"]} [{game["score"]["home"]["team"]} - {game["score"]["away"]["team"]}]")
            print("\n\n")
        
    print("-----------------")
    print(f"matching games {gameMatches} of 240 ({round((gameMatches/(len(gamedays)*8))*100,1)}%)")


def getTotalGoals():          
    season = int(input("Year: "))
    matches = []
    seasonDict = getSeason(season)
    totalGoals = int(input("Total Goals: "))
    gameMatches=0

    gamedays = seasonDict["gamedays"]

    for day in gamedays:
        gamedayDict = getGameday(season, day)
        games = gamedayDict["games"]
        matchingGames = []
        for game in games:
            if game["score"]["home"]["goals"] + game["score"]["away"]["goals"] == totalGoals:
                matchingGames.append(game)
                gameMatches+=1
        if len(matchingGames) > 0:
            matches.append({"day": gamedayDict["date"], "games": matchingGames})
                
        for match in matches:
            print(match["day"])
            print("-------------------------------")
            for game in match["games"]:
                print(f"{game["score"]["home"]["goals"]} - {game["score"]["away"]["goals"]} [{game["score"]["home"]["team"]} - {game["score"]["away"]["team"]}]")
            print("\n\n")
        
    print("-----------------")
    print(f"matching games {gameMatches} of 240 ({round((gameMatches/(len(gamedays)*8))*100,1)}%)")
    


def getGoalsUnder():
    season = int(input("Year: "))
    matches = []
    seasonDict = getSeason(season)
    totalGoals = int(input("Goals under: "))
    gameMatches=0

    gamedays = seasonDict["gamedays"]

    for day in gamedays:
        gamedayDict = getGameday(season, day)
        games = gamedayDict["games"]
        matchingGames = []
        for game in games:
            if game["score"]["home"]["goals"] + game["score"]["away"]["goals"] < totalGoals:
                matchingGames.append(game)
                gameMatches+=1
        if len(matchingGames) > 0:
            matches.append({"day": gamedayDict["date"], "games": matchingGames})
                
        for match in matches:
            print(match["day"])
            print("-------------------------------")
            for game in match["games"]:
                print(f"{game["score"]["home"]["goals"]} - {game["score"]["away"]["goals"]} [{game["score"]["home"]["team"]} - {game["score"]["away"]["team"]}]")
            print("\n\n")
        
    print("-----------------")
    print(f"matching games {gameMatches} of 240 ({round((gameMatches/(len(gamedays)*8))*100,1)}%)")
    



def render():
    print(".:STAT EXPLORER:.")
    print("-----------------")
    print("1 | Exact score")
    print("2 | Total goals")
    print("3 | Goals under")
    print("-----------------")
    


if __name__=="__main__":
    render()

    operation = int(input(">"))
    print("-----------------")
    
    match operation:
        case 1:
            getExactScore()
        case 2:
            getTotalGoals()
        case 3:
            getGoalsUnder()
        case _:
            print("ERROR: Bad selection")
    print("-----------------")
    
