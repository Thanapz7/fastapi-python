import mysql.connector


def con():
    mydb = mysql.connector.connect(
            host="localhost",
            user="test",
            password="12345",
            database="test"
        )
    return mydb

class Con:
    def getHW():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hardware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def getHWByID(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hardware WHERE ID={}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
        
    def getHWByName(name):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hardware WHERE Name ='{}'".format(name)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def insertHW(name, hw_name, status, value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hardware (name, hw_name, status, value) VALUES ('{}', '{}', '{}', {})".format(name, hw_name, status, value)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID
    
    def updatestatusHW(ID, status):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hardware SET status = '{}' WHERE ID = {}".format(status, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def updatevalueHW(ID, value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hardware SET value = {} WHERE ID = {}".format(value, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def deleteHW(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hardware WHERE ID='{}'".format(ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def updateHW_StatusValue(ID, status, value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hardware SET status = '{}', value = {} WHERE ID = {}".format(status,value,ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    
class Con2:
    def login(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users WHERE username='{}' and password = '{}'".format(user.username, user.password)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data 
    
    def getuser(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
    
    def register(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO users (username, password, name, last_name, address) VALUES ('{}', '{}', '{}', '{}', '{}')".format(user.username, user.password, user.name, user.last_name, user.address)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        ID = mycursor.lastrowid
        return ID
    
    def checkUserForRegister(username):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT username FROM users WHERE username='{}'".format(username)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data 
    
    def changePassword(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE users SET password = '{}' WHERE id = {}".format(user.password, user.ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def deleteUser(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM users WHERE id = {}".format(user.ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def changeName_Lastname(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE users SET name = '{}' lastname = '{}' WHERE id = {}".format(user.name, user.lastname, user.ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True