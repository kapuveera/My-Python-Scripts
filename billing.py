import SoftLayer.API

#Create a client to the SoftLayer_Account API service.
client = SoftLayer.create_client_from_env(username="IBM284483", api_key="69802976cabca4ed455b534848fc2e655196e204aae02977c23c58e5bad30a9f")

# Now we can call the methods of the SoftLayer account 
prod_info = client['Product_Item_Category']

prod_list = prod_info.getBillingItems().get('description')

for prod in prod_list:
    print ("id: " + prod('id'))
