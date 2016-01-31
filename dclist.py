import SoftLayer.API

#Create a client to the SoftLayer_Account API service.
client = SoftLayer.create_client_from_env(username="IBM284483", api_key="69802976cabca4ed455b534848fc2e655196e204aae02977c23c58e5bad30a9f")

# Now we can call the methods of the SoftLayer account 
dc_info = client['Location']

#image_list = virtual_guest.getCreateObjectOptions().get('operatingSystems')
dc_list = dc_info.getDatacenters()

for dc in dc_list:
    print ("id: " + str(dc['id']) + " name: " + dc['name'] + "Long Name: " + dc['longName'])
