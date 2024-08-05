from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi

try:
    client = MongoClient(
    "mongodb+srv://astrebovaolga01:01061970@cluster0.ccslbtj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

    db = client.book

except errors.ConnectionError as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

def update_cat_age_by_name(cat_name, new_age):
    """
    Оновлює вік кота за ім'ям.
    """
    result = db.cats.update_one(
        {"name": cat_name},
        {"$set": {"age": new_age}}
    )
    
    if result.matched_count > 0:
        print(f"Updated age for {cat_name} to {new_age}.")
    else:
        print(f"No cat found with the name {cat_name}.")

def add_feature_to_cat_by_name(cat_name, new_feature):
    """
    Додає нову характеристику до списку features кота за ім'ям.
    """
    result = db.cats.update_one(
        {"name": cat_name},
        {"$addToSet": {"features": new_feature}}
    )
    
    if result.matched_count > 0:
        print(f"Added feature '{new_feature}' to {cat_name}.")
    else:
        print(f"No cat found with the name {cat_name}.")

if __name__ == "__main__":
    # Запит користувача на введення імені кота
    cat_name = input("Enter the cat's name: ")
    
    # Оновлення віку кота
    new_age = int(input("Enter the new age for the cat: "))
    update_cat_age_by_name(cat_name, new_age)
    
    # Додавання нової характеристики до списку features
    new_feature = input("Enter a new feature to add: ")
    add_feature_to_cat_by_name(cat_name, new_feature)
