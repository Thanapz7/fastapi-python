from cgi import test
from lib2to3.pgen2.token import OP
from unicodedata import name
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from action import Action

app = FastAPI()

class User(BaseModel):
    ID : Optional[int]
    username : Optional[str]
    password : Optional[str]
    name : Optional[str]
    last_name : Optional[str]
    address : Optional[str]
    
class login(BaseModel):
    username : Optional[str]
    password : Optional[str]

class deleteUser(BaseModel):
    ID : Optional[str]

class changeNameLast(BaseModel):
    ID : Optional[int]
    name : Optional[str]
    last_name : Optional[str]
    
    
#-------------------------------------
@app.get("/my_name")
async def my_name(name):
    data = "Thanaphon Phetcharat"
    return data

@app.get("/input_name")
async def input_name(name):
    data = name
    return data

@app.get("/")
async def read_root():
    return {"Con" : "Start"}

@app.get("/hw/get")
async def hw_get():
    data = Action.getHW()
    return data

@app.get("/hw/get_byid")
async def hw_getbyid(ID):
    data = Action.getHWByID(ID)
    return data
   
@app.get("/hw/get_byname")
async def hw_getbyname(name):
    data = Action.getHWByName(name)
    return data

@app.get("/hw/insert")
async def hw_insert(name, hw_name, status, value):
    data = Action.insertHW(name, hw_name, status, value)
    return data

@app.get("/hw/update_status")
async def hw_updatestatus(ID, status):
    data = Action.updatestatusHW(ID, status)
    return data

@app.get("/hw/update_value")
async def hw_updatevalue(ID, value):
    data = Action.updatevalueHW(ID, value)
    return data

@app.get("/hw/delete")
async def hw_delete(ID):
    data = Action.deleteHW(ID)
    return data

@app.get("/hw/update_status_value")
async def updateHW_StatusValue(ID, status, value):
    data = Action.updateHW_StatusValue(ID, status, value)
    return data


@app.post("/login")
async def login(user :login):
    data = Action.login(user)
    return data

@app.post("/register")
async def registers(user :User):
    data = Action.register(user)
    return data

@app.post("/change_password")
async def change_password(user :User):
    data = Action.changePassword(user)
    return data

@app.post("/delete_user")
async def delete_user(user:deleteUser):
    data = Action.deleteUser(user)
    return data

@app.post("/changeName_lastname")
async def changeName_lastname(user :changeNameLast):
    data = Action.changeName_Lastname(user)
    return data

if __name__ == "_main_":
    uvicorn.run(app, host="192.168.1.2", port=8000)
