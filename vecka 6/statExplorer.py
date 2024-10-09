import requests # type: ignore
import json



def getSeason(season):
    r = requests.get("http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/"+season)
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        print("season not found")

def getGameday(season, day):
    r = requests.get(f"http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/{season}/{day}")
    if r.status_code == 200:
       return json.loads(r.text)
    else:
        print("Gameday not found")



"""gamedays = getSeason(season)["gamedays"]
print(gamedays)
for day in gamedays:
    print(getGameday(season, day))
"""
def getExactScore(season):
        homeScore=int(input("Home score: "))
        awayScore=int(input("Away score: "))
        matches=0
        seasonDict=getSeason(season)
        gamedays= seasonDict["gamedays"]
        for day in gamedays:
            games=getGameday(season, day)["games"]
            for game in games:
                if game["score"]["home"]["goals"]==homeScore and game["score"]["away"]["goals"]==awayScore:
                         matches+=1
                                         
        getGameday(season, day) #type: ignore
        print(matches)
        print("Matching games:", matches, "of", len(games), "(",matches/len(games),"%)") 
        
        
def getTotalGoals(season):          
    matches = []
    seasonDict = getSeason(season)
    totalGoals = int(input("Total Goals: "))

    gamedays = seasonDict["gamedays"]

    for day in gamedays:
        gamedayDict = getGameday(season, day)
        games = gamedayDict["games"]
        matchingGames = []
        for game in games:
            if game["score"]["home"]["goals"] + game["score"]["away"]["goals"] == totalGoals:
                matchingGames.append(game)
        if len(matchingGames) > 0:
            matches.append({"day": gamedayDict["date"], "games": matchingGames})
                
        for match in matches:
            print(match["day"])
            print("-------------------------------")
            for game in match["games"]:
                print(f"{game["score"]["home"]["goals"]} - {game["score"]["away"]["goals"]} [{game["score"]["home"]["team"]} - {game["score"]["away"]["team"]}]")
            print("\n\n")
        
    print("-----------------")
    print(games)
    print(f"matching games {len(matches)} of {len(gamedays)*8} ({(len(matches)/(len(gamedays)*8))*100}%)")
    # print(matches)
    


def getGoalsUnder():
    pass

    


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
    season = input("Year: ")
    match operation:
        case 1:
            getExactScore(season)
        case 2:
            getTotalGoals(season)
        case 3:
            getGoalsUnder(season)
        case _:
            print("ERROR: Bad selection")
    print("-----------------")
    

    


    # print(gamedays)
    # for day in gamedays:
    #     print(getGameday(season, day))