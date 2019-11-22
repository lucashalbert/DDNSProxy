from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Server Works!'
  
@app.route('/REST', methods=['GET'])
def rest_say_hello():
    return 'Hello from RESTful Server'

@app.route('/REST/ARecord', methods=['GET'])
def arecord_say_hello():
    return 'Hello from RESTful Server A Record method'

@app.route('/REST/ARecord/<zone>/<fqdn>', methods=['GET', 'POST'])
def create_a_record(zone, fqdn):
    if request.method == 'POST':
        """
        Arguments
        rdata: hash
        ttl: string
        """
        rdata = request.values['rdata']
        ttl = request.values['ttl']
        """ Response
        string fqdn — Fully qualified domain name of a node in the zone.
        hash rdata — RData defining the record.
        string address — IPv4 Address
        string record_type — The RRType of the record.
        string ttl — TTL for the record.
        string zone — Name of the zone
        """
        #return 'FQDN: %s\nRdata: %s\nAddress: %s\nRecord Type: %s\nTTL: %s' % (fqdn, rdata, address, record_type, ttl, zone)
        return 'Creating new A Record\nFQDN: %s\nRdata: %s\nAddress: %s\nRecord Type: %s\nTTL: %s\nZone: %s' % (fqdn, rdata, "10.10.10.10", "A", ttl, zone)
    elif request.method == 'GET':
        # return all A records
        return 'A record: %s %s %s' % (zone, fqdn, "10.10.10.10")


@app.route('/REST/ARecord/<zone>/<fqdn>/<record_id>', methods=['GET', 'PUT'])
def update_a_record(zone, fqdn, record_id):
    if request.method == 'PUT':
        """
        Arguments
        rdata: hash
        ttl: string
        """
        rdata = request.form['rdata']
        ttl = request.form['ttl']
        """ Response
        string fqdn — Fully qualified domain name of a node in the zone.
        hash rdata — RData defining the record.
        string address — IPv4 Address
        string record_type — The RRType of the record.
        string ttl — TTL for the record.
        string zone — Name of the zone
        """
        #return 'FQDN: %s\nRdata: %s\nAddress: %s\nRecord Type: %s\nTTL: %s' % (fqdn, rdata, address, record_type, ttl, zone)
        return 'Updating existing A Record\nFQDN: %s\nRdata: %s\nAddress: %s\nRecord Type: %s\nTTL: %s\nZone: %s' % (fqdn, rdata, "10.10.10.10", "A", ttl, zone)
    elif request.method == 'GET':
        # Return a specific A record
        return 'A record: %s %s %s' % (zone, fqdn, "10.10.10.10")

