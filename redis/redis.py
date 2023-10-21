from fastapi import FastAPI
import uvicorn
import redis
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Redis password from the environment variables
redis_password = os.getenv("REDIS_PASSWORD")

app = FastAPI()

# Define your Redis credentials
redis_url = f"redis://default:{redis_password}@containers-us-west-91.railway.app:6708"

@app.get("/")
async def read_redis_key(key: str):
    try:
        client = redis.from_url(redis_url)
        if key == "list_keys":
            # List all keys in the Redis database
            keys = [key.decode('utf-8') for key in client.keys('*')]
            return {"keys": keys}
        value = client.get(key)
        if value is not None:
            return {"key": key, "value": value.decode('utf-8')}
        else:
            return {"error": "Key not found in Redis"}
    except Exception as e:
        return {"error": f"Failed to connect to Redis: {e}"}

if __name__ == "__redis__":
    uvicorn.run(app, host="0.0.0.0", port=8883)
