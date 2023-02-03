import pymongo

client = pymongo.MongoClient("mongodb+srv://7datascience:admin123@cluster0.bcxjahw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

cars_db = client['Cars_DB']
cars_t = cars_db['Cars_T']

cars = [
    
    {"brand":"TATA","color":"Blue","seating":5,"engine":"Petrol"},

    {"brand":"Toyota","color":"Black","seating":7,"engine":"Diesel"},

    {"brand":"Benz","color":"Red","seating":4,"engine":"Diesel"},

    {"brand":"TATA","color":"Blue","seating":5,"engine":"Electric"},

    {"brand":"TATA","color":"Silver","seating":5,"engine":"Electric"},

    {"brand":"TATA","color":"Blue","seating":5,"engine":"Diesel"},

    {"brand":"Hyundai","color":"Green","seating":5,"engine":"Electric"},

    {"brand":"Hyundai","color":"Grey","seating":5,"engine":"Petrol"},

    {"brand":"Maruthi","color":"Grey","seating":5,"engine":"Petrol"},

    {"brand":"Maruthi","color":"Yellow","seating":11,"engine":"Diesel"},

]



# cars_t.insert_many(cars)

# d = cars_t.find({'color':'Blue'})

# d = cars_t.find({'color':{'$in':['Blue','Red','Green']}})

# d = cars_t.find({'seating':{"$gt" : 5}})

# d = cars_t.find({'seating':{"$gte" : 5}})

# d = cars_t.find({'seating': 5})

# d = cars_t.find({"brand":"TATA","engine":"Electric"})

# d = cars_t.find({"engine":"Diesel", "seating":{"$gte":5}})

# d = cars_t.find({"$or":[{"brand":"Benz"},{"color":'Grey'}]})

# d = cars_t.find({"$and":[{"brand":"Benz"},{"color":'Red'}]})

# d = cars_t.find()

# for i in d:
#     print(i)


# cars_t.update_one({"brand":"Benz"},{"$set":{"brand":"Tesla"}})

cars_t.delete_one({"brand":"Tesla"})

# cars_t.drop()