from fastapi import FastAPI
from typing import Optional

app = FastAPI()
NSP_Data ={
   'Ivan': {'Fullname':'Ivan Sasu','age':24, 'Complexion':'Chocolate', 'Marital status':'Single'},
    'Karen': {'Occupation':'Software Eng.','gender':'Female','marital status':'Taken','complexion':'chocolate'},
    'Dennis': {'Height':1.9,'weight':82},
}
    


@app.get('/getNSPData')
def get_posts(search:Optional[str]=None):
    index = search
    if index == None:
        return NSP_Data
    elif index in NSP_Data :
        return {
            index :NSP_Data[index]
        }
    elif index not in NSP_Data:
        return {
            'message':'User not found'
        }

