
import json
from elasticsearch import Elasticsearch

client = Elasticsearch(['192.168.0.24:9200'])

SrcUplink = "port1"
SourceNSG = "nsg-branch1-1"
np = {"id":"9d495bdc-e545-403d-9bd0-11f279d8e028"}


response = client.search(
    index="nuage_dpi_flowstats",
    body={
      "query": {
        "filtered": {
          "filter": {
            "term": {
              "vportId": "9d495bdc-e545-403d-9bd0-11f279d8e028"
            }
          }
        }
      },
	  "sort" :[
	    {"timestamp" : {"order" : "desc"}}
	  ],
	  "from" : 0, "size" : 1
	}
)

print json.dumps(response, indent=4, sort_keys=True)
