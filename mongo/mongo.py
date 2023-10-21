from fastapi import FastAPI
import pymongo
from dotenv import load_dotenv
import os
from bson import ObjectId
import uvicorn

# Load environment variables from the .env file
load_dotenv()

app = FastAPI()

# Retrieve the MongoDB password from the environment variable
mongo_password = os.getenv("MONGO_PASSWORD")

# Define your MongoDB credentials
mongo_url = f"mongodb://mongo:{mongo_password}@containers-us-west-58.railway.app:6946"
mongo_client = pymongo.MongoClient(mongo_url)

# Connect to the MongoDB database (replace 'test' with the actual database name)
db = mongo_client['test']

# Access a collection within the database (replace 'majesticcoding' with the actual collection name)
collection = db['majesticcoding']

@app.get("/")
async def list_data():
    # Retrieve data from the MongoDB collection and convert ObjectId to string
    data = list(collection.find({}))  # Find all documents in the collection
    serialized_data = [
        {k: str(v) if isinstance(v, ObjectId) else v for k, v in item.items()} for item in data
    ]

    return {"data": serialized_data}

if __name__ == "__mongo__":
    uvicorn.run(app, host="0.0.0.0", port=8881)
