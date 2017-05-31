import requests
import json
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta

client = Elasticsearch(['192.168.0.24:9200'])

start = datetime.now() - timedelta(hours=24)
end = datetime.now()

start = int(start.strftime("%s")) * 1000
end  = int(end.strftime("%s")) * 1000



response = client.search(
    index="nuage_dpi_flowstats-2017-05-31",
    body={ "sort":[ { "timestamp":{ "order":"desc" } } ], "query":{ "bool":{ "should":[ { "bool":{ "must":[ { "term":{ "SourceNSG":"nsg-branch1" } }, { "term":{ "DestinationNSG":"nsg-branch2" } }, ] } } ] } } }
)

for hit in response['hits']['hits']:
    print '*' * 1000
    print hit
 


URL = 'http://192.168.0.24:9200'

request_api= requests.get(URL  + "/nuage_dpi_probestats-2017-05-31/_search?pretty")
print json.dumps(request_api.json(), indent=4, sort_keys=True)
