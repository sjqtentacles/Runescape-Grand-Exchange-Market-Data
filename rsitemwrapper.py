import requests
import json

class RunescapeAPI:
    def getItemGraph(self,itemID):
        try:
            data = requests.get("http://services.runescape.com/m=itemdb_rs/api/graph/"+str(itemID)+".json")
            data = data.content
            data = json.loads(data)
            return data
        except:
            pass
    def getItemPriceInformation(self,itemID):
        try:
            data = requests.get("http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item="+str(4798))
            data = data.content
            data = json.loads(data)
            return data
        except:
            pass
