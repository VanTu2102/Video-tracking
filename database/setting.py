from pathlib import Path
import pymongo
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    "mongodb": {
        "NAME": "vector_db",
    }
}

def connect_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")[DATABASES["mongodb"]["NAME"]]
    return client

print(connect_db().list_collection_names())