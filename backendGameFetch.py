import requests, json, re, schedule, time, sqlite3

from flask import Flask
from sqlite3 import Error
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

steamCategoryID = {
	"action": 19,
	"indie": 492,
	"adventure": 21,
	"rpg": 122,
	"horror": 1667,
	"mystery": 5716,
	"simulation": 599,
	"sports": 701,
	"racing": 699,
	"shooter": 1774,
	"strategy": 9,
	"fighting": 1743,
	"retro": 4004,
	"anime": 4085
}

API_KEY='4ca42d11f7def3c9d0eea805aa48413a2c5ec7e6'
GAMES_TO_FETCH = 10

def create_conn(path):
    connection = None
    try:
        connection = sqlite3.connect(path, check_same_thread = False)
        print("DB connection successfully.")
    except Error as e:
       #for security purpose we do not send the exact reason why the Database failed
        print(f" Sorry, an error occurred during Database connection")
    return connection

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
OBSOLETE until isthereanydeals fixes NULL title field

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
param dataType: "art" to get direct link to cover art, "html" to retrieve html data
"""
def retrieveMeta(gameURL, dataType, HTMLdata):
	if dataType == "html":
		return requests.get(gameURL).content
	else:
		soup = BeautifulSoup(HTMLdata, 'html.parser').head
		if gameURL != None and dataType == "art":
			# TOFIX: Find specific image tag and get attribute
			# If temporary HTML fetch error occurs, re-fetch
			if soup == None:
				tempHTML = retrieveMeta(gameURL, "html", None)
				retrieveMeta(gameURL, "art", tempHTML)
			else:
				temp = soup.find_all("link")[-1]
				return re.findall(r"http.*\d+", str(temp))[0]

"""
dbForm - Escapes special characters
param text - Text to inspect
return text - Escaped characters in string if applicable
"""
def dbForm(text):
	if "'" in text:
		return text.replace("'","''")
	else:
		return text

"""
dbConn - Will start a db connection and return it
"""
def dbConn():
	conn = create_conn("django-rest-react-prototype/db.sqlite3")
	return conn

"""
dbInit - Will create and initialize tables
"""
def dbInit():
	with dbConn() as con:
		con.execute('''DROP TABLE IF EXISTS 'webpage';''')
		con.execute('''CREATE TABLE 'webpage' (
						'gameID' int PRIMARY KEY,
						'title' VARCHAR(255) NOT NULL,
						'category' VARCHAR(32) NOT NULL,
						'price_old' float NOT NULL,
						'price_new' float NOT NULL,
						'price_cut' smallint NOT NULL,
						'url' varchar(255) NOT NULL,
						'art' varchar(255)
						);''')

"""
showDB - Will print all db rows
"""
def showDB(category):
	with dbConn() as con:
		sqlStmt = "SELECT * FROM webpage WHERE category='{}'".format(category)
		cursor = con.execute(sqlStmt)
		for row in cursor:
			print("title: " + str(row[0]) + ", \ncategory: " + str(row[1]) + ", \nprice_old: " + str(row[2]) + ", \nprice_new: " + str(row[3]) + ", \nprice_cut: " + str(row[4]) + ", \nurl: " + str(row[5]) + ", \nart: " + str(row[6]))
			print("\n")

"""
steamDBFetch - Will fetch numGmaes from APIs and Steam and update DB every 6 hours
param numGames: Amount of games to fetch from Steam and APIs
param category: Specify front, action, indie, adventure, etc. to get a narrowed result
"""
def steamDBFetch(category, numGames=6):
	print("Fetching " + str(numGames) + " games from category " + str(category) + "...")
	with dbConn() as con:
		gamesFetched = 0
		gameItems = numGames
		steamFetch = "https://store.steampowered.com/search/?specials=1" if "front" in category else "https://store.steampowered.com/search/?tags={}&specials=1".format(steamCategoryID.get(category))
		soup = BeautifulSoup(requests.get(steamFetch).content, features="lxml")
		gameData = soup.find_all("a", class_="search_result_row ds_collapse_flag")
		gameTitles = soup.find_all("span", class_="title")
		gameOldPrices = soup.find_all("strike")
		gameNewPrices = soup.find_all("div", class_="col search_price discounted responsive_secondrow")
		while gamesFetched < gameItems:
			url = gameData[gamesFetched]['href']

			# Fetch HTML for game page for scraping
			gameHTML = retrieveMeta(url, "html", None)
			soup = BeautifulSoup(gameHTML, 'html.parser')

			title = gameTitles[gamesFetched].contents[0]
			price_old = gameOldPrices[gamesFetched].contents[0]
			price_new = gameNewPrices[gamesFetched].contents[-1].strip()
			price_cut = round(100.00 - ((float(price_new[1:]) * 100) / (float(price_old[1:]))))

			art = retrieveMeta(url, "art", gameHTML)
			# Insert into db
			con.execute("INSERT INTO webpage(title, category, price_old, price_new, price_cut, url, art) VALUES(?,?,?,?,?,?,?)", (title, category, price_old, price_new, price_cut, url, art))
			gamesFetched += 1
"""
steamDBResp - Will access the SQLite DB and form a JSON response for the frontend to fetch
param numGames: Amount of games to fetch
return: JSON response for numGames
"""
def steamDBResp(category, numGames=6):
	with dbConn() as con:
		JSONData = []
		sqlFetch = "SELECT * FROM webpage WHERE category='{}' LIMIT '{}'".format(category, numGames)
		cursor = con.execute(sqlFetch)
		for row in cursor:
			gameJSON = dict()
			gameJSON["title"] = row[1]
			gameJSON["category"] = row[2]
			gameJSON["price_old"] = row[3]
			gameJSON["price_new"] = row[4]
			gameJSON["price_cut"] = row[5]
			gameJSON["url"] = row[6]
			gameJSON["art"] = row[7]
			JSONData.append(gameJSON)
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
		parser.add_argument('cat')
		args = parser.parse_args()
		return json.loads(json.dumps(steamDBResp(args['cat'], int(args['num'])))), 200

"""
OBSOLETE - Based on older code, not in use in this version.
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

"""
Main program:
- Initialize DB with tables
- Start scheduler to refresh DB every hour with 6 games by default
- Start Flask server
- Make sure scheduler continues to check for pending tasks if missed
"""
dbInit()
steamDBFetch("front")
schedule.every().hour.do(steamDBFetch, "front")

for key in steamCategoryID:
	steamDBFetch(key, 10)
	schedule.every().hour.do(steamDBFetch, key, 10)

api.add_resource(Deals, '/deals')
# api.add_resource(Lowest,'/lowest')
app.run()

while True:
	schedule.run_pending()
	time.sleep(1)
