from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel
import os
import dotenv
dotenv.load_dotenv()

app = FastAPI()

db = mysql.connector.connect(
    host=os.environ.get("MYSQL_HOST"),
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    database=os.environ.get("MYSQL_DATABASE") 
)
print(db, flush=True)
cursor = db.cursor()

db.commit()

class CallRecord(BaseModel):
    username: str
    call_duration: int


@app.post('/mobile/{call_record.username}/call')
async def record_call(call_record: CallRecord):
    try:
        cursor.execute("""
            INSERT INTO calls (username, call_duration)
            VALUES (%s, %s)
        """, (call_record.username, call_record.call_duration))
        db.commit()
        return {'message': 'Call recorded successfully'}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/mobile/{username}/billing/')
async def get_billing_info(username: str):
    try:
        cursor.execute("""
            SELECT COUNT(*) as call_count, SUM(CEIL(call_duration / 30)) as block_count
            FROM calls
            WHERE username = %s
        """, (username,))
        result = cursor.fetchone()
        return {
            'call_count': result[0],
            'block_count': result[1]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
