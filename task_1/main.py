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


result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

print(result_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)

