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

def delete_cat_by_name(cat_name):
    """
    Видаляє запис про кота за ім'ям.
    """
    result = db.cats.delete_one({"name": cat_name})
    
    if result.deleted_count > 0:
        print(f"Deleted cat with the name {cat_name}.")
    else:
        print(f"No cat found with the name {cat_name}.")

def delete_all_cats():
    """
    Видаляє всі записи з колекції cats.
    """
    result = db.cats.delete_many({})
    
    print(f"Deleted {result.deleted_count} cats.")

if __name__ == "__main__":
    # Видалення кота за ім'ям
    cat_name = input("Enter the cat's name to delete: ")
    delete_cat_by_name(cat_name)
    
    # Видалення всіх записів
    confirm = input("Do you really want to delete all cats? (yes/no): ")
    if confirm.lower() == 'yes':
        delete_all_cats()
    else:
        print("Operation cancelled.")
