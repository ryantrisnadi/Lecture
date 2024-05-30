'''
Introduction to HTTP and communication process

http isa protocol that allows communication'''

from fastapi import FastAPI
#import pandas as pd
"""
#membuat object FastAPI()
app = FastAPI()

df = pd.read_csv("dataset.csv")

@app.get("/")
def getHome():
    return{
        "message": "selamat datang di home!"
    }

@app.get("/all-data")
def getAllData():
    return df.to_dict(orient='records')
"""

"""
data = []

##membuat endpoint (URL) untuk home/halaman utama

@app.get("/")
def getHome():
    return{
        "message": "selamat datang di home!"
    }

@app.post("/new")
def newdata(add_data:dict): 
    # menyiapkan data yang akan ditambahkan
    value_id = len(data) + 1
    add_data["id"] = value_id
    #add_data["name"] = "Budi"
    #add_data["address"] = "Jakarta"
    #memassukkan dictionary ke dalam list
    data.append(add_data)
    return add_data

    

"""
#uvicorn API_test:app --reload
# add /docs in the end

