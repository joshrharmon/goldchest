import requests, json, backendGameFetch as fetch

backFetch = fetch.gameFetch(fetch.API_KEY, fetch.DB_PATH)

class gameSearch():
	def __init__(self, api_key, db_path):
		self.api_key = api_key
		self.db_path = db_path
		
	def search(self, name, numResults, apikey):
		apiRequest = "https://api.isthereanydeal.com/v02/search/search/?key=" + str(fetch.API_KEY) + "&q=" + backFetch.gameList(str(name)) + "&limit=" + numResults
		print(apiRequest)
		return backFetch.apiStatus(requests.get(apiRequest))
		
	def start(self):
		fetch.api.add_resource(Search, '/search')
	
"""
Search - Outward API call to give search results to front-end
param query: Search query
param limit: Number of results to return
return JSON, statuscode: The JSON response and status code
"""
class Search(fetch.Resource):
	def get(self):
		parser = fetch.reqparse.RequestParser()
		parser.add_argument('query', required=True)
		parser.add_argument('limit', required=True)
		args = parser.parse_args()
		print(args['query'], args['limit'], fetch.API_KEY)
		return json.loads(json.dumps(gameSearch(fetch.API_KEY, fetch.DB_PATH).search(args['query'], args['limit'], fetch.API_KEY))), 200
