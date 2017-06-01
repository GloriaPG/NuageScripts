import json
from elasticsearch import Elasticsearch

client = Elasticsearch(['192.168.0.24:9200'])

DestinationNSG = "nsg-branch1-2"
DstUplink = "port2"

response = client.search(
    index="nuage_dpi_flowstats",
    body={
	  "query": {
	    "filtered": {
	      "query": {
	        "range" : {
	            "timestamp" : {
	                "gte" : "now-24h"
	            }
	        }
	      },
	      "filter" : {
	            "bool" : {
	                "must" : [
	                    { "term" : { "DestinationNSG" : "{0}".format(DestinationNSG) } }, 
	                    { "term" : { "DstUplink" : "{0}".format(DstUplink) } } 
	                ]
	            }
	        }
	    }
	  }
	}
)

print json.dumps(response, indent=4, sort_keys=True)
