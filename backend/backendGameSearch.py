
import requests, json, backendGameFetch as fetch

backFetch = fetch.gameFetch(fetch.API_KEY, fetch.DB_PATH)

class gameSearch():
    def search(self, query, numResults):
        gamesFetched = 0
        searchURL = "https://store.steampowered.com/search/?term='{}'".format(query)
        soup = fetch.BeautifulSoup(requests.get(searchURL).content, features='html.parser')
        searchArr = []
        gameData = soup.find_all("a", class_="search_result_row ds_collapse_flag")
        gameTitles = soup.find_all("span", class_="title")
        gamePrices = soup.find_all("div", class_="col search_price responsive_secondrow")
        while gamesFetched < numResults:
            searchItem = dict()
            searchItem["title"] = gameTitles[gamesFetched].contents[0]
            searchItem["price"] = backFetch.priceFormat(gamePrices[gamesFetched].contents[0])
            searchItem["url"] = gameData[gamesFetched]['href']
            searchArr.append(searchItem)
            gamesFetched += 1
        return searchArr
        
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
        return gameSearch().search(args['query'], int(args['limit'])), 200
