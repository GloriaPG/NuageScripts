import json
from elasticsearch import Elasticsearch

client = Elasticsearch(['192.168.0.24:9200'])

SourceNSG = "nsg-branch1-2"
SrcUplink = "port2"

response = client.search(
    index="nuage_dpi_probestats",
    body={
	  "query": {
	    "filtered": {
	      "query": {
	        "range" : {
	            "timestamp" : {
	                "gte" : "now-5m"
	            }
	        }
	      },
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

response = client.search(
    index="nuage_dpi_probestats",
    body={
	  "query": {
	    "filtered": {
	      "filter" : {
	            "bool" : {
	                "must" : [
	                    { "term" : { "SourceNSG" : "{0}".format(SourceNSG) } }, 
	                    { "term" : { "SrcUplink" : "{0}".format(SrcUplink) } } 
	                ]
	            }
	        }
	    }
	  },
	  "from" : 0, "size" : 10,
	  "sort": [
		    {
		        "timestamp": "desc"
		    }
	    ]
	}
)

print json.dumps(response, indent=4, sort_keys=True)
