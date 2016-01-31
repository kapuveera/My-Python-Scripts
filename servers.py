import SoftLayer.API

#Create a client to the SoftLayer_Account API service.
client = SoftLayer.create_client_from_env(username="IBM284483", api_key="69802976cabca4ed455b534848fc2e655196e204aae02977c23c58e5bad30a9f")

#Get list of CCIs
server_list = client['Account'].getVirtualGuests()

for server in server_list:
    print "id: " + str(server['id']) + " hostname: " + server['hostname'] + "." + server['domain']

#Get list of baremetal instances
server_list = client['Account'].getBareMetalInstances()

for server in server_list:
    print "id: " + str(server['id']) + " hostname: " + server['hostname'] + "." + server['domain']

# get the dedicated servers
server_list = client['Account'].getHardware()

for server in server_list:
    print "id: " + str(server['id']) + " hostname: " + "hostname: " + server['hostname'] + "." + server['domain']
