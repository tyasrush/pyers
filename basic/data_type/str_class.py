import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

_TestString = "testing d"

def print_str():
    print(_TestString)

class Metadata(BaseModel):
    _id: uuid.UUID
    account_email: str
    table_name: str
    symbol: str
    last_sync_timestamp: int
    last_record_timestamp: int
    last_record_id: str
    created_at: Optional[datetime]

    