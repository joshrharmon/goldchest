import requests
import json
import re
import time

from flask import Flask
from flask_restful import Resource, Api, reqparse
from bs4 import BeautifulSoup

app = Flask(__name__)
api = Api(app)

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
        return status.json()
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
    if "/" in games:
        return games.replace("/", "%2F")
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
    return apiStatus(requests.get(apiRequest))
    
"""
gameLowest - Will return a game(s) lowest-ever price
param apiKey: API key for making request
param gameTitle: single, non-spaced game titles or multiple game titles separated by commas
    (e.g. dishonored OR amongus,dishonored,etc)
"""
def gameLowest(apiKey, gameTitle):
    gameFormat = gameList(gameTitle)
    apiRequest = "https://api.isthereanydeal.com/v01/game/lowest/?key=" + apiKey + "&plains=" + gameFormat + "&region=us&country=US&shops=steam"
    return apiStatus(requests.get(apiRequest))

"""
getPlains - Will return a game(s) "plain" titles based on ID
param apiKey: API key for making request
param ids: ids in the format of app/12345
"""
def getPlains(API_KEY, ids):
    idFormat = gameList(ids)
    apiRequest = "https://api.isthereanydeal.com/v01/game/plain/id/?key=" + API_KEY + "&shop=steam&ids=" + idFormat
    plainsDict = requests.get(apiRequest).json()
    return plainsDict.get('data').get(ids)

"""
gamePrices - Returns price data for games
param apiKey: API key for making request
param gameTitle: game to search for
"""
def gamePrices(apiKey, gameTitle):
    gameFormat = gameList(gameTitle)
    apiRequest = "https://api.isthereanydeal.com/v01/game/prices/?key=" + apiKey + "&plains=" + gameFormat + "&region=us&country=US&shops=steam"
    return apiStatus(requests.get(apiRequest))

"""
currentDeals - Will return the numGames amount of games most recently on sale that are SFW
param apiKey: API key for making request
param numGames: Number of games to return in list of deals
"""
def currentDeals(apiKey, numGames):
    gamesFetched = -1
    gameOffset = 0
    JSONData = []
    while gamesFetched < numGames:
        apiRequest = "https://api.isthereanydeal.com/v01/deals/list/?key=" + apiKey + "&offset=" + str(gameOffset) + "&limit=10&region=us&country=US&shops=steam&sort="
        gameJSON = requests.get(apiRequest).json()
        gen = (game for game in gameJSON.get('data').get('list') if gamesFetched < numGames)
        for game in gen:
            if "bundle" in game["urls"]["buy"]:
                continue
            gameHTML = retrieveMeta(game["urls"]["buy"], "html", None)
            if retrieveMeta(game["urls"]["buy"], "rating", gameHTML) == "SFW":
                game["art"] = retrieveMeta(game["urls"]["buy"], "art", gameHTML)
                JSONData.append(game)
                gamesFetched += 1
            gameOffset += 10
    return JSONData

"""
gameOverview - General information about the game
param apiKey: API key for making request
param title: game to search for
"""
def gameOverview(apiKey, title):
    titleFormat = gameList(title)
    apiRequest = "https://api.isthereanydeal.com/v01/game/overview/?key=" + apiKey + "&region=us&country=US&shop=steam&allowed=steam&ids=" + str(title)
    overJSON = requests.get(apiRequest).json()
    return overJSON
    
"""
retrieveMeta - Multi-purpose function to retrieve specific info on a game.
param gameURL: Direct link to Steam game
param dataType: "art" to get direct link to cover art or "rating" to get SFW/NSFW status
"""
def retrieveMeta(gameURL, dataType, HTMLdata):
    if dataType == "html":
        return requests.get(gameURL).content
    else:
        htmldata = HTMLdata
    soup = BeautifulSoup(htmldata, 'html.parser')
    if gameURL != None and dataType == "rating":
        if "bundle" in gameURL:
            gameBund = re.findall(r"http.*\d+", str(soup.find_all("a", class_="tab_item_overlay")))
            for game in gameBund:
                if retrieveMeta(game, "rating", retrieveMeta(game, "html", None)) == "NSFW":
                    return "NSFW"
                else:
                    continue
            return "SFW"
        else:
            if str(soup).lower().find("mature content description") > 0:
                return "NSFW" 
            else:
                return "SFW"
    elif gameURL != None and dataType == "art":
        if "bundle" in gameURL:
            return re.findall(r"http.*\d+", str(soup.find("img", class_="package_header")))
        else:
            return re.findall(r"http.*\d+", str(soup.find("img", class_="game_header_image_full")))

"""
steamDeals - Returns numGames amount of Steam games in JSON
param numGames: Amount of games to return
return JSON: JSON response of games requested
"""
def steamDeals(numGames):
    gamesFetched = 0
    JSONData = []
    steamFetch = "https://store.steampowered.com/search/?filter=topsellers"
    soup = BeautifulSoup(requests.get(steamFetch).content)
    gameData = re.findall(r"http.*\d+\"", str(soup.find_all("a", class_="search_result_row ds_collapse_flag")))
    gameItems = numGames * 2
    while gamesFetched < gameItems:
        gameJSON = dict()
        gameID = re.findall(r"app\/\d+|sub\/\d+", str(gameData[gamesFetched]))
        gamePlain = getPlains(API_KEY, gameID[0])
        gameInfo = gameGET(API_KEY, gamePlain).get('data').get(gamePlain)
        gamePriceData = gamePrices(API_KEY, gamePlain).get('data').get(gamePlain).get('list')
        gameJSON["title"] = gameInfo['title']
        gameJSON["price_old"] = gamePriceData[0].get('price_old')
        gameJSON["price_new"] = gamePriceData[0].get('price_new')
        gameJSON["price_cut"] = gamePriceData[0].get('price_cut')
        gameJSON["url"] = gamePriceData[0].get('url')
        gameJSON["art"] = gameInfo['image']
        JSONData.append(gameJSON)
        gamesFetched += 2
    return JSONData
        
"""
Deals - Outward API call to give all relevant game data to front-end
param num: Number of games to return
return JSON, statuscode: The JSON response and status code
"""
class Deals(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('num', required=True)
        args = parser.parse_args()
        return json.loads(json.dumps(steamDeals(int(args['num'])))), 200
    
"""
Lowest - Outward API call to give lowest price for list of games
param games: List of games to query (game1,game2,...) in 'plains' format
return JSON, statuscode: The JSON response and status code
"""
class Lowest(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('games', required=True)
        args = parser.parse_args()
        rawData = gameLowest(API_KEY, args['games']).get('data')
        for game in rawData.items():
            gameData = game[1].get('list')[0]
            html = retrieveMeta(gameData["url"], "html", None)
            gameData["art"] = retrieveMeta(gameData["url"], "art", html)
        jsonData = json.dumps(rawData)
        jsonObj = json.loads(jsonData)
        return jsonObj, 200
    
api.add_resource(Deals, '/deals')
api.add_resource(Lowest,'/lowest')
app.run()
