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

print '#' * 1000
print 'Indices Nuage'

indices= requests.get(URL  + "/_cat/indices?v")
#print DPI_sla_stats.json()
print json.dumps(indices.json(), indent=4, sort_keys=True)


print '#' * 1000
print 'nuage_addressmap'
request_api= requests.get(URL  + "/nuage_addressmap-2017-05-31/_search?pretty")
#print DPI_sla_stats.json()
print json.dumps(request_api.json(), indent=4, sort_keys=True)
print '$' * 1000

print '#' * 1000
print 'nuage_vlan'
request_api= requests.get(URL  + "/nuage_vlan-2017-05-31/_search?pretty")
#print DPI_sla_stats.json()
print json.dumps(request_api.json(), indent=4, sort_keys=True)
print '$' * 1000

print '#' * 1000
print 'nuage_vport'
request_api= requests.get(URL  + "/nuage_vport-2017-05-31/_search?pretty")
#print DPI_sla_stats.json()
print json.dumps(request_api.json(), indent=4, sort_keys=True)
print '$' * 1000

print '#' * 1000
print 'nuage_vport'
request_api= requests.get(URL  + "/nuage_vport-2017-05-31/_search?pretty")
#print DPI_sla_stats.json()
print json.dumps(request_api.json(), indent=4, sort_keys=True)
print '$' * 1000

print '#' * 1000
print 'nuage_dpi_probestats'
request_api= requests.get(URL  + "/nuage_dpi_probestats-2017-05-31/_search?pretty")
#print DPI_sla_stats.json()
print json.dumps(request_api.json(), indent=4, sort_keys=True)
print '$' * 1000

print '#' * 1000
print 'nuage_dpi_flowstats'
DPI_flow_stats= requests.get(URL  + "/nuage_dpi_flowstats-2017-05-31/_search?pretty")
#print DPI_flow_stats.json()
print json.dumps(DPI_flow_stats.json(), indent=4, sort_keys=True)
print '$' * 1000

print '#' * 1000
print 'nuage_flow'
DPI_flow_stats= requests.get(URL  + "/nuage_flow-2017-05-31/_search?pretty")
#print DPI_flow_stats.json()
print json.dumps(DPI_flow_stats.json(), indent=4, sort_keys=True)