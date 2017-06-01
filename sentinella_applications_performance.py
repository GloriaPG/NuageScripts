import json
from elasticsearch import Elasticsearch

client = Elasticsearch(['192.168.0.24:9200'])

DestinationNSG = "nsg-branch2-1"
DstUplink = "port1"

response = client.search(
    index="nuage_dpi_flowstats",
    body={
	  "query": {
	    "filtered": {
	      "filter" : {
	            "bool" : {
	                "must" : [
	                    { "term" : { "DestinationNSG" : "{0}".format(DestinationNSG) } }, 
	                    { "term" : { "DstUplink" : "{0}".format(DstUplink) } } 
	                ]
	            }
	        }
	    }
	  },
	  "aggs": {
        "group_by_AppID": {
          "terms": {
            "field": "AppID.keyword"
          },
          "aggs": {
            "average_TotalMB": {
              "avg": {
                "field": "TotalMB"
              }
            }
          }
        }
      }
	}
)

print json.dumps(response, indent=4, sort_keys=True)
