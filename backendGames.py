import requests
import json

GENRE_ACTION = ["Violent", "Gore", "Platformer", "Fast-paced", "Roguelite", "Batman"]
GENRE_INDIE = ["Point and click", "Crowdfunded", "Reboot", "8-bit Music"]
GENRE_ADVENTURE = ["Atmospheric", "Story-Rich", "Sci-fi", "Fantasy", "Exploration", "Space", "Sandbox"]
GENRE_RPG = ["Turn-based", "Building", "RPGMaker", "JRPG", "Action RPG", "Post-apocalyptic"]
GENRE_HORROR = ["Violent", "Gore", "Psychological Horror", "Survival Horror"]
GENRE_MYSTERY = ["Dark", "Detective", "Thriller", "Psychological Horror", "Crime"]
GENRE_SIMULATION = ["VR", "Survival", "Physics", "Farming Sim", "Cooking", "Transportation"]
GENRE_SPORTS = ["Football", "Soccer", "Baseball", "Gambling", "Boxing", "Golf", "Basketball", "Wrestling", "Tennis", "Skateboarding", "Hockey", "Bowling", "Cycling", "Sailing", "Archery"]
GENRE_RACING = ["Motorbike", "Cycling", "Time Attack", "Snow"]
GENRE_SHOOTER = ["Gore", "First-person", "Tactical", "Shoot-em-up", "Zombies", "Bullet Hell", "Top-down", "War"]
GENRE_STRATEGY = ["Puzzle", "Tactical", "Management", "Turn-based Strategy", "RTS", "Crafting", "Tower Defense", "Card Game"]
GENRE_FIGHTING = ["Gore", "Combat", "Beat 'em up"]
GENRE_RETRO = ["Pixel Graphics", "Arcade", "Top down", "Sidescroller", "Classic", "Cult Classic", "Tabletop", "8-bit Music"]
GENRE_ANIME = ["Visual Novel"]

gameRelation = {
    "GENRE_ACTION": ["GENRE_ADVENTURE", "GENRE_FIGHTING", "GENRE_SPORTS", "GENRE_RETRO"],
    "GENRE_INDIE": ["GENRE_ADVENTURE", "GENRE_RPG", "GENRE_RETRO"],
    "GENRE_ADVENTURE": ["GENRE_INDIE", "GENRE_SIMULATION"],
    "GENRE_RPG": ["GENRE_STRATEGY", "GENRE_SIMULATION", "GENRE_ANIME"],
    "GENRE_HORROR": ["GENRE_MYSTERY", "GENRE_FIGHTING"],
    "GENRE_MYSTERY": ["GENRE_HORROR", "GENRE_ADVENTURE"],
    "GENRE_SIMULATION": ["GENRE_ANIME", "GENRE_RPG", "GENRE_SPORTS"],
    "GENRE_SPORTS": ["GENRE_ACTION", "GENRE_RACING"],
    "GENRE_RACING": ["GENRE_SPORTS", "GENRE_FIGHTING"],
    "GENRE_SHOOTER": ["GENRE_ACTION", "GENRE_FIGHTING"],
    "GENRE_STRATEGY": ["GENRE_RPG", "GENRE_MYSTERY"],
    "GENRE_FIGHTING": ["GENRE_SHOOTER", "GENRE_ACTION"],
    "GENRE_RETRO": ["GENRE_INDIE", "GENRE_ADVENTURE"],
    "GENRE_ANIME": ["GENRE_INDIE", "GENRE_RPG"]
}

API_KEY='4ca42d11f7def3c9d0eea805aa48413a2c5ec7e6'

"""
apiStatus - Returns API response or error code
param status: Takes in request object from Python API request
return status: Prints API JSON body if successful (200), else returns appropriate error code
"""
def apiStatus(status):
    if status.status_code == 200:
        print(status.json())
    else:
        returnMsg = ":: API fetch failed with error code: " + str(status)
        print(returnMsg)

"""
gameList - If string contains commas (indicating multiple game queries), replace with appropriate string
param games: list of game(s)
return games: Properly formatted string to execute a multi-return API request
"""
def gameList(games):
    if "," in games:
        return games.replace(",","%2C")
    else:
        return games
        
"""
userNameGET - Returns string representation of a Steam username granted by the OAuth Token
param oauthToken: OAuth token required to access Steam profile and return username
"""
def usernameGET(oauthToken):
    apiRequest = "https://api.isthereanydeal.com/v01/user/info?access_token=" + oauthToken
    apiStatus(apiRequest)

"""
gameGET - Returns basic metadata about game (does not include prices)
param apiKey: API key for making request
param gameTitle: single, non-spaced game titles or multiple game titles separated by commas
    (e.g. dishonored OR amongus,dishonored,etc)
"""
def gameGET(apiKey, gameTitle):
    gameFormat = gameList(gameTitle)
    apiRequest = "https://api.isthereanydeal.com/v01/game/info/?key=" + apiKey + "&plains=" + gameFormat
    apiStatus(requests.get(apiRequest))

"""
gameLowest - Will return a game(s) lowest-ever price
param apiKey: API key for making request
param gameTitle: single, non-spaced game titles or multiple game titles separated by commas
    (e.g. dishonored OR amongus,dishonored,etc)
"""
def gameLowest(apiKey, gameTitle):
    gameFormat = gameList(gameTitle)
    apiRequest = "https://api.isthereanydeal.com/v01/game/prices/?key=" + apiKey + "&plains=" + gameFormat + "&region=us&country=US&shops=steam"
    apiStatus(requests.get(apiRequest))
    
"""
currentDeals - Will return the numGames amount of games most recently on sale
param apiKey: API key for making request
param numGames: Number of games to return in list of deals
"""
def currentDeals(apiKey, numGames):
    apiRequest = "https://api.isthereanydeal.com/v01/deals/list/?key=" + apiKey + "&limit=" + str(numGames) + "&region=us&country=US&shops=steam"
    apiStatus(requests.get(apiRequest))
