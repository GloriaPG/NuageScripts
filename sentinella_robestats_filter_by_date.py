import requests
import json
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta

client = Elasticsearch(['192.168.0.24:9200'])

less_five_minutes = datetime.now() - timedelta(minutes=15)

response = client.search(
    index="nuage_dpi_probestats",
    body={
	    "query": {
	        "range" : {
	            "timestamp" : {
	                "gte" : "2017-05-31 18:49:32.365950",
	            }
	        }
	    }
    }
)
print json.dumps(response, indent=4, sort_keys=True)

URL = 'http://192.168.0.24:9200'

request_api= requests.get(URL  + "/nuage_dpi_probestats-2017-05-31/_search?pretty")
#print json.dumps(request_api.json(), indent=4, sort_keys=True)
