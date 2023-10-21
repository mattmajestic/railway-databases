from fastapi import FastAPI
import psycopg2
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables from the .env file
load_dotenv()

app = FastAPI()

# Retrieve PostgreSQL credentials from environment variables
pg_database_url = os.getenv("DATABASE_URL")
pg_user = os.getenv("PGUSER")
pg_password = os.getenv("PGPASSWORD")
pg_host = os.getenv("PGHOST")
pg_database = os.getenv("PGDATABASE")
pg_port = os.getenv("PGPORT")

# Create a PostgreSQL connection
pg_connection = psycopg2.connect(
    database=pg_database,
    user=pg_user,
    password=pg_password,
    host=pg_host,
    port=pg_port
)

@app.get("/")
async def list_data():
    cursor = pg_connection.cursor()
    cursor.execute("SELECT * FROM majesticcoding")  # Replace 'majesticcoding' with your table name
    data = cursor.fetchall()
    cursor.close()

    return {"data": data}

if __name__ == "__postgres__":
    uvicorn.run(app, host="0.0.0.0", port=8882)
