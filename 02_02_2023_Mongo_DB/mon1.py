import pymongo

client = pymongo.MongoClient("mongodb+srv://7datascience:admin123@cluster0.bcxjahw.mongodb.net/?retryWrites=true&w=majority")

# To test connection
db = client.test

# Below line is used to create a database
database_name = client['MLearning']

# For creating a collection
collection_name = database_name['M_Topics']


data1 = {
        "Topic_1" : "Python",
        "Topic_2":"SQL",
        "Topic_3":"Pandas",
        }

data2 = {
        "Topic_1" : "JS",
        "Topic_2":"SQL",
        "Topic_3":"HTML",
        "Topic_4":"CSS"
        }

data3 = {
        "Topic_1" : "Python",
        "Topic_2":"SQL",
        "Topic_3":{"Topic_1" : "JS","Topic_2":"SQL","Topic_3":"HTML","Topic_4":"CSS"}
        }

# collection_name.insert_one(data3)

list_of_records = [
{"Name":"Poorna", "Qualification":"B.E","City":"CKM"},
{"Name":"Mahendra","State":"AP","City":"PRA"},
{"Name":"Kalpana","Qualification":"MSc","Course":"DS"}
]

# collection_name.insert_many(list_of_records)

students_db = client['students_db']
Student_Information = students_db["Student_Information"]

lst = [
    {"Name":"Kalpana","Course":"DS","Topics":['Python','SQL','Mongo']},
    {"Name":"Mahendra","Course":"DS","Topics":['Python','SQL','Mongo'],'Intrest':"JS"}
]

Student_Information.insert_many(lst)