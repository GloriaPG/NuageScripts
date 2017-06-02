#!/usr/bin/env python

# Created on 2017-05-11
# 
# @author: Galvarado - guillermo@sentinel.la
# 
#Depends on vspk, https://github.com/nuagenetworks/vspk-python/blob/4.0/doc/quickstart.rst




from vspk import v4_0 as vspk
import logging
from vspk.utils import set_log_level

# Auth vars
"""
vsd_ip = '147.75.69.37'
api_url = "https://vsd1.sdn40r8.lab:8443"
username = "csproot"
password = "csproot"
enterprise = "csp"
"""
vsd_ip = '192.168.0.20'
api_url = "https://192.168.0.20:8443"
username = "csproot"
password = "csproot"
enterprise = "csp"


def setup_logging():
    pass
    #set_log_level(logging.DEBUG, logging.Streamhandler())

def start_csproot_session():
    session = vspk.NUVSDSession(
        username=username,
        password=password,
        enterprise=enterprise,
        api_url=api_url
    )
    try:
        session.start()
    except:
        logging.error('Failed to start the session')
    return session.user


def vsc_health(csproot):
        print "DIR Object API Nuage"
        print csproot.__dict__
        print "++++++++++++++++++++++++++++++++++++++++++++++++++"
        for vsp in csproot.vsps.get():
            print "\n\n**********  VSP: %s **********" % vsp.name
            print vsp.to_dict()
            if True :
                for vsc in vsp.vscs.get():
                    print "\n\n#####  VSC: %s #####" % vsc.name
                    print vsc.to_dict()
                    if vsc.status == 'Down':
                        logging.info('VSC state is Not Healthy')
                        logging.info('Sending alert to Team')
                        break
                    elif vsc.status == 'UP':
                        logging.info('VSC state is Healthy')

                    else:
                        break
                    for vrs in vsc.vrss.get():
                        print "\n\n$$$$$  VRS: %s $$$$$" % vrs.name
                        print  vrs.to_dict()
                        if vrs.status == 'DOWN':
                            logging.info('VRS state is Not Healthy')
                            logging.info('Sending alert to Team')
                            break
                        elif vrs.status == 'UP':
                            logging.info('VRS state is Healthy')
                        else:
                            break

def cafectavba(csproot):
    #print csproot.__dict__
    response = {}
    for enterprise in csproot.enterprises.get(filter='ID is "6e51eafc-a2d7-4f6b-9a34-bb5262b60688"'):
        response['enterprise'] = enterprise
        nsg_branch_up = 0
        nsg_branch_dow = 0
        nsgs = []

        for g in enterprise.ns_redundant_gateway_groups.get(filter='ID is "79ad6616-3e75-4d98-b80f-efea2997d17a"'):
            for p in g.ns_gateways.get():
                if p.bootstrap_status != "ACTIVE":
                    nsg_branch_dow = nsg_branch_dow + 1
                else:
                    nsg_branch_up = nsg_branch_up +1
                ports_data = []
                for np in p.ns_ports.get():
                    nsg_port = {
                        "id": np.id,
                        "name": np.name,
                        "description" : np.description,
                        "status" : np.status,
                        "nsg-brach" : p.name,
                        "nsg-branch-id" : p.id
                    }
                    #print nsg_port
                    ports_data.append(nsg_port)
                    for stats in np.statistics.get():
                        print stats.stats_data +"\n"
                        print stats.number_of_data_points + "\n"

                nsg = {
                    "name": p.name,
                    "status" : p.bootstrap_status,
                    "cpu_usage" : 10.0,
                    "memory_usage" : 10.0,
                    "ports" : ports_data
                }
                print nsg
                nsgs.append(nsg)
        
        response['nsg-branch-dow'] = nsg_branch_dow
        response['nsg-branch-up'] = nsg_branch_up
    """
    for vsp in obj:
        print "\n\n**********  VSP: %s **********" % vsp.name
        print vsp.to_dict()
    """
    
            
def main():

    setup_logging()
    csproot = start_csproot_session()
    #import pdb; pdb.set_trace()
    cafectavba(csproot)
    #vsc_health(csproot)

if __name__ == "__main__":
   main()
   #import pdb; pdb.set_trace()

