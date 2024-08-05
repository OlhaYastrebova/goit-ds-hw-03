from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://astrebovaolga01:01061970@cluster0.ccslbtj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)
db = client.book

result = db.cats.find({})
for el in result:
    print(el)

def get_cat_info_by_name(cat_name):
    # Підключення до MongoDB
    client = MongoClient(
        "mongodb+srv://astrebovaolga01:01061970@cluster0.ccslbtj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        server_api=ServerApi('1')
    )
    
    # Вибір бази даних
    db = client.book
    
    # Пошук кота за ім'ям
    result = db.cats.find_one({"name": cat_name})
    
    # Перевірка результату
    if result:
        print(result)
    else:
        print(f"No cat found with the name {cat_name}")

if __name__ == "__main__":
    # Запит користувача на введення імені кота
    cat_name = input("Enter the cat's name: ")
    get_cat_info_by_name(cat_name)