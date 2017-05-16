from flask import Flask, render_template, jsonify
from vspk import v4_0 as vspk
import logging
from vspk.utils import set_log_level

app = Flask(__name__)

# Auth vars
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
        data = {}
        for vsp in csproot.vsps.get():
            data['vscs'] = []
            data['name'] = vsp.name
            for vsc in vsp.vscs.get():
		vsc_dict = vsc.dict()
                data_vsc = {
                    'name': vsc.name,
                    'status': vsc.status,
		    'averageMemoryUsage': vsc_dict['averageMemoryUsage'],
                    'vrss': []
                }
                for vrs in vsc.vrss.get():
                    data_vsc['vrss'].append({
                        'name': vrs.name,
                        'status': vrs.status,
                        'address': vrs.address,
                        'uptime': vrs.uptime,
                    })
                data['vscs'].append(data_vsc)

        return data

@app.route('/')
def table():
    setup_logging()
    csproot = start_csproot_session()
    #return jsonify(vsc_health(csproot))
    return render_template('table.html', vsp=vsc_health(csproot))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='9000')
