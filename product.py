import SoftLayer.API
import pprint

client = SoftLayer.Client(username="IBM284483", api_key="69802976cabca4ed455b534848fc2e655196e204aae02977c23c58e5bad30a9f")
print "Categories:"
res = client['Product_Item_Price'].getCategories(id='1')
pprint.pprint(res)
print "Inventory:"
res = client['Product_Item_Price'].getInventory(id='1')
pprint.pprint(res)
print "Item:"
res = client['Product_Item_Price'].getItem(id='1')
pprint.pprint(res)
print "object:"
res = client['Product_Item_Price'].getObject(id='1')
pprint.pprint(res)
print "Packages:"
res = client['Product_Item_Price'].getPackages(id='1')
pprint.pprint(res)
print "RatePrices:"
res = client['Product_Item_Price'].getUsageRatePrices(id='1')
pprint.pprint(res)
print "AccountRestrictions:"
res = client['Product_Item_Price'].getAccountRestrictions(id='1')
pprint.pprint(res)
