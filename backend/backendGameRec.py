import backendGameFetch as fetch
backFetch = fetch.gameFetch(fetch.API_KEY, fetch.DB_PATH)

CUR_TAB_COLNAME = 1
LIKE = 1
DISLIKE = -1

class gameRec():

	"""
	Game Affinity:
	The value for any given genre can be -1, 0 or 1. -1 means the user does not
	like the genre and doesn't want to see it. 0 means neutral. 1 means the user 
	likes the genre and should be recommended it. 
	"""
	def dbInit(self):
		with backFetch.create_conn(fetch.DB_PATH) as con:
			con.execute('''CREATE TABLE IF NOT EXISTS 'gc_userData'(
							'username' VARCHAR(30) PRIMARY KEY,
							'action_aff' TINYINT DEFAULT 0,
							'indie_aff' TINYINT DEFAULT 0,
							'adventure_aff' TINYINT DEFAULT 0,
							'rpg_aff' TINYINT DEFAULT 0,
							'horror_aff' TINYINT DEFAULT 0,
							'mystery_aff' TINYINT DEFAULT 0,
							'simulation_aff' TINYINT DEFAULT 0,
							'sports_aff' TINYINT DEFAULT 0,
							'racing_aff' TINYINT DEFAULT 0,
							'shooter_aff' TINYINT DEFAULT 0,
							'strategy_aff' TINYINT DEFAULT 0,
							'fighting_aff' TINYINT DEFAULT 0,
							'retro_aff' TINYINT DEFAULT 0,
							'anime_aff' TINYINT DEFAULT 0
							);''')
	"""
	modAff (Modify Affinity) - Change affinity values for various game types
	param affList: A list of tuples of genres and the value to set the affinity to.
	(e.g. {(action, 1), (rpg, -1), (anime, 0)}). If affList == "RESET", all affinities
	are reset to neutral in the table. If affList == "HIDEALL", all genres are set to 
	dislike (hidden), which could be useful if the user wants to select a few genres 
	to be recommended and hide everything else.
	param username: Username to modify
	param verbose: Defaults to False, set to True to print error/success messages
	"""	
	def modAff(self, affList, user, verbose=False):
		sqlStmtSelect = "PRAGMA table_info('{}')".format("gc_userData")
		status = ""
		with backFetch.create_conn(fetch.DB_PATH) as con:
			if "RESET" not in affList and "HIDEALL" not in affList:
				for aff in affList:
					sqlStmt = "UPDATE gc_userData SET '{}' = {} WHERE username = '{}'".format(aff[0] + "_aff", aff[1], user)
					try:
						con.execute(sqlStmt)
					except fetch.Error as e:
						verbose and print(":: Update of affinities '{}' for user '{}' did not succeed.".format(affList, user))
				verbose and print(":: Update of affinities '{}' for user '{}' succeeded.".format(affList, user))
			else:
				cursor = con.execute(sqlStmtSelect)
				for row in cursor:
					setFlag = 0
					if "username" in row[CUR_TAB_COLNAME]:
						continue	
					elif "HIDEALL" in affList:
						setFlag = -1
					sqlStmt = "UPDATE gc_userData SET '{}' = {} WHERE username = '{}'".format(row[CUR_TAB_COLNAME], setFlag, user)
					try:
						con.execute(sqlStmt)
						verbose and print(":: '{}' for user '{}' successful.".format(affList, user))
					except fetch.Error as e:
						verbose and print(":: '{}' for user '{}' did not succeed.".format(affList, user))

	"""
	getAff (Get Affinity) - Retrieve specific (or all) affinity values for games.
	param - affList: List of tuples to get status for. If affList == "LIKE", it
	will return all affinities with value '1'. If affList == "DISLIKE", it will 
	return all affinities with value '-1'. If affList is a list of genres, it will
	return the values for those genres. All responses will be in a JSON list. 
	param verbose: Defaults to False, set to True to print error/success messages
	"""
	def getAff(self, affList, user, verbose=False):
		sqlStmtSelect = "PRAGMA table_info('{}')".format("gc_userData")
		affJSON = dict()
		with backFetch.create_conn(fetch.DB_PATH) as con:
			if "LIKE" not in affList and "DISLIKE" not in affList:
				affList = [aff + '_aff' for aff in affList]
				sqlAffList = ", ".join(affList)
				sqlStmt = "SELECT {} FROM gc_userData WHERE username = '{}'".format(sqlAffList, user)
				try:
					cursor = con.execute(sqlStmt)
					verbose and print(":: SELECT statment for affinities '{}' for user '{}' successful.".format(affList, user))
				except fetch.Error as e:
					verbose and print(":: SELECT statment for affinities '{}' for user '{}' was not successful.".format(affList, user))
				for row in cursor:
					for entry in range(len(row)):
						affJSON[affList[entry]] = row[entry]
			else:
				sqlStmt = "SELECT * FROM gc_userData WHERE username = '{}'".format(user)
				try:
					cursor = con.execute(sqlStmt)
					verbose and print(":: SELECT statment for all affinities for user '{}' successful.".format(user))
				except fetch.Error as e:
					verbose and print(":: SELECT statment for all affinities for user '{}' was not successful.".format(user))
				cursorNames = con.execute(sqlStmtSelect)
				for row in cursor:
					for rowName, entry in zip(cursorNames, range(len(row))):
						if "username" in rowName[CUR_TAB_COLNAME]:
							continue
						else:
							if affList == "LIKE" and row[entry] == LIKE:
								affJSON[rowName[CUR_TAB_COLNAME][:-4]] = row[entry]
							elif affList == "DISLIKE" in affList and row[entry] == DISLIKE:
								affJSON[rowName[CUR_TAB_COLNAME][:-4]] = row[entry]
		return affJSON
	
	"""
	getPersonalRec - Returns a personalized list of games already present in the
	database for a user based on their preferences
	param user: username to lookup
	param limit: amount of games to return
	"""
	def getPersonalRec(self, user, limit, verbose=False):
		affJSON = [("\"" + genre + "\"") for genre in self.getAff("LIKE", user)]
		perJSON = []
		sqlStmt = """SELECT * FROM webpage 
						WHERE category IN({}) 
						GROUP BY title 
						ORDER BY RANDOM()
						LIMIT {}""".format(", ".join(affJSON), limit)
		with backFetch.create_conn(fetch.DB_PATH) as con:
			try:
				cursor = con.execute(sqlStmt)
				for row in cursor:
					perJSON.append(backFetch.dbToJSON(row, cursor))	
			except fetch.Error as e:
				verbose and print(":: SELECT statement for personalized recommendations for user '{}' was not successful.".format(user))
		return perJSON
						
	def start(self):
		self.dbInit()
		fetch.api.add_resource(Recommendation, '/rec')
		
"""
Recommendation - Outward API call to manage game recommendations
param op: either mod (Modify) or get
param args: Comma-separated list of affinities to modify or get.
Examples:
	For modify:
		args=anime,1,rpg,-1,action,1 (Will set these genres)
		args=RESET (Will reset all genres)
		args=HIDEALL (Will set all genres to dislike)
		
	For get:
		args=anime,rpg,action (Will return affinities for these genres)
		args=LIKE (Will return all liked genres)
		args=DISLIKE (Will return all dislikes genres)
		args=RECC (Will return personalized list of recommendations, limit is REQUIRED)
		
param user: User to look up
"""
class Recommendation(fetch.Resource):
	def get(self):
		parser = fetch.reqparse.RequestParser()
		parser.add_argument('op', required=True)
		parser.add_argument('args', required=True)
		parser.add_argument('user', required=True)
		parser.add_argument('limit')
		args = parser.parse_args()
		
		errMSG = dict()
		
		if args['op'] == "mod":
			if(args['args'] == "RESET" or args['args'] == "HIDEALL"):
				return gameRec().modAff(args['args'], args['user'])
			else:
				argList = args['args'].split(",")
				argPass = []
				for elem in range(0, len(argList), 2):
					argPass.append((argList[elem], int(argList[elem + 1])))
				return gameRec().modAff(argPass, args['user'])
		elif args['op'] == "get":
			if(args['args'] == "LIKE" or args['args'] == "DISLIKE"):
				return gameRec().getAff(str(args['args']), args['user'])
			elif args['args'] == "RECC":
				if not args['limit']:
					errMSG["Message: "] = "Missing limit argument."
					return errMSG
				else:
					return gameRec().getPersonalRec(args['user'], int(args['limit']))
			else:
				argList = args['args'].split(",")
				argPass = []
				for elem in argList:
					argPass.append(elem)
				return gameRec().getAff(argPass, args['user'])
