import backendGameFetch as fetch, backendGameSearch as search

GENRE_ACTION = ["Violent", "Gore", "Platformer", "Fast-paced", "Roguelite", "Batman"]
GENRE_INDIE = ["Point and click", "Crowdfunded", "Reboot", "8-bit Music"]
GENRE_ADVENTURE = ["Atmospheric", "Story-Rich", "Sci-fi", "Fantasy", "Exploration", "Space", "Sandbox"]
GENRE_RPG = ["Turn-based", "Building", "RPGMaker", "JRPG", "Category RPG", "Post-apocalyptic"]
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

backFetch = fetch.gameFetch(fetch.API_KEY, fetch.DB_PATH)
backSearch = search.gameSearch(fetch.API_KEY, fetch.DB_PATH)
backFetch.start()
backSearch.start()
fetch.app.run()

while True:
	fetch.schedule.run_pending()
	time.sleep(1)
