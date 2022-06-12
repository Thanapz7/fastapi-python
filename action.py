from distutils.log import error

from xmlrpc.client import boolean

from numpy import delete
from conDB import Con,Con2

class Action:
    def getHW():
        data = Con.getHW()
        return data
    
    def getHWByID(ID):
        data = Con.getHWByID(ID)
        return data
    
    def getHWByName(name):
        data = Con.getHWByName(name)
        return data
    
    def insertHW(name, hw_name, status, value):
        data = Con.insertHW(name, hw_name, status, value)
        return data
    
    def updatestatusHW(ID, status):
        data = Con.updatestatusHW(ID, status)
        if(boolean):
            data = Con.getHWByID(ID)
        else:
            data = {"erroe" : True}
        return data
    
    def updatevalueHW(ID, value):
        data = Con.updatevalueHW(ID, value)
        if(boolean):
            data = Con.getHWByID(ID)
        else:
            data = {"error" : True}
        return data
    
    def deleteHW(ID):
        boolean = Con.deleteHW(ID)
        if boolean:
            data = {"error": False, "Delete": "Succeses"}
        else:
            data = {"error": True}
        return data
    
    def updateHW_StatusValue(ID, status, value):
        data = Con.updateHW_StatusValue(ID, status, value)
        if(boolean):
            data = Con.getHWByID(ID)
        else:
            data = {"error" : True}
        return data
    
    def login(user):
        user = Con2.login(user)
        if(user): 
            data = {"error" : False, "user":user}
            return data
        else:
            data = {"error" : True}
            return data
        
    def register(user):
        checkUser = Con2.checkUserForRegister(user.username)
        if(not checkUser):
            ID = Con2.register(user)
            data = Con2.getuser(ID)
            return data
        else:
            data = {"error" : True, "username" : 'error'}
            return data
    
    def changePassword(user):
        boolean = Con2.changePassword(user)
        if boolean():
            data = Con2.getuser(user.ID)  
            return data
        else:
            data = {"error" : True, "username" : 'error'}
            return data
    
    def deleteUser(user):
        boolean = Con2.deleteUser(user)
        if(boolean):
            data = {"error": False,}
            return data
        else:
            data = {"error": True,}
            return data
    
    def changeName_Lastname(user):
        boolean = Con2.changeName_Lastname(user)
        if boolean():
            data = Con2.getuser(user.ID)  
            return data
        else:
            data = {"error" : True, "username" : 'error'}
            return data
