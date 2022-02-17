from pymongo_test_insert import get_database
dbname = get_database()

collection_name = dbname["neighborhoods"]


item_details = collection_name.find()
print (type(item_details.collection))
for i in item_details:
    print(i)
