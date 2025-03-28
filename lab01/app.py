from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Определяем модели данных
class PhoneNumber(BaseModel):
    TypeID: int
    CountryCode: int
    Operator: int
    Number: int

class Contact(BaseModel):
    ID: int
    Username: str
    GivenName: str
    FamilyName: str
    FullName: str
    Phone: List[PhoneNumber]
    Email: List[str]
    Birthdate: str  

class Group(BaseModel):
    ID: int
    Title: str
    Description: str
    Contacts: List[int]

# CRUD заглушки
@app.post("/api/v1/contact")
async def create_contact(contact: Contact):
    return {}

@app.get("/api/v1/contact")
async def read_contact():
    return {}

@app.put("/api/v1/contact")
async def update_contact(contact: Contact):
    return {}

@app.delete("/api/v1/contact")
async def delete_contact():
    return {}

@app.post("/api/v1/group")
async def create_group(group: Group):
    return {}

@app.get("/api/v1/group")
async def read_group():
    return {}

@app.put("/api/v1/group")
async def update_group(group: Group):
    return {}

@app.delete("/api/v1/group")
async def delete_group():
    return {}