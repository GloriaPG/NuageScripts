import requests
import json
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta

client = Elasticsearch(['192.168.0.24:9200'])

datetime_less_five_minutes = datetime.now() - timedelta(minutes=5)
epochtime_less_five_minutes = int(datetime_less_five_minutes.strftime("%s")) * 1000

datetime_lte = datetime.now()
epochtime_lte = int(datetime_lte.strftime("%s")) * 1000

response = client.search(
    index="nuage_dpi_probestats",
    body={
	    "query": {
	        "range" : {
	            "timestamp" : {
	                "gte" : "now-5m"
	            }
	        }
	    }
    }
)
print json.dumps(response, indent=4, sort_keys=True)

URL = 'http://192.168.0.24:9200'

request_api= requests.get(URL  + "/nuage_dpi_probestats-2017-05-31/_search?pretty")
#print json.dumps(request_api.json(), indent=4, sort_keys=True)
