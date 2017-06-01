import json
from elasticsearch import Elasticsearch

client = Elasticsearch(['192.168.0.24:9200'])

SourceNSG = "nsg-branch1-2"
SrcUplink = "port1"
response = client.search(
    index="nuage_dpi_probestats",
    body={
	    "query": {
	        "range" : {
	            "timestamp" : {
	                "gte" : "now-5m"
	            }
	        },
	        "constant_score" : {
	            "filter" : {
	                 "bool" : {
	                    "must" : [
	                        { "term" : { "SourceNSG" : "{0}".format(SourceNSG) } }, 
	                        { "term" : { "SrcUplink" : "{0}".format(SrcUplink) } } 
	                    ]
	                }
	            }
            }
	    }
    }
)
print json.dumps(response, indent=4, sort_keys=True)
