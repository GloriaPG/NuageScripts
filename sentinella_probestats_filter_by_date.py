import json
from elasticsearch import Elasticsearch

client = Elasticsearch(['192.168.0.24:9200'])

SourceNSG = "nsg-branch1-2"
SrcUplink = "port2"
interval  = "second" # year, quarter, month, week, day, hour, minute, second

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
	  },
	  "aggs" : {
        "probestats_over_time" : {
            "date_histogram" : {
                "field" : "timestamp",
                "interval" : "{0}".format(interval)
            }
        }
      },
      "sort" : [
          {"timestamp" : {"order" : "desc"}}
      ],
      "from" : 0, "size" : 1
	}
)

print json.dumps(response, indent=4, sort_keys=True)
